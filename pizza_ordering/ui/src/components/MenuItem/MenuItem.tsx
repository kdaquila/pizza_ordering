import { useContext } from "react";
import { AppContext } from "../../App";
import { place_order } from "../../core/place_order";
import styles from "./MenuItem.module.scss";

export function MenuItem(props: {
  name: string;
  description: string;
  orderUrl: string;
  pizza_type: string;
  img_obj: any;
}) {
  const appContext = useContext(AppContext);

  async function handleClick() {
    const response = await place_order(props.orderUrl, props.pizza_type);
    console.log(response)
    const message = response.data.message;
    appContext?.setFlashMessage(message)
  }

  return (
    <button className={styles.menuItem} onClick={handleClick}>
      <div className={styles.menuItem__imgArea}>
        <img
          className={styles.menuItem__img}
          src={props.img_obj}
          alt="cheese pizza"
        />
      </div>
      <div className={styles.menuItem__textArea}>
        <h2 className={styles.menuItem__title}>{props.name}</h2>
        <h3 className={styles.menuItem__subtitle}>{props.description}</h3>
      </div>
    </button>
  );
}
