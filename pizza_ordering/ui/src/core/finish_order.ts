import axios from "axios";

export async function finish_order(baseUrl: string, pizza_id: string) {
  const url = `${baseUrl}/${pizza_id}/finish`;
  const response = await axios.put(url);
  console.log(response);
  return response.data.data;
}
