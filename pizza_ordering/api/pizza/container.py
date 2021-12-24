from injector import Module, Binder, Injector, SingletonScope

from pizza_ordering.core.use_cases.cancel_pizza import CancelPizzaUseCase
from pizza_ordering.core.use_cases.find_pizza import FindPizzaUseCase
from pizza_ordering.core.use_cases.order_pizza import OrderPizzaUseCase
from pizza_ordering.core.pizza_repo import AbstractPizzaRepo, InMemoryPizzaRepo
from pizza_ordering.core.pizza_factory import AbstractPizzaFactory, SamplePizzaFactory
from pizza_ordering.infrastructure.clock import AbstractClock, LocalClock
from pizza_ordering.infrastructure.id_factory import AbstractIdFactory, IntegerIdFactory, UUIDFactory
from pizza_ordering.infrastructure.pizza_repo.django_orm_pizza_repo import DjangoORMPizzaRepo


class Container(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(OrderPizzaUseCase, scope=SingletonScope)
        binder.bind(FindPizzaUseCase, scope=SingletonScope)
        binder.bind(CancelPizzaUseCase, scope=SingletonScope)
        binder.bind(AbstractPizzaRepo, to=DjangoORMPizzaRepo, scope=SingletonScope)
        binder.bind(AbstractClock, to=LocalClock, scope=SingletonScope)
        binder.bind(AbstractIdFactory, to=UUIDFactory, scope=SingletonScope)
        binder.bind(AbstractPizzaFactory, to=SamplePizzaFactory, scope=SingletonScope)


container = Injector([Container])

cancel_pizza_use_case = container.get(CancelPizzaUseCase)
find_pizza_use_case = container.get(FindPizzaUseCase)
order_pizza_use_case = container.get(OrderPizzaUseCase)
