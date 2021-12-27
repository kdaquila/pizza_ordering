import { delete_orders } from "../../core/delete_orders";
import { SecondaryButton } from "../Buttons/SecondaryButton";
import { Hero } from "../Hero/Hero";
import { OrderItems } from "../OrderItems/OrderItems";

export function Orders() {



  return (
    <div className="container">
      <Hero title="Orders" subtitle="View and cancel orders below" />
      <OrderItems />
    </div>
  );
}
