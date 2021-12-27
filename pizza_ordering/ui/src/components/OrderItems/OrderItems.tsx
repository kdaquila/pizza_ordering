import { useEffect, useState } from "react";
import { get_orders } from "../../core/get_orders";
import { PizzaOrder } from "../../core/pizza_order";
import { OrderItem } from "../OrderItem/OrderItem";
import styles from "./OrderItems.module.scss";

const pizzaEndpoint = "http://127.0.0.1:8000/api/pizza";

const OrderData: PizzaOrder[] = [
  {
    id: "1",
    name: "Cheese Pizza",
    status: "cooking",
    startTime: "2021-08-19 5:51",
    stopTime: "2021-08-19 5:51",
  },
  {
    id: "2",
    name: "Pepperoni Pizza",
    status: "cooking",
    startTime: "2021-08-19 5:51",
    stopTime: "2021-08-19 5:51",
  },
  {
    id: "3",
    name: "Veggie Pizza",
    status: "cooking",
    startTime: "2021-08-19 5:51",
    stopTime: "2021-08-19 5:51",
  },
  {
    id: "4",
    name: "Veggie Pizza",
    status: "cooking",
    startTime: "2021-08-19 5:51",
    stopTime: "2021-08-19 5:51",
  },
  {
    id: "5",
    name: "Veggie Pizza",
    status: "cooking",
    startTime: "2021-08-19 5:51",
    stopTime: "2021-08-19 5:51",
  },
];

export function OrderItems() {
  const [orderData, setOrderData] = useState<PizzaOrder[]>();

  useEffect(() => {
    get_orders(pizzaEndpoint).then((orders) => {
      setOrderData(orders);
    });
  }, []);

  return (
    <div className={styles.orderWrapper}>
      {orderData &&
        orderData.map((item) => {
          return (
            <OrderItem
              key={item.id}
              id={item.id}
              name={item.name}
              startTime={item.startTime}
              stopTime={item.stopTime}
              status={item.status}
              pizzaEndpoint={pizzaEndpoint}
            />
          );
        })}
    </div>
  );
}
