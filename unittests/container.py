from injector import Module, Binder, SingletonScope

from application.cancel_pizza import CancelPizzaUseCase
from application.clock import AbstractClock, LocalClock
from application.find_pizza import FindPizzaUseCase
from application.order_pizza import OrderPizzaUseCase
from application.pizza_factory import AbstractPizzaFactory, SamplePizzaFactory
from application.pizza_id_generator import AbstractPizzaIdGenerator, IntegerPizzaIdGenerator
from application.pizza_repo import AbstractPizzaRepo, InMemoryPizzaRepo


class Container(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(OrderPizzaUseCase, scope=SingletonScope)
        binder.bind(FindPizzaUseCase, scope=SingletonScope)
        binder.bind(CancelPizzaUseCase, scope=SingletonScope)
        binder.bind(AbstractPizzaRepo, to=InMemoryPizzaRepo, scope=SingletonScope)
        binder.bind(AbstractClock, to=LocalClock, scope=SingletonScope)
        binder.bind(AbstractPizzaIdGenerator, to=IntegerPizzaIdGenerator, scope=SingletonScope)
        binder.bind(AbstractPizzaFactory, to=SamplePizzaFactory, scope=SingletonScope)
