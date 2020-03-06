# ver
import random
from base_player import BasePlayer
from enum_taki import Colors
from enum_taki import CardType


class RandomPlayer(BasePlayer):
    def random_play_plus_2(self, taki, playable_cards):
        for card in playable_cards:
            if card.type_card == CardType.plus_2:
                the_choice = random.randint(0, 1)
                if the_choice:
                    taki.play_card(self, card)
                    return True
        return False

    def play_turn(self, taki):
        playable_cards = [card for card in self.hand if taki.is_playable_card(card)]
        if taki.count_plus_2:
            if self.random_play_plus_2(taki, playable_cards):
                return

        elif playable_cards:
            card_choice = random.choice(playable_cards)
            taki.play_card(self, card_choice)
            return

        taki.draw_card(self)

    def get_color(self, taki):
        color_in_hand = set(card.color for card in self.hand)
        if color_in_hand:
            taki.last_card.color = random.choice(list(color_in_hand))
            print(f"{self.name} change color to {taki.last_card.color}")
        else:
            taki.last_card.color = random.choice(Colors)
