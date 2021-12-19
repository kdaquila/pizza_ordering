from application.order_id.order_id_maker import OrderIdMaker
from domain.value_objects import OrderId


class IntegerOrderIdMaker(OrderIdMaker):
    def __init__(self):
        super().__init__()
        self.current_id = 0

    def create_new_id(self) -> OrderId:
        self.current_id += 1
        return self.current_id
