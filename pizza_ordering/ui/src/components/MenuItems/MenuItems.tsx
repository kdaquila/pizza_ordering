import { useEffect, useState } from "react";
import { MenuItem } from "../MenuItem/MenuItem";
import styles from "./MenuItems.module.scss";

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

type PizzaMenuItem = {
  id: string;
  name: string;
  description: string;
};

export function MenuItems() {
  const [pizzaMenuItem, setPizzaMenuItems] = useState<PizzaMenuItem[]>();

  useEffect(() => {
    setPizzaMenuItems(PizzaData)
  }, [pizzaMenuItem]);

  return (
    <div className="d-flex justify-content-center">
      <div className={styles.menuItemSet}>
        {pizzaMenuItem &&
          pizzaMenuItem.map((item) => {
            return (
              <MenuItem
                key={item.id}
                name={item.name}
                description={item.description}
              />
            );
          })}
      </div>
    </div>
  );
}
