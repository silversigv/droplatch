import random


class MOTD:
    MESSAGES: list[str] = [
        "Josh is a goober",
        "THE VOICES",
        "uhh i forgot the other thing that i was supposed to add; andrew if you see this remind me",
    ]

    @staticmethod
    def random_motd() -> str:
        return random.choice(MOTD.MESSAGES)
