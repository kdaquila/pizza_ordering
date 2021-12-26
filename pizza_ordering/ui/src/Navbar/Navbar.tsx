import styles from "./Navbar.module.scss";

export function Navbar() {
  return (
    <div className={styles.background + " py-2"}>
      <div className="container d-flex justify-content-between">
        <div>
          <a className={styles.logo__link} href="/menu"><h1 className={styles.logo}>Pizza Management</h1></a> 
        </div>
        <ul className="d-flex">
          <li className={styles.nav__item}>
            <a className={styles.nav__link} href="/menu">Menu</a>
          </li>
          <li className={styles.nav__item}>
            <a className={styles.nav__link} href="/order">Order</a>
          </li>
        </ul>
      </div>
    </div>
  );
}
