from abc import abstractmethod

class BaseBackend:
    """
    Extend in order to create a new backend.
    """

    @abstractmethod
    def __init__(self):
        """
        Initializes a backend.
        """
        pass

    @abstractmethod
    def toggle(self, id: int, retract: bool = False):
        """
        Toggles at the specific id.
        Set retract to true in order to close.
        """
        pass
