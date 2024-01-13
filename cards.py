import random

###########################################
### CONSTANTS
###########################################

NUM_DECKS = 1 # number of decks to play with

HEARTS = chr(9829)   # ♥
SPADES = chr(9824)   # ♠
DIAMONDS = chr(9830) # ♦
CLUBS = chr(9827)    # ♣

suits = (HEARTS, SPADES, DIAMONDS, CLUBS)


###########################################
### ONE SINGLE CARD
###########################################


def generate_2D_card(orientation: str, value="#", suit="#"):
    assert orientation.lower() in ["up", "down"]

    match orientation:
        case "up":
            extra_space = " "
        case "down":
            extra_space = "#"            
    
            
    top = ["+", "-", "-", "-", "+", "   "]
    middle1 = ["|", value, extra_space, " ", "|", "   "]
    middle2 = ["|", extra_space, suit, extra_space, "|", "   "]
    middle3 = ["|", " ", extra_space, value, "|", "   "]
    bottom = ["+", "-", "-", "-", "+", "   "]
    
    return  [row for row in [top, middle1, middle2, middle3, bottom]]
    
       
def display_card_front(card_value: str, card_suit: str) -> None:
    for row in generate_2D_card(orientation="up", value=card_value, suit=card_suit):
        print("".join(row))
        
                
def display_card_back() -> None:
    for row in generate_2D_card(orientation="down"):
        print("".join(row))
        


###########################################
### ENTIRE DECK
###########################################


def initialize_deck(number_of_decks):
    deck = []
    for suit in suits:
        for i in range(2, 10):
            deck.append((str(i), suit))
        for j in ["T", "J", "Q", "K", "A"]:
            deck.append((j, suit))
    return deck * number_of_decks
        
        
class Deck:
    cards = initialize_deck(NUM_DECKS)
    
    def __init__(self):
        random.shuffle(self.cards)

    def shuffle_deck(self):
        self.cards = initialize_deck(NUM_DECKS)
        random.shuffle(self.cards)
            
    def get_cards(self):
        return self.cards
    
    def display_cards(self):
        print(self.cards)
        
    def draw_one_card(self):
        return self.cards.pop(0)
            
                
###########################################
### PLAYER OR DEALER'S HAND
###########################################


class Hand:
    def __init__(self):
        pass
    
    cards = []
    def add_one_card(self, orientation: str, card: tuple):
        assert orientation in ["up", "down"]
        assert type(card) == tuple
        assert type(card[0]) == str
        assert type(card[1]) == str
        
        card_details = [card[0], card[1], orientation]
        self.cards.append(card_details)

    def get_cards(self) -> list:
        return self.cards
    
    def get_score(self) -> int:
        score = 0
        for card in self.cards:
            value = card[0]
            orientation = card[2]
            if orientation == "down":
                continue
            elif value in [str(x) for x in range(2, 10)]:
                score += int(value)
            elif value in ["T", "J", "Q", "K"]:
                score += 10
            elif value == "A":
                score += 11
            
        aces = [card[0] for card in self.cards if card[0] == "A" and card[2] == "up"]
        if score > 21 and len(aces) == 1:
            score -= 10
        if score > 21 and len(aces) == 2:
            score -= 10
        
        return score
                    
    def display_hand(self) -> None:
        num_cards = len(self.cards)
        
        row1 = num_cards * generate_2D_card("down")[0]
        row2 = num_cards * generate_2D_card("down")[1]
        row3 = num_cards * generate_2D_card("down")[2]
        row4 = num_cards * generate_2D_card("down")[3]
        row5 = num_cards * generate_2D_card("down")[4]
        
        values = [card[0] for card in self.cards]
        suits = [card[1] for card in self.cards]
        orientations = [card[2] for card in self.cards]
        
        for i, v in enumerate(values):
            if orientations[i] == "up":               
                row2[1 + (i * 6)] = v
                row2[2 + (i * 6)] = " "
                row4[3 + (i * 6)] = v
                row4[2 + (i * 6)] = " "
                
        for i, s in enumerate(suits):
            if orientations[i] == "up":               
                row3[1 + (i * 6)] = " "
                row3[2 + (i * 6)] = s
                row3[3 + (i * 6)] = " "
       
        
        for row in [row1, row2, row3, row4, row5]:
            print("".join(row))


deck = Deck()
dealer = Hand()
player = Hand()


dealer.add_one_card("down", deck.draw_one_card())
dealer.add_one_card("up", deck.draw_one_card())
dealer.add_one_card("up", deck.draw_one_card())
dealer.add_one_card("up", deck.draw_one_card())

dealer.display_hand()
print(dealer.get_score())