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

    #players = []
    # amount_players = int(input("some players ,the max is 4"))
    # for player in range(amount_players):
    #
    #Type_player = input("what type of the player 1.random player "
     #                 "2. smart player"
      #                "3. normal player")

   # players.append(Type_player(input("what your name"), input("what your age"), hand=[]))

    return players
