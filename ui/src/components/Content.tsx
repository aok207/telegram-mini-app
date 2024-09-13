import { Data } from "@/types";
import ShowBasedOnTag from "./ShowBasedOnTag";

const Content = ({ data }: { data: Data }) => {
  return (
    <div className="flex flex-col gap-4">
      <h1 className="font-bold text-3xl">{data.meta_data.title}</h1>
      <div className="flex gap-3">
        <p className="text-gray-600">{data.meta_data.author}</p>
        {data.meta_data.published_date !== "Unknown" && (
          <p className="text-gray-600">
            Published: {data.meta_data.published_date}
          </p>
        )}
      </div>

      {data.meta_data.og_img !== "" && (
        <div className="w-full h-fit object-cover rounded-md">
          <img
            src={data.meta_data.og_img}
            alt={data.meta_data.title}
            className="w-full h-full"
          />
        </div>
      )}

      {data.contents.map((content, index) => (
        <div key={index} className="flex gap-4">
          <ShowBasedOnTag content={content} />
        </div>
      ))}
    </div>
  );
};

export default Content;
