import random

from card import create_taki_deck, most_frequent_color
from enum_taki import CardType


class Taki:
    def __init__(self, players):
        self.players = players
        self.players.sort(key=lambda x: x.age)

        self.cards = create_taki_deck()
        self.table = self.init_table()
        self.distribute_cards()
        # self.should_activate_stop = False
        self.should_activate_changing_direction = False

    @property
    def last_card(self):
        return self.table[-1]

    @property
    def amount_of_cards(self):
        return len(self.cards)

    def __str__(self):
        return f"the play taki start with {len(self.players)} players  and {self.amount_of_cards}"

    def print_status(self):
        [player.print_status() for player in self.players]

    # Init functions
    def distribute_cards(self):
        for i in range(3):
            for player in self.players:
                player.hand.append(self.cards.pop())

    def init_table(self):
        table = [self.cards.pop()]
        print(f"Game start with {self.amount_of_cards} cards  and  {table[-1]} on the table ")
        return table

    # Play game functions
    def is_game_over(self, player):
        if not player.hand:
            return True
        if not self.cards:
            return True
        return False

    def discard_card(self, player, card):
        self.table.append(card)
        player.hand.remove(card)
        print(f"{player.name} discard {card} (player left with {len(player.hand)} cards)")

    def draw_card(self, player):
        drawn_card = self.cards.pop()
        player.hand.append(drawn_card)
        print(f"{player.name} draw {drawn_card} from the deck ({self.amount_of_cards} cards left on deck)")

    def try_play_normal_card(self, player):
        for card in player.hand:
            if card.type_card == CardType.normal and self.is_playable_card(card):
                self.play_card(player, card)
                return True

        return False

    def try_play_changing_direction(self, player):
        for card in player.hand:
            if card.type_card == CardType.changing_direction and self.is_playable_card(card):
                self.play_card(player, card)
                return True

        return False

    def try_play_color_changer(self, player):
        for card in player.hand:
            if card.type_card == CardType.changes_color and self.is_playable_card(card):
                self.play_card(player, card)
                return True

        return False

    def try_play_stop(self, player):
        for card in player.hand:
            if card.type_card == CardType.stop and self.is_playable_card(card):
                self.play_card(player, card)
                return True

        return False

    def play_first_card(self):
        first_card = self.table[0]
        player = self.players[0]
        if first_card.type_card == CardType.stop:
            self.players.append(player)
            self.players.remove(player)
            print(f"{player} got stop")
        elif first_card.type_card == CardType.changing_direction:
            self.players.reverse()
            print(f"{player} got change direction")
        elif first_card.type_card == CardType.changes_color and not first_card.color:
            player.get_color(self)

    def is_playable_card(self, card):
        same_num = (card.num == self.last_card.num and card.num)
        same_color = (card.color == self.last_card.color)#and card.color
        same_type = (card.type_card == self.last_card.type_card and card.type_card != CardType.normal)
        is_changes_color = (card.type_card == CardType.changes_color)
        # change color is none
        if same_color or same_num or same_type or is_changes_color:
            return True
        return False

    def play_card(self, player, card):
        self.discard_card(player, card)
        if card.type_card == CardType.stop:
            # duplicate code
            self.players.remove(player)
            self.players.append(player)
            print(f"{self.players[0]} got a stop")
        elif card.type_card == CardType.changing_direction:
            self.should_activate_changing_direction = True
        elif card.type_card == CardType.changes_color:
            player.get_color(self)

    def try_play_card(self, player, card):
        if self.is_playable_card(card):
            self.play_card(player, card)
            return True
        else:
            print(f"the card {card} it is illegal , now you will get a card from the deck  ")
            self.draw_card(player)
            return False

    def start_game(self):

        self.play_first_card()
        game_over = False
        print()
        while not game_over:
            player = self.players[0]
            self.print_status()
            player.play_turn(self)
            print()

            print(f"Deck:{self.amount_of_cards} cards, table card is {self.last_card}")

            game_over = self.is_game_over(player)
            if game_over:
                break
            # TODO: do also to stop
            if self.should_activate_changing_direction:
                self.players.reverse()
                self.should_activate_changing_direction = False
 
            else:
                player = self.players[0]
                self.players.append(player)
                self.players.remove(player)

        player_min_card = min(self.players, key=lambda x: len(x.hand))
        if self.cards:
            print(f"The winner is {player_min_card} ")
        else:
            print(f"Game end, the deck is empty, the winner is {player_min_card} ")
        return player_min_card
