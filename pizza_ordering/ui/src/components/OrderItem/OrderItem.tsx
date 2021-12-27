import { cancel_order } from "../../core/cancel_order";
import { finish_order } from "../../core/finish_order";
import { PrimaryButton } from "../Buttons/PrimaryButton";
import { SecondaryButton } from "../Buttons/SecondaryButton";
import styles from "./OrderItem.module.scss";

export function OrderItem(props: {
  id: string;
  name: string;
  status: string;
  startTime: string;
  stopTime: string;
  pizzaEndpoint: string;
  onUpdateOrders: any;
}) {
  async function primaryButtonClickHandler() {
    await finish_order(props.pizzaEndpoint, props.id).then((response) => {});
    props.onUpdateOrders();
  }

  async function secondaryButtonClickHandler() {
    await cancel_order(props.pizzaEndpoint, props.id).then((response) => {});
    props.onUpdateOrders();
  }

  const isCancellable = props.status === "cooking";
  const isFinishable = props.status === "cooking";

  return (
    <div className={styles.orderItem}>
      <h1 className={styles.title}>{props.name}</h1>
      <div className="mb-3">
        <h2 className={styles.sectionName}>Order Id</h2>
        <p className={styles.sectionValue}>{props.id}</p>
      </div>
      <div className="mb-3">
        <h2 className={styles.sectionName}>Started</h2>
        <p className={styles.sectionValue}>{props.startTime}</p>
      </div>
      <div className="mb-3">
        <h2 className={styles.sectionName}>Stopped</h2>
        <p className={styles.sectionValue}>{props.stopTime}</p>
      </div>
      <div className="mb-4">
        <h2 className={styles.sectionName}>Status</h2>
        <p className={styles.sectionValue}>{props.status}</p>
      </div>
      <PrimaryButton
        disabled={!isFinishable}
        onClick={primaryButtonClickHandler}
      />
      <SecondaryButton
        disabled={!isCancellable}
        onClick={secondaryButtonClickHandler}
      />
    </div>
  );
}
