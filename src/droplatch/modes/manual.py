from droplatch.backends.mock import MockBackend
from droplatch.modes.base import BaseMode


class ManualMode(BaseMode):
    """
    A mode that allows you to manually drop at a specific id.
    """

    def __init__(self, id: int, backend=MockBackend()):
        self.__id = id
        super().__init__(backend)

    def run(self):
        self.release(self.__id)
