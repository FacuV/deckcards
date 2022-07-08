import logging

logging.basicConfig(filename='logs/player.log', level=logging.INFO)

class Player(object):

    def __init__(self, name):
        self.name = name
        self.hand = []

    def sayHello(self):
        ''' Say hello to the player '''
        try:
            welcomeMsg = "Hola, mi nombre es {}".format(self.name)
            print(welcomeMsg)

        except Exception as e:
            logging.error("Error: {}".format(e))
            print("Error: {}".format(e))
            return self

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

    def showHand(self):
        ''' Show the cards in the hand '''

        try:
            logging.info("{}'s hand: {}".format(self.name, self.hand))
            print (f"Mano de {self.name}: {self.hand}")
            return self
        except Exception as e:
            logging.error("Error: {}".format(e))
            print("Error: {}".format(e))
            return self

    def discard(self):
        ''' Discard all cards in the hand '''
        return self.hand.pop()

    def __str__(self):
        return (f'Hola! {self.name}, bienvenido a Blackjack!')