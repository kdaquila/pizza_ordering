import abc
from uuid import UUID


class AbstractIdFactory(abc.ABC):
    @abc.abstractmethod
    def create_new_id(self) -> UUID:
        pass
