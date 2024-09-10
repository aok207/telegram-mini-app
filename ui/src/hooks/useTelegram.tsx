import { TelegramContext } from "@/context/TelegramContext";
import { useContext } from "react";

const useTelegram = () => useContext(TelegramContext);

export default useTelegram;
