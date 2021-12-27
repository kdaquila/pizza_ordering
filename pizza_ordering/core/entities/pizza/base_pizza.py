from uuid import UUID
from datetime import datetime


class BasePizza:
    def __init__(self, pizza_id: UUID, name: str, description: str, start_time: datetime = None,
                 stop_time: datetime = None, status: str = "waiting") -> None:
        self.pizza_id: UUID = pizza_id
        self.name: str = name
        self.description: str = description
        self.start_time: datetime = start_time
        self.stop_time: datetime = stop_time
        self.status: str = status

    def start_cooking_at(self, start_time) -> None:
        self.start_time = start_time
        self.status = "cooking"

    def finish_cooking_at(self, stop_time) -> None:
        self.stop_time = stop_time
        self.status = "finished"

    def cancel_cooking_at(self, stop_time) -> None:
        self.stop_time = stop_time
        self.status = "cancelled"

    @property
    def is_cooking(self) -> bool:
        return (self.start_time is not None) and (self.stop_time is None)
