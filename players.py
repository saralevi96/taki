from enum_taki import PlayerType
from random_player import RandomPlayer
from smart_player import SmartPlayer
from normalplayer import normalPlayer


def init_players():
    players = [
        RandomPlayer("Aviv", 18),
        SmartPlayer("Sara", 22),
        normalPlayer("moshe", 28)
    ]

    return players
