import time_convert

from pizza_ordering.infrastructure.clock import AbstractClock


class FastClock(AbstractClock):
    def current_unix_time_sec(self) -> int:
        return int(time_convert.time()) + 60
