from models.Deck import Deck
from models.Player import Player

import logging

logging.basicConfig(filename='logs/main.log', level=logging.INFO)

myDeck = Deck()
myDeck.shuffle()

facu = Player('Facu')
facu.draw(myDeck, 3)
facu.showHand()

delfi = Player('Delfi')
delfi.draw(myDeck, 3)
delfi.showHand()