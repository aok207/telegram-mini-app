import { useState } from "react";
import LinkForm from "./components/LinkForm";
// import useTelegram from "./hooks/useTelegram";
import { Data } from "./types";
import Content from "./components/Content";

const App = () => {
  // const { user } = useTelegram();
  const [data, setData] = useState<Data | null>(null);

  return (
    <div className="font-inter w-full md:max-w-[600px] mx-auto h-full flex flex-col gap-14">
      <h1 className="font-bold text-3xl text-center mt-24">
        Contact <span className="text-purple-600">Crawl</span>
      </h1>
      <div className="w-3/4 mx-auto flex flex-col gap-8">
        <LinkForm setData={setData} />
        {data && <Content data={data} />}
      </div>
    </div>
  );
};

export default App;
