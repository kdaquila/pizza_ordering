import { useEffect, useState } from "react";
import { OrderItem } from "../OrderItem/OrderItem";
import styles from "./OrderItems.module.scss";

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

export type PizzaOrder = {
  id: string;
  name: string;
  startTime: string;
  stopTime: string;
  status: string;
};

export function OrderItems() {
  const [orderData, setOrderData] = useState<PizzaOrder[]>();

  useEffect(() => {
    setOrderData(OrderData)
  }, [orderData])

  return (
    <div className={styles.orderWrapper}>
      {orderData && orderData.map((item) => {
        return (
          <OrderItem
            key={item.id}
            id={item.id}
            name={item.name}
            startTime={item.startTime}
            stopTime={item.stopTime}
            status={item.status}
          />
        );
      })}
    </div>
  );
}
