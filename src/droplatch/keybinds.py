from readchar import key
from droplatch.modes.manual import ManualMode

class Keybinds:
    BINDS = {
        ("0"): lambda: ManualMode(0),
        ("1"): lambda: ManualMode(1),
        ("2"): lambda: ManualMode(2),
        ("3"): lambda: ManualMode(3),
        ("4"): lambda: ManualMode(4),
        ("5"): lambda: ManualMode(5),
        ("6"): lambda: ManualMode(6),
        ("7"): lambda: ManualMode(7),
        ("8"): lambda: ManualMode(8),
    }

    def binding_exists(lis: list[str]) -> bool:
        for key in Keybinds.BINDS.keys():
            if lis == list(key):
                return True
        return False
