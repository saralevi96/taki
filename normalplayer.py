# ver
import random
import taki
from base_player import BasePlayer
from enum_taki import Colors


class normalPlayer(BasePlayer):
    def play_turn(self, taki):
        print(self.name)
        for card in self.hand:
            print(f"  enter {self.hand.index(card)} for {card}")
        is_valid_index = False
        user_input = None
        if taki.count_plus_2:input(f'''you need put +2 or enter "take card" take all card in +2''')
        while not (user_input == "take card" or is_valid_index):
            user_input = input('if you do not have a card to download enter "take card"')
            is_valid_index = (user_input.isdigit() and 0 <= int(user_input) < len(self.hand))
        if user_input == "take card":
            taki.draw_card(self)
        else:
            taki.try_play_card(self, self.hand[int(user_input)])

    def get_color(self, taki):
        taki.last_card.color = input(
            f"Color changes on the table, {self} changes color to ").lower()
