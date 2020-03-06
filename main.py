from players import init_players
from taki import Taki


# main file
def main():
    players = init_players()
    taki = Taki(players)
    taki.print_status()
    player_winner = taki.start_game()


if __name__ == "__main__":
    main()
