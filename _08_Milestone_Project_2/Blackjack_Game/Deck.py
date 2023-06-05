import random

from _08_Milestone_Project_2.Blackjack_Game.Card import Card


class Deck:
    def __init__(self):
        self.deck = []
        for suit in Card.suits:
            for rank in Card.ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.deck)

    def deal(self):
        # Note we remove one card from the list of all_cards
        single_card = self.deck.pop()
        return single_card

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()  # add each Card object's print string
        return 'The deck has:' + deck_comp

