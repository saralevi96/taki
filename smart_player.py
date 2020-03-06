# ver
import random
from base_player import BasePlayer
from enum_taki import Colors
from enum_taki import CardType


class SmartPlayer(BasePlayer):
    def play_turn(self, taki):
        if self.try_play_plus_2(taki):
            return
        elif self.try_play_normal_card(taki):
            return
        elif self.try_play_plus(taki):
            return
        elif self.try_play_stop(taki):
            return
        elif self.try_play_changing_direction(taki):
            return
        elif self.try_play_color_changer(taki):
            return
        taki.draw_card(self)

    def get_color(self, taki):
        colors = [card.color for card in self.hand if card.color]
        if colors:
            taki.last_card.color = max(set(colors), key=colors.count)
            print(f"{self.name} changing card to {taki.last_card.color}")
        else:
            taki.last_card.color = random.choice(Colors)

    def try_play_normal_card(self, taki):
        for card in self.hand:
            if card.type_card == CardType.normal and taki.is_playable_card(card):
                taki.play_card(self, card)
                return True

        return False

    def try_play_changing_direction(self, taki):
        for card in self.hand:
            if card.type_card == CardType.changing_direction and taki.is_playable_card(card):
                taki.play_card(self, card)
                return True

        return False

    def try_play_color_changer(self, taki):
        for card in self.hand:
            if card.type_card == CardType.changes_color and taki.is_playable_card(card):
                taki.play_card(self, card)
                return True
        return False

    def try_play_stop(self, taki):
        for card in self.hand:
            if card.type_card == CardType.stop and taki.is_playable_card(card):
                taki.play_card(self, card)
                return True
        return False

    def try_play_plus_2(self, taki):
        for card in self.hand:
            if card.type_card == CardType.plus_2 and taki.is_playable_card(card):
                taki.play_card(self, card)
                return True
        return False

    def try_play_plus(self, taki):
        for card in self.hand:
            if card.type_card == CardType.plus and taki.is_playable_card(card):
                taki.play_card(self, card)
                return True
