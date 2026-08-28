import random
import time
from droplatch.backends.mock import MockBackend
from droplatch.modes.base import BaseMode


class DropAllMode(BaseMode):
    """
    A mode that is based on the original code from 2024.
    """

    def run(self):
        for i in range(8):
            self.toggle(i)
        time.sleep(1)
        for i in range(8):
            self.toggle(i, retract=True)
