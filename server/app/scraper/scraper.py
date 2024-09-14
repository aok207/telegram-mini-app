import re
from collections.abc import Iterable
from typing import Final, Union, cast
from urllib.parse import urljoin

import log
import requests
from bs4 import BeautifulSoup, PageElement, Tag

from .classify import classify_page

# Set up the logger
logger = log.setup_logger(__name__)

# List of unwanted texts, typically common site elements that are not relevant for scraping
unwanted_texts: Final[list[str]] = [
    # General website links
    "follow",
    "help",
    "status",
    "about",
    "careers",
    "press",
    "blog",
    "privacy",
    "terms",
    "text to speech",
    "teams",
    "contact",
    "faq",
    "support",
    "newsletter",
    "subscribe",
    "advertise",
    "feedback",
    "community",
    "learn more",
    "join",
    "donate",
    "investors",
    "write",
    "search",
    # Social media or engagement links
    "like",
    "share",
    "tweet",
    "retweet",
    "pin",
    "save",
    "comment",
    "reply",
    "reactions",
    "recommendations",
    "follow us",
    "linkedin",
    "facebook",
    "twitter",
    "instagram",
    "youtube",
    "snapchat",
    "tiktok",
    "whatsapp",
    "reddit",
    # Legal and policy links
    "cookie policy",
    "do not sell my data",
    "terms of service",
    "privacy policy",
    "user agreement",
    "copyright",
    "accessibility",
    "licensing",
    "gdpr",
    "ccpa",
    "ethics policy",
    "terms & conditions",
    # Payment and subscription links
    "sign up",
    "sign in",
    "login",
    "log in",
    "register",
    "upgrade",
    "join",
    "get started",
    "plans",
    "pricing",
    "payment",
    "start free trial",
    "try now",
    "subscription",
    "become a member",
    "buy now",
    "purchase",
    "offers",
    "redeem",
    # Navigation and misc UI text
    "home",
    "next",
    "previous",
    "back to top",
    "load more",
    "read more",
    "more stories",
    "related posts",
    "related stories",
    "top stories",
    "sponsored",
    "recommendations",
    "skip",
    "explore",
    "menu",
    "discover",
    "topics",
    "latest",
    "trending",
    # Other common elements
    "most popular",
    "editor's picks",
    "featured",
    "breaking news",
    "in case you missed it",
    "more from",
    "watch",
    "video",
    "advertisement",
    "ads",
    "promoted",
    "sponsored content",
    "share this story, Choose your platform!",
    "email",
    # Content warnings
    "this video cannot play in your browser",
    "please enable javascript",
    "enable cookies",
    "try a different browser",
    "blocked",
    "error",
]


def get_html(url: str) -> Union[BeautifulSoup, None]:
    """
    Fetch the HTML content of the given URL and return a BeautifulSoup object.

    Args:
        url (str): The URL to fetch.

    Returns:
        Union[BeautifulSoup, None]: A BeautifulSoup object if successful, None otherwise.
    """

    try:
        req = requests.get(url)
        req.raise_for_status()
        return BeautifulSoup(req.text, "html.parser")
    except Exception as ex:
        logger.info(f"An exception occured: {ex}")


def get_meta_data(soup: BeautifulSoup) -> dict[str, str]:
    """
    Extract metadata (title, description, author, published date, etc.) from the BeautifulSoup object.

    Args:
        soup (BeautifulSoup): The parsed HTML content.

    Returns:
        dict[str, str]: A dictionary containing metadata such as title, description, author, etc.
    """

    title = (
        soup.title.string.replace("\n", "").strip()
        if soup.title and soup.title.string
        else ""
    )

    meta_description = soup.find("meta", {"name": "description"})
    description = (
        cast(Tag, meta_description).attrs["content"].replace("\n", "").strip()
        if meta_description
        else ""
    )

    meta_author = soup.find("meta", {"name": "author"})
    author = cast(Tag, meta_author).attrs["content"] if meta_author else "Anonymous"

    meta_published_date = soup.find("meta", {"name": "article:published_time"})
    published_date = (
        cast(Tag, meta_published_date).attrs["content"]
        if meta_published_date
        else "Unknown"
    )

    meta_og_img = soup.find("meta", {"property": "og:image"})
    og_img = cast(Tag, meta_og_img).attrs["content"] if meta_og_img else ""

    meta_og_type = soup.find("meta", {"property": "og:type"})
    og_type = cast(Tag, meta_og_type).attrs["content"] if meta_og_type else ""

    return {
        "title": title,
        "description": description,
        "author": author,
        "published_date": published_date,
        "og_img": og_img,
        "og_type": og_type,
    }


