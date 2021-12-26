import styles from "./Hero.module.scss";

export function Hero() {
  return (
    <div className="container my-5">
      <div className="d-flex justify-content-center">
        <h1 className={styles.title}>Menu</h1>
      </div>
      <h2 className={styles.subtitle}>Click an item below to submit order</h2>
    </div>
  );
}
