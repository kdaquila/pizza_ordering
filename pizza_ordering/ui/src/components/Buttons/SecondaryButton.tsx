import styles from "./SecondaryButton.module.scss";

export function SecondaryButton(props: {title:string, disabled: boolean, onClick: any, fluid: boolean }) {
  let classes = styles.button;
  if (props.disabled) {
    classes = classes + " " + styles["button--disabled"];
  }
  if (props.fluid) {
    classes += " " + styles["button--fluid"];
  }
  return (
    <button
      className={classes}
      type="button"
      disabled={props.disabled}
      onClick={props.onClick}
    >
      {props.title}
    </button>
  );
}
