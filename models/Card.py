import logging

logging.basicConfig(filename='logs/card.log', level=logging.INFO)

class Card(object):    

    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
    
    def show(self):
        ''' Show the card '''
        if self.value == 1:
            val = "As"
        elif self.value == 11:
            val = "Sota"
        elif self.value == 12:
            val = "Reina"
        elif self.value == 13:
            val = "Rey"
        else:
            val = self.value

        return f"{val} de {self.suit}"

    # Implementing build in methods so that you can print a card object
    def __unicode__(self):
        return self.show()
    def __str__(self):
        return self.show()
    def __repr__(self):
        return self.show()