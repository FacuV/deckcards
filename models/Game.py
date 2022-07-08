from abc import ABC
import logging
from models.Movements import Movements

class Game(Movements):
    def sayHello(self):
        return super().sayHello()
    
    def draw(self, deck, num=1):
        return super().draw(deck, num)

    def showHand(self):
        return super().showHand()
    
    def discard(self):
        return super().discard()
    
    def __str__(self):
        logging.info(f'Bienvenido a Blackjack! {self.name}')
        return self