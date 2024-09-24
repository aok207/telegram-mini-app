import { ApiResponse } from "./types";

const serverBaseUrl = import.meta.env.VITE_SERVER_URL;

export async function submitForm(data: {
  url: string;
  depth: number;
}): Promise<ApiResponse> {
  return fetch(`${serverBaseUrl}/submit`, {
    headers: {
      "Content-Type": "application/json",
    },
    method: "POST",
    body: JSON.stringify(data),
  }).then((res) => res.json());
}
