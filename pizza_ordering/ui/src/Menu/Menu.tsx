import { Hero } from "../Hero/Hero";
import { MenuItem } from "../MenuItem/MenuItem";
import styles from "./Menu.module.scss";

export function Menu() {
  return (
    <div className="container">
      <Hero title="Menu" subtitle="Click an item below to submit order" />
      <div className="d-flex justify-content-center">
        <div className={styles.menuItemSet}>
          <MenuItem />
          <MenuItem />
          <MenuItem />
        </div>
      </div>
    </div>
  );
}
