from . import AbstractClock
from time import time


class LocalClock(AbstractClock):

    def current_unix_time_sec(self) -> int:
        return int(time())
