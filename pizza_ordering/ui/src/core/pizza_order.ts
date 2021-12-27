export class PizzaOrder {
  id: string;
  name: string;
  startTime: string;
  stopTime: string;
  status: string;
  constructor(
    id: string,
    name: string,
    startTime: string,
    stopTime: string,
    status: string
  ) {
    this.id = id;
    this.name = name;
    this.startTime = startTime;
    if (startTime === null) {
      this.startTime = "n/a";
    }
    this.stopTime = stopTime;
    if (stopTime === null) {
        this.stopTime = "n/a";
      }
    this.status = status;
  }
}
