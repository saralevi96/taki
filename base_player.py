# ver
from abc import abstractmethod

from enum_taki import PlayerType



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
    def get_color(self,taki):
        pass

#     TODO add color function


# TODO  להעביר לקובץ
def init_players():
    from random_player import RandomPlayer
    from smart_player import SmartPlayer
    from normalplayer import normalPlayer
    players = [
        # Player("Aviv", 18,PlayerType.smart_computer),
        RandomPlayer("Aviv", 18),
        SmartPlayer("Sara", 22),
        normalPlayer("moshe", 28)

    ]
    # players = []
    # amount_players = int(input("some players"))
    # for player in range(amount_players):
    #     players.append(Player(input("what your name"), input("what your age"), hand=[]))

    return players
