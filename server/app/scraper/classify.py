""" This file will classify whether the url is a blog list or a single blog """

import re
from typing import Literal, cast

from bs4 import BeautifulSoup
import json


def load_words() -> set[str]:
    with open("words_dictionary.json") as file:
        data = cast(dict[str, int], json.load(file))

    return set(data.keys())


def is_blog_list(url: str) -> bool:
    url_patterns = [
        r"/page/",
        r"/category/",
        r"/tag/",
        r"/blog$",
        r"/posts$",
        r"/article",
    ]

    if any(re.search(pattern, url) for pattern in url_patterns):
        return True

    split_url = url.split("/")
    last_word = split_url[-1]

    if not last_word.isnumeric() or "-" not in last_word or last_word in load_words():
        return True

    return False


def has_pagination(url: str, soup: BeautifulSoup) -> bool:
    if "page" in url.lower():
        return True
    if soup.find("a", text=re.compile(r"next", re.I)) is not None:
        return True
    if soup.find("a", attrs={"href": re.compile(r"page", re.I)}) is not None:
        return True
    return False


def classify_page(url: str, soup: BeautifulSoup) -> Literal["blog-list", "single-blog"]:
    return (
        "blog-list" if is_blog_list(url) or has_pagination(url, soup) else "single-blog"
    )
