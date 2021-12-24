import abc
from datetime import datetime


class AbstractClock(abc.ABC):
    @abc.abstractmethod
    def current_unix_time_sec(self) -> int:
        pass

    @abc.abstractmethod
    def current_local_time(self) -> datetime:
        pass
