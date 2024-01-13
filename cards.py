import random

#################################
### GENERAL CONSTANTS
#################################

NUM_DECKS = 1 # number of decks to play with

HEARTS = chr(9829)   # ♥
SPADES = chr(9824)   # ♠
DIAMONDS = chr(9830) # ♦
CLUBS = chr(9827)    # ♣

suits = (HEARTS, SPADES, DIAMONDS, CLUBS)


#################################
### ONE SINGLE CARD
#################################


def generate_2D_card(value="#", suit="#"):        
    top = ["+", "-", "-", "-", "+"]
    middle1 = ["|", value, "#", " ", "|"]
    middle2 = ["|", "#", suit, "#", "|"]
    middle3 = ["|", " ", "#", value, "|"]
    bottom = ["+", "-", "-", "-", "+"]
    
    return [row for row in [top, middle1, middle2, middle3, bottom]]
    
       
class Card:
    def __init__(self, card: tuple):
        if type(card) != tuple or len(card) != 2:
            raise TypeError("Invalid Card. Please enter a valid card format.")
        self.card = card
                

    def get_card(self):
        return self.card
    
        
    def display_card(self, reverse=False):
        if reverse:
            for row in self.back:
                print("".join(row))      
        else:
            for row in self.front:
                print("".join(row))
        
        
    front = generate_2D_card()
    back = generate_2D_card() 
        

#################################
### ENTIRE DECK
#################################


def initialize_deck(number_of_decks):
    deck = []
    for suit in suits:
        for i in range(2, 11):
            deck.append((i, suit))
        for j in ["J", "Q", "K", "A"]:
            deck.append((j, suit))
    return deck * number_of_decks
        
        
class Deck:
    def __init__(self, num_decks: int):
        self.num_decks = num_decks


    def shuffle_deck(self):
        random.shuffle(self.cards)
       
        
    def get_cards(self):
        return self.cards
    
    
    def display_cards(self):
        print(self.cards)       
            
                
    cards = initialize_deck(NUM_DECKS)
    



deck = Deck(1)

card1 = deck.get_cards()

print(card1)
