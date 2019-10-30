from random import randint
"""
init(): randomly deals out a list of 13 numbers to each player's hand
make_teams(): well it makes teams and u can pick 1v1 or 2v2
passing(): passes
sort_discard(): adds discard pile to the player who takes the round (which used to count points in the end)
count_points(): counts points, duh
card_suit(): takes an input that is a str (e.g. '2s', '2h', etc) and returns the suit it is in (a list containing all the numbered cards in that suit)
can_play(): Checks if card played is valid
order(): makes sure the order of moves is right even after someone takes a round
play_loop(): the actual playing of the game.
"""
 
""" ############################################### CONSTANTS ############################################### """
#s = "♠"
#h = "♥"
#c = "♣"
#d = "♦"
suits = ['s', 'h', 'c', 'd']
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
cards = []
for i in suits:
   for j in numbers:
       cards.append(str(j)+i)
spades = cards[:13]
hearts = cards[13:26]
clubs = cards[26:39]
diamonds = cards[39:]
better_cards = [spades, hearts, clubs, diamonds]
point_cards = {'2h': 0, '3h': 0, '4h': 0,
              '5h': 10, '6h': 10, '7h': 10, '8h': 10, '9h': 10, '10h': 10,
              'Jh': 20, 'Qh': 30, 'Kh': 40, 'Ah': 50,
              'Qs': 100, 'Jd': -100}
""" ############################################### VARIABLES ############################################### """
mode = ""
P1 = input("Enter Player 1's name: ").title()
P2 = input("Enter Player 2's name: ").title()
P3 = input("Enter Player 3's name: ").title()
P4 = input("Enter Player 4's name: ").title()
players = [P1, P2, P3, P4]
player_teams = []
P1_hand = []
P2_hand = []
P3_hand = []
P4_hand = []
hands = [P1_hand, P2_hand, P3_hand, P4_hand]
P1pp = []
P2pp = []
P3pp = []
P4pp = []
counting_points_piles = [P1pp, P2pp, P3pp, P4pp]
move = 0
player_pile = []
""" ############################################### FUNCS ############################################### """
 
 
def init():
   global hands
   global cards
   global suits
   global numbers
   global move
   global mode
   while mode not in ["1v1", "2v2"]:
     mode = input("Would you like to play 1v1 or 2v2?")
   P1hand = None
   P2hand = None
   P3hand = None
   P4hand = None
   rand_card_list = []
   while len(rand_card_list) < 52:
       x = randint(0, 51)
       if not x in rand_card_list:
           rand_card_list.append(x)
   P1hand = rand_card_list[0:13]
   P2hand = rand_card_list[13:26]
   P3hand = rand_card_list[26:39]
   P4hand = rand_card_list[39:52]
   P1hand.sort()
   P2hand.sort()
   P3hand.sort()
   P4hand.sort()
   for i in P1hand:
       hands[0].append(cards[i])
   for i in P2hand:
       hands[1].append(cards[i])
   for i in P3hand:
       hands[2].append(cards[i])
   for i in P4hand:
       hands[3].append(cards[i])
   if mode == "2v2":
     make_teams()
   passing()
   for hand in hands:
       if '3c' in hand:
           move = hands.index(hand)
 
def make_teams():
 global players
 global player_teams
 team_determinants = ["Ac", "Kc", "Ad", "Kd"]
 for player in players:
   input("{}'s turn to draw a card. ENTER to continue.".format(player))
   input("Pick a number: {}".format(list(range(1, (len(team_determinants)+1)))))
   card_picked = team_determinants[randint(0, (len(team_determinants)-1))]
   while (len(team_determinants) > 1) and (player == "Ricky") and (card_picked == "Ac"):
     print("Ricky got the ace of clubs! \nHe slaps it back onto the (virtual) table and draws again.")
     card_picked = team_determinants[randint(0, (len(team_determinants-1)))]
   team_determinants.remove(card_picked)
   print("Your card is {}".format(card_picked))
   player_teams.append(card_picked)
 
def passing():
  global players
  global hands
  pass_bucket = []
  for i in players:
    print(i)
    print(i + " please select 3 cards to pass")
    print(hands[players.index(i)])
    single_pass = []
    card_count = 0
    while card_count < 3:
      card_passed = input()
      while card_passed not in hands[players.index(i)]:
        print("Please choose a valid card to pass")
        card_passed = input()
      hands[players.index(i)].remove(card_passed)
      single_pass.append(card_passed)
      card_count += 1
    pass_bucket.append(single_pass)
  for i in pass_bucket:
    if pass_bucket.index(i) != 3:
      z = pass_bucket.index(i) + 1
    elif pass_bucket.index(i) == 3:
      z = 0
    hands[z].append(i[0])
    hands[z].append(i[1])
    hands[z].append(i[2])
    temporary = []
    for i in hands[z]:
      temporary.append(cards.index(i))
      temporary.sort()
    hands[z] = []
    for k in temporary:
      hands[z].append(cards[k])
 
