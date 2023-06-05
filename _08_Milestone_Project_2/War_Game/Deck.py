from _08_Milestone_Project_2.War_Game.Card import Card
import random


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in Card.suits:
            for rank in Card.ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        # Note this doesn't return anything
        random.shuffle(self.all_cards)

    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()


