import img1 from "../img/cheese_pizza.png";
import styles from "./MenuItem.module.scss";

export function MenuItem() {
  return (
    <button className={styles.menuItem}>
      <div className={styles.menuItem__imgArea}>
        <img className={styles.menuItem__img} src={img1} alt="cheese pizza" />
      </div>
      <div className={styles.menuItem__textArea}>
        <h2 className={styles.menuItem__title}>Cheese Pizza</h2>
        <h3 className={styles.menuItem__subtitle}>
          Thin crust with mozzarella cheese and tomato sauce. Serves
          one(11&quot;)
        </h3>
      </div>
    </button>
  );
}
