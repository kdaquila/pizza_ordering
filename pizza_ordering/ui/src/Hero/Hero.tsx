import styles from "./Hero.module.scss";

export function Hero(props: {title: string, subtitle: string}) {
  return (
    <div className="container my-5">
      <div className="d-flex justify-content-center">
        <h1 className={styles.title}>{props.title}</h1>
      </div>
      <h2 className={styles.subtitle}>{props.subtitle}</h2>
    </div>
  );
}
