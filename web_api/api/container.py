from injector import Module, Binder, Injector, SingletonScope

from core.use_cases.cancel_pizza import CancelPizzaUseCase
from infrastructure.clock import AbstractClock, LocalClock
from core.use_cases.find_pizza import FindPizzaUseCase
from core.use_cases.order_pizza import OrderPizzaUseCase
from core.pizza_factory import AbstractPizzaFactory, SamplePizzaFactory
from infrastructure.id_factory import AbstractIdFactory, IntegerIdFactory
from core.pizza_repo import AbstractPizzaRepo, InMemoryPizzaRepo


class Container(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(OrderPizzaUseCase, scope=SingletonScope)
        binder.bind(FindPizzaUseCase, scope=SingletonScope)
        binder.bind(CancelPizzaUseCase, scope=SingletonScope)
        binder.bind(AbstractPizzaRepo, to=InMemoryPizzaRepo, scope=SingletonScope)
        binder.bind(AbstractClock, to=LocalClock, scope=SingletonScope)
        binder.bind(AbstractIdFactory, to=IntegerIdFactory, scope=SingletonScope)
        binder.bind(AbstractPizzaFactory, to=SamplePizzaFactory, scope=SingletonScope)


container = Injector([Container])

cancel_pizza_use_case = container.get(CancelPizzaUseCase)
find_pizza_use_case = container.get(FindPizzaUseCase)
order_pizza_use_case = container.get(OrderPizzaUseCase)
