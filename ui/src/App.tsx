import { useState } from "react";
import LinkForm from "./components/LinkForm";
// import useTelegram from "./hooks/useTelegram";
import { Data } from "./types";
import Content from "./components/Content";
import { Button } from "./components/ui/button";
import useDownload from "./hooks/useDownload";

const App = () => {
  // const { user } = useTelegram();
  const [data, setData] = useState<Data[] | null>(null);
  const { download } = useDownload({
    data: [JSON.stringify(data, null, 2)],
    fileName: data ? data[0][Object.keys(data[0])[0]].meta_data.title : "",
  });

  return (
    <div className="font-inter w-full md:max-w-[600px] mx-auto h-full flex flex-col gap-14">
      <h1 className="font-bold text-3xl text-center mt-24">
        Contact <span className="text-purple-600">Crawl</span>
      </h1>
      <div className="w-3/4 mx-auto flex flex-col gap-8">
        <LinkForm setData={setData} />
        {data && (
          <Button type="button" variant={"outline"} onClick={download}>
            Download as json file
          </Button>
        )}

        {data && <Content data={data} />}
      </div>
    </div>
  );
};

export default App;
