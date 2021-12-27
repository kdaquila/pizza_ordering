export class PizzaOrder {
  id: string;
  name: string;
  startTime: Date | null;
  stopTime: Date | null;
  status: string;
  constructor(
    id: string,
    name: string,
    startTime: Date | null,
    stopTime: Date | null,
    status: string
  ) {
    this.id = id;
    this.name = name;
    this.startTime = startTime;
    this.stopTime = stopTime;
    this.status = status;
  }
}
