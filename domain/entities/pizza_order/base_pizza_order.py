import time


class BasePizzaOrder:
    def __init__(self, order_id, name, description) -> None:
        self.order_id = order_id
        self.name = name
        self.description = description
        self.start_time = None
        self.stop_time = None

    def start_cooking_at(self, start_time) -> None:
        self.start_time = start_time

    def stop_cooking_at(self, stop_time) -> None:
        self.stop_time = stop_time

    @property
    def is_cooking(self) -> bool:
        return (self.start_time is not None) and (self.stop_time is None)

    def __str__(self) -> str:
        return self.name


if __name__ == "__main__":
    x = BasePizzaOrder(1, "name", "description")
    print(x)
