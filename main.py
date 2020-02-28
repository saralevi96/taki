from players import init_players
from taki import Taki



players = init_players()
taki = Taki(players)
taki.print_status()
player_winner = taki.start_game()
