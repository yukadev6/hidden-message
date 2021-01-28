import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + 'of' + self.suit

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        return ', '.join(map(str,self.deck))

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,new_card):
        self.cards.append(new_card)
        self.value += values[card.rank]

    def adjust_for_ace(self):
        if self.value > 10
            'Ace' == 1
        else:
            'Ace' == 11

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        return self.total += self.bet
    
    def lose_bet(self):
        return self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("What do you bet? $ "))
        except:
            print('That is an invalid entry, please try again')    
        else: 
            if chips.bet > chips.total:
                print("You don't have enough chips to bet that.",chips.total)
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    next_play = input("Do you want to hit or stand? ")
    if next_play == 'hit':
        hit(deck,hand)
    elif next_play == 'stand':
        print("Player stands and next dealer's turn.")
        playing = False
    else:
        print("Sorry, please try again.")
        continue
    break
        
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:")
    print('',player.cards[0])
    print('',player.cards[1])
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(player,dealer,chips):
    chips.lose_bet()
    print("Player busts and loses chips. The dealer wins!")

def player_wins(player,dealer,chips):
    chips.win_bet()
    print("Player wins and takes chips! The dealer loses.")

def dealer_busts(player,dealer,chips):
    chips.win_bet()
    print("Dealer busts. Player wins and takes chips!")
    
def dealer_wins(player,dealer,chips):
    chips.lose_bet()
    print("Dealer wins! Player loses chips.")
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

while True:
    # Print an opening statement
    print("Welcome to Black Jack!")
    
    # Create & shuffle the deck, deal two cards to each player
    new_deck = Deck()
    new_deck.shuffle()
    
    player_hand = []
    (add_card(new_deck.deal())) * 2
    
    dealer_hand = []
    (add_card(new_deck.deal())) * 2
    
        
    # Set up the Player's chips
    player_chips = Chips()
    
    # Prompt the Player for their bet
    take_bet()
    
    # Show cards (but keep one dealer card hidden)
    show_some()
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        player_hand.hit_or_stand()
        
        # Show cards (but keep one dealer card hidden)
         show_some()
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand > 21:
            player_busts()
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand not player_busts:
        while dealer_hand < 17:
            dealer_hand.hit()
            break
    
        # Show all cards
        show_all()
        # Run different winning scenarios
        
    
    # Inform Player of their chips total 
    
    # Ask to play again

        break

        