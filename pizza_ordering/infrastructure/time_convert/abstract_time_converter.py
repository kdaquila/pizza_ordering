import abc


class AbstractTimeConverter(abc.ABC):
    @abc.abstractmethod
    def get_time_from_timestamp(self, timestamp):
        pass

    @abc.abstractmethod
    def get_timestamp_from_datetime(self, date):
        pass
