# ver
import random

from enum_taki import CardType, Colors


class Card:
    def __init__(self, color, num, type_card):
        self.color = color
        self.num = num
        self.type_card = type_card

    def __str__(self):
        if self.type_card == CardType.normal:
            return f"{self.num} {self.color}"
        elif self.type_card == CardType.changes_color:
            return self.type_card if not self.color else f"{self.type_card} to {self.color}"
        else:
            return f"{self.type_card} {self.color}"


def create_taki_deck():
    numbers = list(range(1, 11))
    colors = [Colors.blue, Colors.red, Colors.green, Colors.yellow]
    cards = []
    for color in colors:
        for num in numbers:
            cards.append(Card(color, num, CardType.normal))

    cards += [Card(color=None, num=None, type_card=CardType.changes_color) for i in range(4)]
    for i in range(2):
        cards += [Card(color=color, num=None, type_card=CardType.stop) for color in colors]
        cards += [Card(color=color, num=None, type_card=CardType.changing_direction) for color in colors]
        cards += [Card(color=color, num=None, type_card=CardType.plus) for color in colors]
        cards += [Card(color=color, num=None, type_card=CardType.plus_2) for color in colors]
    random.shuffle(cards)
    return cards


def most_frequent_color(cards):
    colors = [card.color for card in cards if card.color]
    if colors:
        return max(set(colors), key=colors.count)
    else:
        return Colors.red
