from droplatch.modes.ronan import RonanMode
from readchar import key
from droplatch.modes.manual import ManualMode


class Keybinds:
    BINDS = {
        ("1"): lambda backend: ManualMode(0, backend),
        ("2"): lambda backend: ManualMode(1, backend),
        ("3"): lambda backend: ManualMode(2, backend),
        ("4"): lambda backend: ManualMode(3, backend),
        ("5"): lambda backend: ManualMode(4, backend),
        ("6"): lambda backend: ManualMode(5, backend),
        ("7"): lambda backend: ManualMode(6, backend),
        ("8"): lambda backend: ManualMode(7, backend),
        ("9"): lambda backend: RonanMode(backend),
    }

    def binding_exists(lis: list[str]) -> bool:
        for key in Keybinds.BINDS.keys():
            if lis == list(key):
                return True
        return False
