from datetime import datetime

class Pizza:
    def __init__(self, pizza_id: str, name: str, description: str, start_time: datetime = None,
                 stop_time: datetime = None) -> None:
        self.pizza_id: str = pizza_id
        self.name: str = name
        self.description: str = description
        self.start_time: datetime = start_time
        self.stop_time: datetime = stop_time

