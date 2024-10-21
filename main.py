import Deck
import Hand
import Card
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
# main class models a 4 person poker game
# main class creates a poker game with 4 players dispalying their hands and uses methods to display who wins. I creates a list of of all 4 hands and that is used thought the code to compare and displayed all the hands.
# extends



poker_game = []
hand1 = Hand.Hand()
hand2 = Hand.Hand()
hand3 = Hand.Hand()
hand4 = Hand.Hand()

poker_game.append(hand1)
poker_game.append(hand2)
poker_game.append(hand3)
poker_game.append(hand4)

deck1 = Deck.Deck()
deck1.shuffle()


for i in range(5):
    hand1.add_card(deck1.deal_card())
    hand2.add_card(deck1.deal_card())
    hand3.add_card(deck1.deal_card())
    hand4.add_card(deck1.deal_card())

hands = []
hands.append(hand1.rank())
hands.append(hand2.rank())
hands.append(hand3.rank())
hands.append(hand4.rank())
hands.sort()
hands.reverse()

winner = None

if hands.count(hands[0]) == 1:
    for i in range(4):
        if poker_game[i].rank() == hands[0]:
            winner = poker_game[i]

elif hands.count(hands[0]) == 2:
    temp = []

    for i in range(4):
        if poker_game[i].rank() == hands[0]:
            temp.append(poker_game[i])
    if temp[0].compare(temp[1]) == 1:
        winner = temp[0]
    if temp[0].compare(temp[1]) == -1:
        winner = temp[1]

elif hands.count(hands[0]) == 3:
    temp = []
    for i in range(4):
        if poker_game[i].rank() == hands[0]:
            temp.append(poker_game[i])
    if temp[0].compare(temp[1]) == 1:
        winner = temp[0]
    if temp[0].compare(temp[1]) == -1:
        winner = temp[1]
    if temp[2].compare(temp[0]) == 1 and temp[2].compare(temp[1]) == 1:
        winner = temp[2]

else:
    temp = []

    for i in range(4):
        if poker_game[i].rank() == hands[0]:
            temp.append(poker_game[i])

    if temp[0].compare(temp[1]) == 1:
        r1 = temp[0]
    elif temp[0].compare(temp[1]) == -1:
        r1 = temp[1]
    
    if temp[2].compare(temp[3]) == 1:
        r2 = temp[2]
    elif temp[2].compare(temp[3]) == -1:
        r2 = temp[3]
    
    if r1.compare(r2) == 1 or r2 is None:
        winner = r1
    if r1.compare(r2) == -1 or r1 is None:
        winner = r2



def make_row(im1, im2, im3, im4, im5):
    row = Image.new('RGB', (im1.width*6, im1.height))
    row.paste(im1, (0, 0))
    row.paste(im2, (im1.width, 0))
    row.paste(im3, (im1.width*2, 0))
    row.paste(im4, (im1.width*3, 0))
    row.paste(im5, (im1.width*4, 0))
    return row

def make_columns(im1, im2, im3, im4):
    column = Image.new('RGB', (im1.width, im1.height*4))
    column.paste(im1, (0, 0))
    column.paste(im2, (0, im1.height))
    column.paste(im3, (0, im1.height*2))
    column.paste(im4, (0, im1.height*3))
    return column

handlistimg = []

for i in range(4):
    handlistimg.append(make_row(Image.open("Poker/cards/" + poker_game[i].get_hand()[0].image_file_name()), 
                        Image.open("Poker/cards/" + poker_game[i].get_hand()[1].image_file_name()), 
                        Image.open("Poker/cards/" + poker_game[i].get_hand()[2].image_file_name()), 
                        Image.open("Poker/cards/" + poker_game[i].get_hand()[3].image_file_name()), 
                        Image.open("Poker/cards/" + poker_game[i].get_hand()[4].image_file_name()), 
                        ))

game = make_columns(handlistimg[0], handlistimg[1], handlistimg[2], handlistimg[3])

#hand1.print_hand()
#hand2.print_hand()
#hand3.print_hand()
#hand4.print_hand()

I1 = ImageDraw.Draw(game)
myFront = ImageFont.truetype('Arial', 12)
winnerFont = ImageFont.truetype('Arial', 21)

# I1.text( (x, y), "text content", myFront, fill=(0, 0, 0)) 

final = []
final.extend(poker_game)
final.reverse()
for i in range(4):
    if(final[i] == winner):
        I1.text((game.width-95, game.height-60-(i*150)), "WINNER!", font=winnerFont, fill=(255, 0, 0))
    #else:
        #I1.text((game.width-95, game.height-60-(i*150)), "Loser", font=winnerFont, fill=(0, 225, 0))
    I1.text((game.width-85, game.height-75-(i*150)), final[i].get_hand_type(), font=myFront, fill=(255, 255, 255))

if winner == None:
    I1.text((510, 290), "PUSH!", font=winnerFont, fill=(255, 0, 0))

game.show()


#hand1.print_hand()
#hand2.print_hand()
#hand3.print_hand()
#hand4.print_hand()

#deck1 = Deck.Deck()
#deck1.shuffle()
#deck1.print_deck()

#card1 = Card.Card("Heart", 14)
#print(card1)

'''
hand1 = Hand.Hand()
c1 = Card.Card("Clubs", 14)
c2 = Card.Card("Clubs", 14)
c3 = Card.Card("Clubs", 9)
c4 = Card.Card("Diamonds", 5)
c5 = Card.Card("Clubs", 2)

hand2 = Hand.Hand()
c6 = Card.Card("Clubs", 11)
c7 = Card.Card("Clubs", 11)
c8 = Card.Card("Diamonds", 9)
c9 = Card.Card("Clubs", 8)
c10 = Card.Card("Clubs", 6)
hand1.add_card(c1)
hand1.add_card(c2)
hand1.add_card(c3)
hand1.add_card(c4)
hand1.add_card(c5)

hand2.add_card(c6)
hand2.add_card(c7)
hand2.add_card(c8)
hand2.add_card(c9)
hand2.add_card(c10)

#hand1.print_hand()
#print()
#hand2.print_hand()

print(hand1.get_hand_type())
print(hand2.get_hand_type())
print(hand1.compare(hand2))
'''