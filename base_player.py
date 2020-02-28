from abc import abstractmethod

from enum_taki import PlayerType
import taki


class BasePlayer:
    def __init__(self, name, age, hand=None):
        if not hand:
            hand = []

        self.name = name
        self.age = age
        self.hand = hand

    def __str__(self):
        return f"{self.name} with {len(self.hand)} cards"

    def print_status(self):
        print(f"{self.name} {[str(CARD) for CARD in self.hand]}")

    @abstractmethod
    def play_turn(self, taki):
        pass

    def get_color(self, taki):
        pass


#     TODO add color function
