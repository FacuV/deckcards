from abc import ABC, abstractmethod
import logging

logging.basicConfig(filename='logs/main.log', level=logging.INFO)

class Movements(ABC, object):

    def __init__(self, name):
        self.name = name
        self.hand = []

    @abstractmethod
    def sayHello(self):
        ''' Say hello to the player '''
        try:
            welcomeMsg = "Hola, mi nombre es {}".format(self.name)
            print(welcomeMsg)

        except Exception as e:
            logging.error("Error: {}".format(e))
            print("Error: {}".format(e))
            return self

    @abstractmethod
    def draw(self, deck, num=1):
        ''' Draw n number of cards from a deck '''
        try:
            for _ in range(num):
                self.hand.append(deck.deal())
            return self
        except Exception as e:
            logging.error("Error: {}".format(e))
            print("Error: {}".format(e))
            return self

    @abstractmethod
    def showHand(self):
        ''' Show the cards in the hand '''

        try:
            logging.info (f"Mano de {self.name}: {self.hand}")
            print (f"Mano de {self.name}: {self.hand}")
            return self
        except Exception as e:
            logging.error("Error: {}".format(e))
            print("Error: {}".format(e))
            return self

    @abstractmethod
    def discard(self):
        ''' Discard all cards in the hand '''
        return self.hand.pop()

    def __str__(self):
        return (f'Hola! {self.name}, bienvenido a Blackjack!')