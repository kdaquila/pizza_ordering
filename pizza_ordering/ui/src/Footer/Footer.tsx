import style from "./Footer.module.scss";

export function Footer() {
  return (
    <ul className="container">
      <div className={style.footer}>
        <li className={style["footerItem--divider"]}>
          Copyright 2021 Pizza Ordering LLC
        </li>
        <li className={style["footerItem--divider"]}>
          <a className={style.footerItem__link} href="/terms">
            Terms of Use
          </a>
        </li>
        <li className={style["footerItem--divider"]}>
          <a className={style.footerItem__link} href="/privacy">
            Privacy Policy
          </a>
        </li>
        <li className={style["footerItem"]}>
          <a className={style.footerItem__link} href="/support">
            Support
          </a>
        </li>
      </div>
    </ul>
  );
}
