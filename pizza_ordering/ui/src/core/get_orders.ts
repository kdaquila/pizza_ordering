import axios from "axios";
import { PizzaOrder } from "./pizza_order";

export async function get_orders(url: string): Promise<PizzaOrder[]>{
    const response = await axios.get(url)
    const order_data = response.data.data;
    const orders: PizzaOrder[] = order_data.map((item: any) => {
        return new PizzaOrder(item.pizza_id, item.name, item.start_time, item.stop_time, item.status)
    })
    return orders
}