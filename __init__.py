from models.Deck import Deck
from models.Game import Game
from models.User import User

myDeck = Deck()
myDeck.shuffle()

facu = Game("Facu")
facu.draw(myDeck, 5)
facu.showHand()

delfi = Game("Delfi")
delfi.draw(myDeck, 5)
delfi.showHand()

game = Game('Facu')
print(game)

deck = Deck()
print(deck)

facuUser = User('Facundo', 'Vicente', 20)
delfiUser = User('Delfina', 'Gerea', 20)

print(User('Facundo', 'Vicente', 20))
print(User('Delfina', 'Gerea', 20))