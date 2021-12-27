import axios from "axios";
import img1 from "../../img/cheese_pizza.png";
import styles from "./MenuItem.module.scss";

export function MenuItem(props: { name: string; description: string, orderUrl: string, pizza_type: string }) {
  function onClickHandler() {
    console.log(`send message to ${props.orderUrl} with body of: {pizza_type: ${props.pizza_type}}`)
    axios.post(props.orderUrl, {
      pizza_type: props.pizza_type
    })
  }

  return (
    <button className={styles.menuItem} onClick={onClickHandler}>
      <div className={styles.menuItem__imgArea}>
        <img className={styles.menuItem__img} src={img1} alt="cheese pizza" />
      </div>
      <div className={styles.menuItem__textArea}>
        <h2 className={styles.menuItem__title}>{props.name}</h2>
        <h3 className={styles.menuItem__subtitle}>{props.description}</h3>
      </div>
    </button>
  );
}
