import { Hero } from "../Hero/Hero";
import { OrderItem } from "../OrderItem/OrderItem";
import styles from "./Orders.module.scss";

export function Orders() {
  return (
    <div className="container">
      <Hero title="Orders" subtitle="View and cancel orders below" />
      <div className={styles.orderWrapper}>
          <OrderItem />
          <OrderItem />
          <OrderItem />
          <OrderItem />
          <OrderItem />
      </div>
    </div>
  );
}
