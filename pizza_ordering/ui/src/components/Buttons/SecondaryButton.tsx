import styles from "./SecondaryButton.module.scss";

export function SecondaryButton(props: { disabled: boolean, onClick: any }) {
  let classes = styles.button;
  if (props.disabled) {
    classes = classes + " " + styles["button--disabled"];
  }
  return (
    <button
      className={classes}
      type="button"
      disabled={props.disabled}
      onClick={props.onClick}
    >
      Cancel
    </button>
  );
}
