from uuid import UUID

from pizza_ordering.infrastructure.id_factory import AbstractIdFactory


class IntegerIdFactory(AbstractIdFactory):
    def __init__(self):
        super().__init__()
        self.current_id = 0

    def create_new_id(self) -> UUID:
        self.current_id += 1
        return self.current_id