def sort_discard(player, pile):
 counting_points_piles[player] += pile

def count_points(points):
 global point_cards
 global hearts
 count = 0
 has_hearts = []
 other_point_cards = []
 for i in points:
     if i in hearts:
         has_hearts.append(i)
     elif i == 'Qs' or i == 'Jd' or i == '10c':
         other_point_cards.append(i)
 if len(has_hearts) == 13:
    count = -200
    for i in other_point_cards:
      if i in ['Qs', 'Jd']:
        count -= 100
    for i in other_point_cards:
      if i == '10c':
        count = count * 2
 else:
   for i in has_hearts:
     count += point_cards.get(i)
   for i in other_point_cards:
     if i == 'Qs':
       count += 100
     if i == 'Jd':
       count -= 100
     if i == '10c':
       if len(has_hearts) == 0 and len(other_point_cards) == 1:
         count = -50
       else:
         count = count * 2
 return count

def card_suit(card):
 global spades
 global clubs
 global diamonds
 global hearts
 for suit in [spades, clubs, diamonds, hearts]:
   if card in suit:
     return suit

def can_play(card, player):
  global hands
  global player_pile
  global spades
  global clubs
  global diamonds
  global hearts
  global cards
  suit_list = []
  if card not in hands[player]:
    return False
  elif ('3c' in hands[player]) and (card != '3c'):
    return False
  elif (len(player_pile) > 0):
    if (card_suit(cards[player_pile[0]]) != card_suit(card)):
      for i in hands[player]:
        if i in card_suit(cards[player_pile[0]]):
          suit_list.append(i)
      if len(suit_list) > 0:
        return False
      else:
        return True
    else:
      return True
  else:
    return True
 
 
def order(move):
 if move == 0:
     return [0, 1, 2, 3]
 elif move == 1:
     return [1, 2, 3, 0]
 elif move == 2:
     return [2, 3, 0, 1]
 else:
     return [3, 0, 1, 2]

def play_loop():
 global players
 global move
 global hands
 global spades
 global hearts
 global clubs
 global diamonds
 global better_cards
 global player_pile
 i = order(move)[0]
 input("{}'s turn. Ready to play? ENTER to continue. ".format(players[i]))
 while (len(hands[0]) > 0) and (len(hands[1]) > 0) and (len(hands[2]) > 0) and (len(hands[3]) > 0):
    discard_pile = []
    counting_points_pile = []
    player_pile = []
    orders = order(move)
    for player in order(move):
       print(players[player] + "'s turn")
       card_played = input("{} \nCard to play: ".format(hands[player]))
       while not can_play(card_played, player):
          print("Please play a valid card")
          card_played = input()
       hands[player].remove(card_played)
       discard_pile.append(cards.index(card_played))
       player_pile.append(cards.index(card_played))
       counting_points_pile.append(card_played)
    for i in better_cards:
     for j in i:
       if cards[player_pile[0]] == j:
         for k in discard_pile:
           if cards[k] not in i:
             discard_pile.remove(k)
    discard_pile.sort()
    print(discard_pile)
    for l in orders:
     if discard_pile[-1] == player_pile[orders.index(l)]:
       move = l
       sort_discard(l, counting_points_pile)

def game_end():
   global discard_pile
   global players
   global P1_points
   global P2_points
   global P3_points
   global P4_points
   global P1pp
   global P2pp
   global P3pp
   global P4pp
   global player_teams
   P1_points = count_points(P1pp)
   P2_points = count_points(P2pp)
   P3_points = count_points(P3pp)
   P4_points = count_points(P4pp)
   P_points = [P1_points, P2_points, P3_points, P4_points]
   print(P1 + " got " + str(P1_points) + " points")
   print(P2 + " got " + str(P2_points) + " points")
   print(P3 + " got " + str(P3_points) + " points")
   print(P4 + " got " + str(P4_points) + " points")
   if mode == "1v1":
     if P4_points < P1_points and P4_points < P1_points and P4_points < P1_points:
         print(P4 + " wins!")
     elif P3_points < P1_points and P3_points < P2_points and P3_points < P4_points:
         print(P3 + " wins!")
     elif P2_points < P1_points and P2_points < P3_points and P2_points < P4_points:
         print(P2 + " wins!")
     elif P1_points < P2_points and P1_points < P3_points and P1_points < P4_points:
         print(P1 + " wins!")
   else:
     black_pts = 0
     red_pts = 0
     for player_team in player_teams:
       print("{} was {}".format(players[player_teams.index(player_team)], player_team))
       if player_team in ["Ac", "Kc"]:
         black_pts += P_points[player_teams.index(player_team)]
       else:
         red_pts += P_points[player_teams.index(player_team)]
     print("Black got {} pts, red got {} pts.".format(black_pts, red_pts))
 
""" ############################################### RUN LOOP ############################################### """
init()
play_loop()
game_end()
 
 
 
 

