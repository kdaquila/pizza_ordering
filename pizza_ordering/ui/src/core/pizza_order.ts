export class PizzaOrder {
    id: string;
    name: string;
    startTime: string;
    stopTime: string;
    status: string;
    constructor(id: string, name: string, startTime: string, stopTime: string, status: string) {
        this.id = id
        this.name = name
        this.startTime = startTime 
        this.stopTime = stopTime
        this.status = status
    }
}