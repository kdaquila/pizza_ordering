import { OrderItem } from "../OrderItem/OrderItem";

export function Orders() {
  return (
    <div className="container d-flex justify-content-center flex-wrap">
      <OrderItem />
      <OrderItem />
      <OrderItem />
      <OrderItem />
      <OrderItem />
    </div>
  );
}
