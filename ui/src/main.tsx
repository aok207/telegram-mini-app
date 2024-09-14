import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App.tsx";
import "./index.css";
import { TelegramProvider } from "./context/TelegramContext.tsx";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { Toaster } from "react-hot-toast";

const queryClient = new QueryClient();

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <QueryClientProvider client={queryClient}>
      <TelegramProvider>
        <App />
        <Toaster
          toastOptions={{
            style: {
              wordBreak: "break-all",
              maxWidth: 350,
            },
          }}
        />
      </TelegramProvider>
    </QueryClientProvider>
  </StrictMode>
);
