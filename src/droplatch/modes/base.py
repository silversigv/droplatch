from abc import abstractmethod
from time import sleep
from droplatch.backends.mock import MockBackend

class InvalidIDError(ValueError):
    pass

class BaseMode:
    """
    Extend to implement a custom dropping mode.
    """

    def __init__(self, backend = MockBackend()):
        """
        Initializes the mode.
        """
        self.__backend = backend

    @abstractmethod
    def run(self):
        """
        A function that gets ran when the game starts
        """
        pass

    def release(self, id: int):
        """
        Opens and closes the latch at the specific id.
        """
        if id not in range(0, 9):
            raise InvalidIDError("Release ID should be from 0-8 inclusive")
        self.__backend.toggle(id)
        sleep(1)
        self.__backend.toggle(id, retract=True)

