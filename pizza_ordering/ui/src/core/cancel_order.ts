import axios from "axios";

export async function cancel_order(baseUrl: string, pizza_id: string) {
    const url = `${baseUrl}/${pizza_id}/cancel`;
    const response = await axios.put(url);
    console.log(response);
    return response.data.data;
}