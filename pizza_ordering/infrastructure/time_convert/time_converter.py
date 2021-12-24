from datetime import datetime

import pytz
import time

from .abstract_time_converter import AbstractTimeConverter


class TimeConverter(AbstractTimeConverter):
    def __init__(self):
        self.tz = pytz.timezone("America/Chicago")

    def get_timestamp_from_datetime(self, date: datetime):
        return int(time.mktime(date.timetuple()))

    def get_time_from_timestamp(self, timestamp):
        return datetime.fromtimestamp(timestamp, self.tz)
