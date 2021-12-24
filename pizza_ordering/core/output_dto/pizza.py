class Pizza:
    def __init__(self, pizza_id: str, name: str, description: str, start_time: int = None,
                 stop_time: int = None) -> None:
        self.pizza_id: str = pizza_id
        self.name: str = name
        self.description: str = description
        self.start_time: int = start_time
        self.stop_time: int = stop_time

