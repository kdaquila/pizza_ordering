import { useContext, useEffect, useState } from "react";
import { AppContext } from "../../App";
import styles from "./FlashMessage.module.scss";

export function FlashMessage() {
  const appContext = useContext(AppContext);

  const [timerHandle, setTimerHandle] = useState<number>();

  useEffect(() => {
    if (appContext?.flashMessage !== "") {
      const handle = window.setTimeout(() => {
        appContext?.setFlashMessage("");
        appContext?.setFlashMessageStatus("");
      }, 3000);
      setTimerHandle(handle);
    }
    return () => {
      clearTimeout(timerHandle);
    };
  }, [appContext?.flashMessage]);

  let classes = styles.flashMessage
  if (appContext?.flashMessageStatus === "success") {
    classes += " " + styles['flashMessage--success']
  }
  else if (appContext?.flashMessageStatus === "fail" || appContext?.flashMessageStatus === "error") {
    classes += " " + styles['flashMessage--warning']
  }

  return <div className={classes}>{appContext?.flashMessage}</div>;
}
