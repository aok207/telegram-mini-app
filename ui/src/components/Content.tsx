import type { Content, Data, MetaData } from "@/types";
import ShowBasedOnTag from "./ShowBasedOnTag";
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";

const Content = ({ data }: { data: Data[] }) => {
  return (
    <Accordion type="multiple" collapsible>
      {data.map((content, index) => {
        const url: string = Object.keys(content)[0];
        const data: {
          page_type: string;
          meta_data: MetaData;
          contents: Content[];
        } = content[url];

        return (
          <AccordionItem key={url} value={`link-${index + 1}`}>
            <AccordionTrigger>{url}</AccordionTrigger>
            <AccordionContent>
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
            </AccordionContent>
          </AccordionItem>
        );
      })}
    </Accordion>
  );
};

export default Content;
