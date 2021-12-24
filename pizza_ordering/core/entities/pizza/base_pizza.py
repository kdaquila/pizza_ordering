from uuid import UUID


class BasePizza:
    def __init__(self, pizza_id: UUID, name: str, description: str, start_time: int = None,
                 stop_time: int = None) -> None:
        self.pizza_id: UUID = pizza_id
        self.name: str = name
        self.description: str = description
        self.start_time: int = start_time
        self.stop_time: int = stop_time

    def start_cooking_at(self, start_time) -> None:
        self.start_time = start_time

    def stop_cooking_at(self, stop_time) -> None:
        self.stop_time = stop_time

    @property
    def is_cooking(self) -> bool:
        return (self.start_time is not None) and (self.stop_time is None)
