import { Hero } from "../Hero/Hero";
import { MenuItems } from "../MenuItems/MenuItems";

export function Menu() {
  return (
    <div className="container">
      <Hero title="Menu" subtitle="Click an item below to submit order" />
      <MenuItems />
    </div>
  );
}
