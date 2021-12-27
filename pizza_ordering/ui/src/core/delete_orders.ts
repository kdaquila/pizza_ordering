import axios from "axios";

export async function delete_orders(url: string) {
  await axios.delete(url);
}
