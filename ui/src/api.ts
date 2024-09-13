import { ApiResponse } from "./types";

const serverBaseUrl = import.meta.env.VITE_SERVER_URL;

export function submitForm(url: string): Promise<ApiResponse> {
  return fetch(`${serverBaseUrl}/submit`, {
    headers: {
      "Content-Type": "application/json",
    },
    method: "POST",
    body: JSON.stringify({ url }),
  }).then((res) => res.json());
}
