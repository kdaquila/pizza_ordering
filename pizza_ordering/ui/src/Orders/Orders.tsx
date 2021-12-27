import { Hero } from "../Hero/Hero";
import { OrderItem } from "../OrderItem/OrderItem";

export function Orders() {
  return (
    <div className="container">
      <Hero title="Orders" subtitle="View and cancel orders below" />
      <div className="d-flex justify-content-center flex-wrap">
        <OrderItem />
        <OrderItem />
        <OrderItem />
        <OrderItem />
        <OrderItem />
      </div>
    </div>
  );
}
