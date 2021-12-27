import styles from "./PrimaryButton.module.scss";

export function PrimaryButton(props: { disabled: boolean; onClick: any }) {
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
      Finish
    </button>
  );
}
