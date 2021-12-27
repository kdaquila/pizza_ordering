import { Hero } from "../Hero/Hero";
import { MenuItems } from "../MenuItems/MenuItems";

const PizzaData = [
  {
    id: "1",
    name: "Cheese Pizza",
    description:
      "Thin crust with mozzarella cheese and tomato sauce. Serves one (11&quot;))",
    status: "cooking",
    start_time: "2021-08-19 5:51",
    stop_time: "2021-08-19 5:51",
  },
  {
    id: "2",
    name: "Pepperoni Pizza",
    description:
      "Thin crust with pepperoni, mozzarella cheese and tomato sauce. Serves one (11&quot;)",
    status: "cooking",
    start_time: "2021-08-19 5:51",
    stop_time: "2021-08-19 5:51",
  },
  {
    id: "3",
    name: "Veggie Pizza",
    description:
      "Thin crust with bell peppers, zucchini, olives, corn, onion, mozzarella cheese and tomato sauce. Serves one (11&quot;)",
    status: "cooking",
    start_time: "2021-08-19 5:51",
    stop_time: "2021-08-19 5:51",
  },
];

export function Menu() {
  return (
    <div className="container">
      <Hero title="Menu" subtitle="Click an item below to submit order" />
      <MenuItems items={PizzaData} />
    </div>
  );
}
