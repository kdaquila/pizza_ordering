import abc


class AbstractClock(abc.ABC):
    @abc.abstractmethod
    def current_unix_time_sec(self) -> int:
        pass
