from droplatch.modes.dropall import DropAllMode
from droplatch.modes.ronan import RonanMode
from readchar import key
from droplatch.modes.manual import ManualMode


class Keybinds:
    BINDS = {
        ("0", "1"): lambda backend: ManualMode(0, backend),
        ("0", "2"): lambda backend: ManualMode(1, backend),
        ("0", "3"): lambda backend: ManualMode(2, backend),
        ("0", "4"): lambda backend: ManualMode(3, backend),
        ("0", "5"): lambda backend: ManualMode(4, backend),
        ("0", "6"): lambda backend: ManualMode(5, backend),
        ("0", "7"): lambda backend: ManualMode(6, backend),
        ("0", "8"): lambda backend: ManualMode(7, backend),
        ("6", "7"): lambda backend: DropAllMode(backend),
        ("1"): lambda backend: RonanMode(backend),
        ("2"): lambda backend: RonanMode(backend, 0.85),
        ("3"): lambda backend: RonanMode(backend, 0.25),

    }

    def binding_exists(lis: list[str]) -> bool:
        for key in Keybinds.BINDS.keys():
            if lis == list(key):
                return True
        return False
