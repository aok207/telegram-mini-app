import LinkForm from "./components/LinkForm";

const App = () => {
  return (
    <div className="font-inter w-full h-full flex flex-col gap-14">
      <h1 className="font-bold text-3xl text-center mt-24">
        Contact <span className="text-purple-600">Crawl</span>
      </h1>
      <div className="w-3/4 mx-auto">
        <LinkForm />
      </div>
    </div>
  );
};

export default App;
