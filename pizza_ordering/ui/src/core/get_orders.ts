import axios from "axios";
import { PizzaOrder } from "./pizza_order";

export async function get_orders(url: string): Promise<PizzaOrder[]> {
  const response = await axios.get(url);
  const order_data = response.data.data;
  const orders: PizzaOrder[] = order_data.map((item: any) => {
    const startTime = item.start_time
      ? new Date(Date.parse(item.start_time))
      : null;
    const stopTime = item.stop_time
      ? new Date(Date.parse(item.stop_time))
      : null;
    return new PizzaOrder(
      item.pizza_id,
      item.name,
      startTime,
      stopTime,
      item.status
    );
  });
  orders.sort((a, b) => {
    if (a.startTime === null || b.startTime === null) {
      return -1;
    }
    return a.startTime.getTime() - b.startTime.getTime();
  });
  return orders;
}
