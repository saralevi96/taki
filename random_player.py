import random
import taki
from base_player import BasePlayer
from enum_taki import Colors



class RandomPlayer(BasePlayer):
    def play_turn(self,taki):
        playable_cards = []
        # TODO: for in one line
        for card in self.hand:
            if taki.is_playable_card(card):
                playable_cards.append(card)
        if playable_cards:
            card_choice = random.choice(playable_cards)
            taki.play_card(self, card_choice)

        else:
            taki.draw_card(self)

    def get_color(self,taki):
        color_in_hand = set(card.color for card in self.hand)
        if color_in_hand:
            taki.last_card.color = random.choice(list(color_in_hand))
            print(f"{self.name} change color to {taki.last_card.color}")
        else:
            taki.last_card.color = random.choice(Colors)
