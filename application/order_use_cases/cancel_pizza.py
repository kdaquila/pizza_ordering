from application.clock.clock import Clock
from application.order_repo.pizza_order_repo import PizzaOrderRepo
from domain.exceptions import CannotCancelOrder
import config


class CancelPizza:
    def __init__(self, pizza_repo: PizzaOrderRepo, clock: Clock):
        self.clock = clock
        self.pizza_repo = pizza_repo

    def execute(self, order_id):
        current_time = self.clock.current_unix_time_sec()
        pizza_order = self.pizza_repo.get(order_id)
        start_time = pizza_order.start_time
        elapsed_time = current_time - start_time
        if elapsed_time < config.cancel_order_interval_sec:
            pizza_order.stop_cooking_at(current_time)
            self.pizza_repo.save(pizza_order)
        else:
            raise CannotCancelOrder()
