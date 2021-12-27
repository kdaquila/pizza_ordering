import { OrderItem } from "../OrderItem/OrderItem";
import styles from "./OrderItems.module.scss";


export function OrderItems() {
  return (
    <div className={styles.orderWrapper}>
      <OrderItem />
      <OrderItem />
      <OrderItem />
      <OrderItem />
      <OrderItem />
    </div>
  );
}
