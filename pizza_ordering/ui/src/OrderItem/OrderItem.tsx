import { PrimaryButton } from "../Buttons/PrimaryButton";
import { SecondaryButton } from "../Buttons/SecondaryButton";
import styles from "./OrderItem.module.scss"

export function OrderItem() {
  return (
    <div className={styles.orderItem}>
      <h1 className={styles.title} >Cheese Pizza</h1>
      <div className="mb-3">
        <h2 className={styles.sectionName}>Order Id</h2>
        <p className={styles.sectionValue}>e01b4d97-aa17-40b9-b9c6-81e8e31a396e</p>
      </div>
      <div className="mb-3">
        <h2 className={styles.sectionName}>Started</h2>
        <p className={styles.sectionValue}>2021-12-25 04:16</p>
      </div>
      <div className="mb-3">
        <h2 className={styles.sectionName}>Stopped</h2>
        <p className={styles.sectionValue}>n/a</p>
      </div>
      <div className="mb-3">
        <h2 className={styles.sectionName}>Status</h2>
        <p className={styles.sectionValue}>cooking</p>
      </div>
      <PrimaryButton disabled={false}/>
      <SecondaryButton disabled={false}/>
    </div>
  );
}
