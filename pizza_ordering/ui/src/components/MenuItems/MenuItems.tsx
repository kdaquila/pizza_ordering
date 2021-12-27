import { MenuItem } from "../MenuItem/MenuItem";
import styles from "./MenuItems.module.scss";

type Pizza = {
  id: string,
  name: string,
  description: string
}

export function MenuItems(props: {"items": Pizza[]}) {
  return (
    <div className="d-flex justify-content-center">
      <div className={styles.menuItemSet}>
        {props.items.map(item => {
          return <MenuItem key={item.id} name={item.name} description={item.description} />
        })}
        
      </div>
    </div>
  );
}
