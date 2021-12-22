import time

from infrastructure.clock import AbstractClock


class FastClock(AbstractClock):
    def current_unix_time_sec(self) -> int:
        return int(time.time()) + 60
