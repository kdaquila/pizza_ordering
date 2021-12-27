import axios from "axios";

export async function place_order(url: string, pizza_type: string) {
  return await axios.post(url, {
    pizza_type: pizza_type,
  });
}
