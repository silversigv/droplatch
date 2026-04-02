from droplatch.backends.base import BaseBackend

class MockBackend(BaseBackend):
    """
    A fake backend that prints to the console
    """

    def __init__(self):
        pass

    def toggle(self, id: int, retract: bool = False):
        if not retract:
            print(f"{id} was opened")
        else:
            print(f"{id} was closed")
