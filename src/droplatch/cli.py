from typing import Optional
from droplatch.keybinds import Keybinds
from droplatch.modes.base import BaseMode
import readchar
import time


class Cli:
    """
    The command line interface to Droplatch
    """

    INPUT_TIMEOUT: int = 3

    def __init__(self) -> None:
        """
        Initializes the command line interface
        """
        self.__input_queue: list[str] = []
        self.__last_keystroke: int = 0

    def start_interactive(self) -> None:
        """
        Starts a prompt where you can press keys to select different modes and start the game
        """
        key: str = ""
        while key != "q":
            key = readchar.readkey()
            time_now: int = int(time.time())

            if time_now - self.__last_keystroke >= Cli.INPUT_TIMEOUT:
                self.__input_queue = []
                self.__last_keystroke = time_now

            if self.is_binding(key):
                tup: tuple = tuple(self.__input_queue)
                if len(tup) == 1:
                    mode: BaseMode = Keybinds.BINDS[tup[0]]()
                else:
                    mode: BaseMode = Keybinds.BINDS[tup]()
                mode.run()
                self.__input_queue = []

    def is_binding(self, key: str) -> bool:
        """
        Adds a key to the input queue. If a command is equivalent to the queue, return true
        """
        self.__input_queue.append(key)
        return Keybinds.binding_exists(self.__input_queue)
