import styles from "./PrimaryButton.module.scss";

export function PrimaryButton(props: {title: string, disabled: boolean; onClick: any, fluid: boolean }) {
  let classes = styles.button;

  if (props.disabled) {
    classes += " " + styles["button--disabled"];
  }
  else if (props.fluid) {
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
