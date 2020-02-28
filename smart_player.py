# ver
import random
<<<<<<< HEAD
import taki
=======


>>>>>>> eccb585d685840919c9e69bdf167466829263a9c
from base_player import BasePlayer
from enum_taki import Colors


class SmartPlayer(BasePlayer):
    def play_turn(self, taki):

        if taki.try_play_normal_card(self):
            return
        elif taki.try_play_stop(self):
            return
        elif taki.try_play_changing_direction(self):
            return
        elif taki.try_play_color_changer(self):
            return
        taki.draw_card(self)

    def get_color(self, taki):
        colors = [card.color for card in self.hand if card.color]
        if colors:
            taki.last_card.color = max(set(colors), key=colors.count)
            print(f"{self.name} changing card to {taki.last_card.color }")
        else:
            taki.last_card.color = random.choice(Colors)
