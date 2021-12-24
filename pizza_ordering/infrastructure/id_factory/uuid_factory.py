from uuid import uuid4, UUID

from pizza_ordering.infrastructure.id_factory import AbstractIdFactory


class UUIDFactory(AbstractIdFactory):
    def create_new_id(self) -> UUID:
        return uuid4()
