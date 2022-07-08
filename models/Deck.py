import random
from models.Card import Card

class Deck(object):

    def __init__(self):
        self.cards = []
        self.build()

    def show(self):
        ''' Show all cards in the deck '''
        
        for card in self.cards:
            print(card.show())
        pass

    def build(self):
        ''' Generate 52 cards '''

        self.cards = []
        for suit in ['Corazones', 'Trébol', 'Diamantes', 'Picas']:
            for val in range(1,14):
                self.cards.append(Card(suit, val))

    def shuffle(self, num=1):
        ''' Shuffle the deck '''

        length = len(self.cards)
        for _ in range(num):
            for i in range(length-1, 0, -1):
                randi = random.randint(0, i)
                if i == randi:
                    continue
                self.cards[i], self.cards[randi] = self.cards[randi], self.cards[i]
        return self

    def deal(self):
        ''' Return the top card '''
        return self.cards.pop()

    def __str__(self):
        return "Deck: {}".format(self.cards)
