const useDownload = ({
  data,
  fileName,
}: {
  data: BlobPart[] | null;
  fileName: string;
}) => {
  const download = () => {
    if (!data) return;

    const file = new File(data, fileName, { type: "application/json" });
    const a = document.createElement("a");
    const url = URL.createObjectURL(file);

    a.href = url;
    a.download = file.name;
    document.body.appendChild(a);

    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  return { download };
};

export default useDownload;
