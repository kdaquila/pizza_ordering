import { useEffect, useState } from "react";
import { MenuItem } from "../MenuItem/MenuItem";
import styles from "./MenuItems.module.scss";

import cheesePizzaImg from "../../img/cheese_pizza.png";
import pepperoniPizzaImg from "../../img/pepperoni_pizza.png";
import veggiePizzaImg from "../../img/veggie_pizza.png";

const orderUrl = "http://127.0.0.1:8000/api/pizza"
const PizzaData = [
  {
    id: "1",
    name: "Cheese Pizza",
    pizza_type: "cheese",
    description:
      "Thin crust with mozzarella cheese and tomato sauce. Serves one. 11\"",
    status: "cooking",
    start_time: "2021-08-19 5:51",
    stop_time: "2021-08-19 5:51",
    img_obj: cheesePizzaImg
  },
  {
    id: "2",
    name: "Pepperoni Pizza",
    pizza_type: "pepperoni",
    description:
      "Thin crust with pepperoni, mozzarella cheese and tomato sauce. Serves one. 11\"",
    status: "cooking",
    start_time: "2021-08-19 5:51",
    stop_time: "2021-08-19 5:51",
    img_obj: pepperoniPizzaImg
  },
  {
    id: "3",
    name: "Veggie Pizza",
    pizza_type: "veggie",
    description:
      "Thin crust with bell peppers, zucchini, olives, corn, onion, mozzarella cheese and tomato sauce. Serves one. 11\"",
    status: "cooking",
    start_time: "2021-08-19 5:51",
    stop_time: "2021-08-19 5:51",
    img_obj: veggiePizzaImg
  },
];

type PizzaMenuItem = {
  id: string;
  pizza_type: string;
  name: string;
  description: string;
  img_obj: any;
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
                orderUrl={orderUrl}
                pizza_type={item.pizza_type}
                img_obj={item.img_obj}
              />
            );
          })}
      </div>
    </div>
  );
}
