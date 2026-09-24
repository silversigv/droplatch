import random
import time
from droplatch.backends.mock import MockBackend
from droplatch.modes.base import BaseMode


class AndrewMode(BaseMode):
    """
    Drops randomly, regardless of what is currently down. 
    """

    def __init__(self, backend=MockBackend()):
        super().__init__(backend)

    def run(self):
        pins = []
        while len(pins) <= 8:
            time.sleep((random.randint(5, 15) / 10.0))
            randnum = random.randint(0, 8)
            self.release(randnum)
            if randnum not in pins:
                pins.append(randnum)

