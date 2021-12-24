import time
from datetime import datetime, timedelta

import pytz

from pizza_ordering.infrastructure.clock import AbstractClock


class FastClock(AbstractClock):
    def current_local_time(self) -> datetime:
        return datetime.now().astimezone(pytz.timezone("America/Chicago")) + timedelta(seconds=60)

    def current_unix_time_sec(self) -> int:
        return int(time.time()) + 60
