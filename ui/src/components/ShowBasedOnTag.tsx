import { Content } from "@/types";
import React from "react";

interface ShowBasedOnTagProps {
  content: Content;
}

const ShowBasedOnTag = ({ content }: ShowBasedOnTagProps) => {
  /*
    Content structure is like this:
      if it is an image, only img property will be there
      if it is a text, tag, and text properties will be there
      if it is a link, tag, text, and link properties will be there
  */

  return (
    <>
      {content.img ? (
        <div className="w-full object-cover rounded-lg overflow-hidden">
          <img src={content.img} className="w-full h-full" loading="lazy" />
        </div>
      ) : (
        <>
          {content.link && content.tag === "a" ? (
            <a
              href={content.link}
              className="text-blue-400 hover:text-blue-500 hover:underline"
              target="_blank"
            >
              <i>{content.text}</i>
            </a>
          ) : (
            <>
              {content.tag &&
                content.text &&
                React.createElement(
                  content.tag as string,
                  {
                    className: content.tag?.startsWith("h")
                      ? "text-2xl font-bold"
                      : content.tag === "time"
                      ? "italic text-gray-400 text-semibold"
                      : "",
                  },
                  content.text
                )}
            </>
          )}
        </>
      )}
    </>
  );
};

export default ShowBasedOnTag;
