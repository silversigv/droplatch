import random
import time
from droplatch.backends.mock import MockBackend
from droplatch.modes.base import BaseMode


class RonanMode(BaseMode):
    """
    A mode that is based on the original code from 2024.
    """

    def __init__(self, backend=MockBackend(), difficulty: float = 1):
        self.__difficulty = difficulty
        super().__init__(backend)

    def run(self):
        pins = list(range(8))
        while len(pins) > 0:
            time.sleep((random.randint(5, 15) / 10.0) * self.__difficulty)
            randnum = random.randint(0, len(pins) - 1)
            self.release(pins[randnum])
            del pins[randnum]
