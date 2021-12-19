from application.clock.clock import Clock
import time


class LocalClock(Clock):
    def __init__(self, time_shift_sec: int = 0):
        self.time_shift_sec = time_shift_sec

    def current_unix_time_sec(self) -> int:
        return int(time.time()) + self.time_shift_sec
