import styles from "./PrimaryButton.module.scss";

export function PrimaryButton(props: { disabled: boolean }) {
  let classes = styles.button;
  if (props.disabled) {
    classes = classes + " " + styles["button--disabled"];
  }
  return (
    <button className={classes} type="button" disabled={props.disabled}>
      Finish
    </button>
  );
}
