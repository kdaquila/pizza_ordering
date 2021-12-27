import { useEffect, useState } from "react";
import { delete_orders } from "../../core/delete_orders";
import { get_orders } from "../../core/get_orders";
import { PizzaOrder } from "../../core/pizza_order";
import { SecondaryButton } from "../Buttons/SecondaryButton";
import { OrderItem } from "../OrderItem/OrderItem";
import styles from "./OrderItems.module.scss";

const pizzaEndpoint = "http://127.0.0.1:8000/api/pizza";

export function OrderItems() {
  const [orderData, setOrderData] = useState<PizzaOrder[]>();

  useEffect(() => {
    handleUpdateOrders();
  }, []);

  function handleUpdateOrders() {
    get_orders(pizzaEndpoint).then((orders) => {
      setOrderData(orders);
    });
  }

  function handleDeleteOrders() {
    const url = `http://127.0.0.1:8000/api/pizza`;
    delete_orders(url).then(() => handleUpdateOrders());
  }

  const isOrders = orderData && orderData.length > 0

  let placeholder = null
  if (!isOrders) {
    placeholder = <p className={styles.ordersPlaceholder}>No orders right now</p>
  }

  return (
    <div>
      <div className="d-flex justify-content-center">
        {isOrders && <SecondaryButton
          title="Delete All"
          disabled={false}
          onClick={handleDeleteOrders}
          fluid={false}
        />}
      </div>
      <div className={styles.orderWrapper}>
        {placeholder}
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
                onUpdateOrders={handleUpdateOrders}
              />
            );
          })}
      </div>
    </div>
  );
}
