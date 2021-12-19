from application.clock.clock import Clock
import time


class LocalClock(Clock):
    def get_current_unixtime_sec(self) -> int:
        return int(time.time())
