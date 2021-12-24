from datetime import datetime, timezone

from . import AbstractClock
from time import time
import pytz


class LocalClock(AbstractClock):

    def current_unix_time_sec(self) -> int:
        return int(time())

    def current_local_time(self) -> datetime:
        return datetime.now().astimezone(pytz.timezone("America/Chicago"))
