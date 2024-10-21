# Cards class models indivudal cards
# each cardshas a suit (Clubs, Spades, etc) and a value (2-10, J, Q, K, A)
# aquires the english name and file of each name along with its value and suit
# 
class Card:

    def __init__ (self, suit, value):
        self.suit = suit
        self.value = value

    def get_value(self):
        return self.value
    
    def get_suit(self):
        return self.suit
    
    def __repr__ (self):
        if self.value < 11 and self.value > 1:
            return f"{self.value} of {self.suit}"
        elif self.value == 11:
            return f"Jack of {self.suit}"
        elif self.value == 12:
            return f"Queen of {self.suit}"
        elif self.value == 13:
            return f"King of {self.suit}"
        elif self.value == 14:
            return f"Ace of {self.suit}"
        else:
            return "no card error"


    def image_file_name(self):
        if self.value < 11:
            return str(self.value) + "_of_" + self.suit.lower() + ".png"
        elif self.value == 11:
            return "jack_of_" + self.suit.lower() + ".png"
        elif self.value == 12:
            return "queen_of_" + self.suit.lower() + ".png"
        elif self.value == 13:
            return "king_of_" + self.suit.lower() + ".png"
        elif self.value == 14:
            return "ace_of_" + self.suit.lower() + ".png"
        else:
            return "ace_of_" + self.suit.lower() + ".png"
    
#- returns a string that corresponds to the file name of the cards image. For example, "2_of_clubs.png" or "jack_of_hearts.png".

