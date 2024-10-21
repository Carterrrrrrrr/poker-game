import random
import Card

# Deck class models a deck of 52 cards
# each has a list of one of every card (no jokers)
# creates a 52 card deck allows randomaztion of the deck and deals (returns) the next card in the deck
# tuple, copy, append, clear, pop
class Deck:
    def __init__ (self):
        self.the_deck = []
        for i in range(13):
            self.the_deck.append(Card.Card("Diamonds", i+2))
        for i in range(13):
            self.the_deck.append(Card.Card("Spades", i+2))
        for i in range(13):
            self.the_deck.append(Card.Card("Clubs", i+2))
        for i in range(13):
            self.the_deck.append(Card.Card("Hearts", i+2))
        self.deck = tuple(self.the_deck.copy())
        self.the_deck.clear()
            

# Your Deck class should have one attribute: a list that will store all 52 cards. It should also have the following methods:

    def get_deck(self):
        return self.deck

    def print_deck(self):
        for x in self.deck:
            print(x)
    
    def shuffle(self):
        self.the_deck = list(self.deck)
        random.shuffle(self.the_deck)
        self.deck = self.the_deck.copy()
        self.the_deck.clear()
    
    def deal_card(self):
        if len(self.deck) > 0:   
            delt = self.deck[0]
            self.deck.pop(0)
            return delt
        else:
            return None
    
#removes and returns the top card in the deck. Returns None if the deck is empty.