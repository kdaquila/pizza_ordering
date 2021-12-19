import abc


class Clock(abc.ABC):
    @abc.abstractmethod
    def get_current_unixtime_sec(self) -> int:
        pass
