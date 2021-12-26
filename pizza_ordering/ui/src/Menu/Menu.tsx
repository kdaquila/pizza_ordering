import { MenuItem } from "../MenuItem/MenuItem";
import styles from "./Menu.module.scss";

export function Menu() {
  return (
    <div className="container d-flex justify-content-center">
      <div className={styles.menuItemSet} >
        <MenuItem />
        <MenuItem />
        <MenuItem />
      </div>
    </div>
  );
}
