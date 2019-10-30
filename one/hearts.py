from random import randint

"""==========CONSTANTS=========="""
s = "♠"
h = "♥"
c = "♣"
d = "♦"
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = [h, s, c, d]
numbers = range(0, 13)

"""==========VARIABLES=========="""

P1_cards = []
P2_cards = []
P3_cards = []
P4_cards = []

"""==========INIT=========="""

def deal(): 
    global P1_cards
    global P2_cards
    global P3_cards
    global P4_cards

    cards = []
    for suit in suits: 
        for number in numbers: 
            cards.append(values[number]+suit)

    while len(cards) != 0:
        card_index = randint(0, (len(cards) - 1))
        if len(P1_cards) < 13:
            P1_cards.append(cards[card_index])
        elif len(P2_cards) < 13:
            P2_cards.append(cards[card_index])
        elif len(P3_cards) < 13:
            P3_cards.append(cards[card_index])
        else:
            P4_cards.append(cards[card_index])
        del cards[card_index]
    

deal()

print(P1_cards)
print(P2_cards)
print(P3_cards)
print(P4_cards)    











from random import randint

"""==========CONSTANTS=========="""
s = "♠"
h = "♥"
c = "♣"
d = "♦"
from random import randint
 
"""==========CONSTANTS=========="""
s = "♠"
h = "♥"
c = "♣"
d = "♦"
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = [h, s, c, d]
numbers = range(0, 13)
 
"""==========VARIABLES=========="""
P1 = ["Player1", []]
P2 = ["Player2", []]
P3 = ["Player3", []]
P4 = ["Player4", []]
 
players = [P1, P2, P3, P4]
 
"""==========INIT=========="""
 
def deal():
   global players
 
   cards = []
   for suit in suits:
       for number in numbers:
           cards.append(values[number]+suit)
 
   while len(cards) != 0:
       card_index = randint(0, len(cards)-1)
       for player in players:
           print(player)
           print(player[1])
           print(len(player[1]))
           while len(player[1]) < 13:
               player[1].append(cards[card_index])
               del cards[card_index]
  
 
deal()
 
print(players[1][1])
print(players[2][1])
print(players[3][1])
print(players[4][1])
 

