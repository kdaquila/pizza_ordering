import styles from "./SecondaryButton.module.scss";

export function SecondaryButton(props: { disabled: boolean }) {
  let classes = styles.button;
  if (props.disabled) {
    classes = classes + " " + styles["button--disabled"];
  }
  return (
    <button
      className={classes}
      type="button"
      disabled={props.disabled}
    >
      Cancel
    </button>
  );
}
