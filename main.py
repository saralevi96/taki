<<<<<<< HEAD
from players import init_players
from taki import Taki



players = init_players()
taki = Taki(players)
taki.print_status()
player_winner = taki.start_game()
=======
# main file
def main():
	from base_player import init_players
	from taki import Taki

	aviv = 0
	sara = 0
	players = init_players()
	taki = Taki(players)
	taki.print_status()
	player_winner = taki.start_game()

	
if __name__ == "__main__":
	main()
>>>>>>> eccb585d685840919c9e69bdf167466829263a9c
