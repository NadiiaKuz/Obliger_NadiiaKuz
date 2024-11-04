import random

class Cart:
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value
    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Jack":10, "Queen":10, "King":10, "Ace":11}
        self.cards = self.build_deck()

    # lager en kortstokk
    def build_deck(self):
        return [Cart(rank, suit, self.values[rank]) for suit in self.suits for rank in self.ranks]

    #blander kortstokken
    def shuffle_deck(self):
        random.shuffle(self.cards)

    # fjerner det gitte kortet fra kortstokken
    def deal_card(self):
        return self.cards.pop() if self.cards else None
