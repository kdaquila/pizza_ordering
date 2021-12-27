import img1 from "../../img/cheese_pizza.png";
import styles from "./MenuItem.module.scss";

export function MenuItem(props: { name: string; description: string }) {
  return (
    <button className={styles.menuItem}>
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
