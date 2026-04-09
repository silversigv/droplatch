from droplatch.backends.base import BaseBackend
import RPi.GPIO as GPIO


class RPIGPIOBackend(BaseBackend):
    """
    A backend that drops breadstick
    """

    PINS = [21, 23, 29, 31, 33, 35, 37, 11]

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        for pin in RPIGPIOBackend.PINS:
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.HIGH)

    def toggle(self, id: int, retract: bool = False):
        GPIO.output(RPIGPIOBackend.PINS[id], not retract)
