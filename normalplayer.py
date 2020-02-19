# ver
import random

from base_player import BasePlayer
from enum_taki import Colors


class normalPlayer(BasePlayer):
    def play_turn(self, taki):
        print(self.name)
        for card in self.hand:
            print(f"  enter {self.hand.index(card)} for {card}")
        print('if you do not have a card to download enter "take card"')
        user_input = input()
        is_valid_index = (user_input.isdigit() and 0 <= int(user_input) < len(self.hand))
        while not (user_input == "take card" or is_valid_index):
            user_input = input("the enter not good")
        if user_input == "take card":
            taki.draw_card(self)
        else:
            taki.try_play_card(self, self.hand[int(user_input)])

    def get_color(self, taki):
        color_in_hand = set(card.color for card in self.hand)
        if color_in_hand:
            taki.last_card.color = input(
                f"Color changes on the table, {self} changes color to ").lower()
        else:
            taki.last_card.color = random.choice(Colors)
