from Card import Card
import Deck

def get_key(obj):
    return obj.value

# Hand class models a hand of cards in reverse order
# each hand has a list of cards
# ranks the value of the players hand 0-9 and compares it to another hand to see who wins even if both have the same 0-9 value the compare method comapares two hands objects to ensure that if they are tied (the rank is the same) the winner is determined in acordance with poker rules.
# tuple, sort, count, remove
class Hand:
    
    def __init__(self):
        self.hand = []
    
#Your Hand class should have one attribute: a list that will receive cards as they are dealt. All cards should be stored in descending order according to their value. The class should also have the following methods:

    def get_hand(self):
        return self.hand

    def print_hand(self):
        for x in self.hand:
            print(x)
#prints all cards on their own line for readability.
            
    def add_card(self, card):
        self.hand.append(card)
        self.hand.sort(reverse=True, key=get_key)

    def get_card_value(self, num):
        return self.hand[num].get_value()

    def compare(self, other_hand):
        if self.rank() > other_hand.rank():
            return 1
        elif self.rank() < other_hand.rank():
            return -1
        else:
            if self.rank() == 9:
                return 0
            if self.rank() == 8 or self.rank() == 5 or self.rank() == 4 or self.rank() == 0:
                return self.comp_high(other_hand)
            if self.rank() == 7:
                return self.comp_four_kind(other_hand)
            if self.rank() == 6:
                return self.comp_full_house(other_hand)
            if self.rank() == 3:
                return self.comp_three_kind(other_hand)
            if self.rank() == 2:
                return self.comp_two_pair(other_hand)
            if self.rank() == 1:
                return self.comp_pair(other_hand)     

    def rank(self):
        if(self.isRoyalFlush()):
            return 9
        elif(self.isStraightFlush()):
            return 8
        elif(self.isFourKind()):
            return 7
        elif(self.isFullHouse()):
            return 6
        elif(self.isFlush()):
            return 5
        elif(self.isStraight()):
            return 4
        elif(self.isThreeKind()):
            return 3
        elif(self.isTwoPair()):
            return 2
        elif(self.isPair()):
            return 1
        else:
            return 0
    
    def comp_three_kind(self, other_hand):
        return self.comp_n_card(other_hand, 2)   

    def comp_four_kind(self, other_hand):
        return self.comp_n_card(other_hand, 2)


    def comp_full_house(self, other_hand):
        return self.comp_n_card(other_hand, 2)
        
    def comp_n_card(self, other_hand, n):
        if self.get_card_value(n) > other_hand.get_card_value(n):
            return 1
        elif self.get_card_value(n) < other_hand.get_card_value(n):
            return -1
        else: return 0 

    def comp_two_pair(self, other_hand):
        u_values1 = self.get_hand_values()
        u_values2 = other_hand.get_hand_values()

        hand_vals1 = self.get_all_hand_values()
        hand_vals2 = other_hand.get_all_hand_values()

        u_values1.remove(hand_vals1[1])
        u_values1.remove(hand_vals1[3])

        u_values2.remove(hand_vals2[1])
        u_values2.remove(hand_vals2[3])

        if self.comp_n_card(other_hand, 1) != 0:
            return self.comp_n_card(other_hand, 1)
        if self.comp_n_card(other_hand, 3) != 0:
            return self.comp_n_card(other_hand, 3)
        
        if u_values1[0] > u_values1[0]:
            return 1
        if u_values1[0] < u_values1[0]:
            return 1
        return 0


    def comp_pair(self, other_hand):
        u_values1 = self.get_hand_values()
        u_values2 = other_hand.get_hand_values()

        hand_vals1 = self.get_all_hand_values()
        hand_vals2 = other_hand.get_all_hand_values()

        for i in u_values1:
            if hand_vals1.count(i) > 1:
                temp1 = i
                u_values1.remove(i)
    
        for i in u_values2:
            if hand_vals2.count(i) > 1:
                temp2 = i
                u_values2.remove(i)
        if temp1 > temp2:
            return 1
        elif temp1 < temp2:
            return -1

        for i in range(3):
            if u_values1[i] > u_values2[i]:
                return 1
            elif u_values1[i] < u_values2[i]:
                return -1
        return 0

    def comp_high(self, other_hand):
        hand_vals1 = self.get_all_hand_values()
        hand_vals2 = other_hand.get_all_hand_values()

        for i in range(5):
            if hand_vals1[i] > hand_vals2[i]:
                return 1
            elif hand_vals1[i] < hand_vals2[i]:
                return -1
        return 0


    # VALUE + SUIT LIST MAKERS
    def get_all_hand_values(self):
        values = []
        for card in self.hand:
            values.append(card.get_value())
        return values
    
    def get_hand_values(self):
        values = []
        for card in self.hand:
            if card.get_value() not in values:
                values.append(card.get_value())
        return values

    def get_hand_suits(self):
        suits = []
        for card in self.hand:
            if card.get_suit() not in suits:
                suits.append(card.get_suit())
        return suits
    

    # IS CHECKERS
    def isRoyalFlush(self):
        values = self.get_hand_values()
        suits = self.get_hand_suits()

        if values == [14, 13, 12, 11, 10] and len(suits) == 1:
            return True
        return False

    def isStraightFlush(self):
        suits = self.get_hand_suits()
        count = 0
        nonCount = 0
        for i in range(len(self.hand)-1):
            if self.get_card_value(i) == self.get_card_value(i + 1) + 1:
                count += 1
            else:
                nonCount += 1
        if len(suits) == 1 and count == 4 and nonCount == 0:
            return True
        return False
    
    def isFourKind(self):
        val_list = self.get_all_hand_values()
        values = self.get_hand_values()

        count1 = val_list.count(values[0])
        count2 = val_list.count(values[1])

        if count1 == 4 or count2 == 4:
            return True
        return False
    
    def isFullHouse(self):
        val_list = self.get_all_hand_values()
        values = self.get_hand_values()

        count1 = val_list.count(values[0])
        count2 = val_list.count(values[1])

        if (count1 == 2 and count2 == 3) or (count1 == 3 and count2 == 2):
            return True
        return False

    def isFlush(self):
        suits = self.get_hand_suits()
        if len(suits) == 1:
            return True
        return False
    
    def isStraight(self):
        count = 0
        nonCount = 0
        for i in range(len(self.hand)-1):
            if self.get_card_value(i) == self.get_card_value(i + 1) + 1:
                count += 1
            else:
                nonCount += 1
        if count == 4 and nonCount == 0:
            return True
        return False
    
    def isThreeKind(self):
        val_list = self.get_all_hand_values()
        values = self.get_hand_values()

        count1 = val_list.count(values[0])
        count2 = val_list.count(values[1])
        count3 = val_list.count(values[2])

        if count1 == 3 or count2 == 3 or count3 == 3:
            return True
        return False

    def isTwoPair(self):
        count = 0
        for i in range(len(self.hand)-1):
            if self.get_card_value(i) == self.get_card_value(i + 1):
                count += 1
        if count == 2:
            return True
        return False

    def isPair(self):
        count = 0
        for i in range(len(self.hand)-1):
            if self.get_card_value(i) == self.get_card_value(i + 1):
                count += 1
        if count == 1:
            return True
        return False


# - returns an integer between 0 and 9 that corresponds to the hand's rank, following the standard ranking system for poker hands:
        
    def get_hand_type(self):
        ranks = ("High Card", "One Pair", "Two Pair", "Three-of-a-kind", "Straight", "Flush", "Full House", "Four-of-a-kind", "Straight Flush", "Royal Flush")
        rank = self.rank()

        return ranks[rank]