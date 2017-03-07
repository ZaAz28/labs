import random

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


    def __repr__(self):
        return"%s %s" % (self.suit, self.rank)

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["Clubs", "Diamonds", "Hearts", "Spades"]:
            for rank in range(1,14):
                card = Card(rank, suit)
                self.cards.append(card)
        random.shuffle(self.cards)

    def __str__(self):
        return self.cards

    def __next__(self):
        return self.cards.pop()

class Pyramid:
    def __init__(self):
        self.cards_pyramid = []

    def __str__(self):
        return self.cards_pyramid


class Game:
    def __init__(self):
        self.deck = Deck()
        self.pyramid = Pyramid()
        for i in range(28):
            self.pyramid.cards_pyramid.append(self.deck.__next__())

    def __str__(self):
        return self.pyramid.cards_pyramid


if __name__ == "__main__":
    mydeck = Deck()
    print(mydeck.__str__())
    mygame = Game()

    print(mygame.__str__())
    mypyramid = Pyramid()
    print(mypyramid.__str__())