def extract_contents_from_descendants(
    url: str,
    descendants: Iterable[PageElement],
    contents: list[dict[str, str]],
    unwanted_parents: Union[list[str], None] = None,
    length: int = 0,
):
    """
    Extract relevant content from the HTML descendants while filtering unwanted elements.

    Args:
        url (str): The base URL used for resolving relative links.
        descendants (Iterable[PageElement]): The HTML elements to extract content from.
        contents (list[dict[str, str]]): The list to store extracted content (text, images, links).
        unwanted_parents (Union[list[str], None]): List of parent tags to ignore (e.g., "header", "footer").
        length (int): Tracks the number of extracted elements.

    """

    for c in descendants:
        if unwanted_parents and c.find_parent(unwanted_parents):
            continue

        content = {}

        if isinstance(c, Tag) and c.name == "img":
            content["img"] = urljoin(url, cast(str, c.get("src")))

        """
        To extract a text, it must not be
            - the instanace of Tag because we'll get duplicate texts otherwise (trust me)
            - in the unwanted list
            - less than 3 characters
            - inside a figure (the reason why we don't just put it in the unwanted_parents is because
                                we won't get images)
            - a link whose href contains a "#", because these are not actual links
        """

        if (
            not isinstance(c, Tag)
            and c.get_text(strip=True).lower() not in unwanted_texts
            and len(c.get_text(strip=True)) > 3
            and not c.find_parent("figure")
            and not c.find_parent("a", attrs={"href": re.compile(r"#")})
        ):

            content["tag"] = c.parent.name if c.parent else ""
            content["text"] = c.get_text(strip=True).replace("\n", "")

            if c.parent and c.parent.name == "a":
                content["link"] = urljoin(url, cast(str, c.parent.get("href")))

        if len(content.keys()) > 0:
            contents.append(content)
            length += 1


def scrape(url: str):
    """
    Main function to scrape a web page. It extracts metadata, page content,
    and handles content extraction based on page structure.

    Args:
        url (str): The URL of the page to scrape.

    Returns:
        dict: A dictionary containing page type, metadata, and extracted contents.
    """

    soup = get_html(url)

    if soup is None:
        return None

    page_type = classify_page(url, soup)

    main_ele = soup.find("main")

    meta_data = get_meta_data(soup)

    length: int = 0

    contents: list[dict[str, str]] = []

    # Extract contents from the main element if it exists
    if main_ele:
        main_ele = cast(Tag, main_ele)
        # Focus contents in the article tags
        for article in main_ele.find_all("article"):
            extract_contents_from_descendants(
                url,
                article.descendants,
                contents,
                ["button", "noscript", "header"],
                length,
            )

        # If no article tags found, extract contents from the main element
        if length == 0:
            extract_contents_from_descendants(
                url,
                main_ele.descendants,
                contents,
                ["nav", "footer", "button", "noscript", "header"],
                length,
            )

    # If no main element found, extract contents from the body element
    else:
        if soup.body:
            extract_contents_from_descendants(
                url,
                soup.body.descendants,
                contents,
                ["nav", "footer", "button", "noscript", "header"],
                length,
            )

    return {"page_type": page_type, "meta_data": meta_data, "contents": contents}
