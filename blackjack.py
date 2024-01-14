from card_stuff import Deck, Hand
from user_input import ask_move   
        
                    
def display_table(dealer: Hand, player: Hand):
    print("--------------------------------")
    dealer.display_hand()
    print(f"Dealer Score: {dealer.get_score()}")
    player.display_hand()
    print(f"Player Score: {player.get_score()}")
    

def deal_cards(deck: Deck, dealer: Hand, player: Hand):
    dealer.add_one_card("down", deck.draw_one_card())
    player.add_one_card("up", deck.draw_one_card())
    dealer.add_one_card("up", deck.draw_one_card())
    player.add_one_card("up", deck.draw_one_card())

    dealer.display_hand()
    print(f"Dealer Score: {dealer.get_score()}")
    player.display_hand()
    print(f"Player Score: {player.get_score()}")
    

def play_blackjack(deck: Deck, dealer: Hand, player: Hand):
    i = 0
    while True:
        if player.get_score() > 21:
            print(f"BUST! YOU LOSE!")
            break
        elif player.get_score() == 21:
            print(f"BLACKJACK!")
            break
        
        if i == 0:
            deal_cards(deck, dealer, player)
        else:
            display_table(dealer, player) 
            
        move = ask_move()
        
        if move == "hit":
            new_card = deck.draw_one_card()
            player.add_one_card("up", new_card)
            display_table(dealer, player)
        elif move == "stand":
            display_table(dealer, player)
            print(f"Player Final Score: {player.get_score()}")
            break
        i += 1
    
    dealer.flip_face_down_card()
    display_table(dealer, player)
    
    while True:
        if dealer.get_score() > 21:
            print("DEALER BUSTED! YOU WIN!")
            break   
        elif dealer.get_score() >= 17:
            break
        new_card = deck.draw_one_card()
        dealer.add_one_card("up", new_card)
        display_table(dealer, player)
    
    player_final_score = player.get_score()
    dealer_final_score = dealer.get_score()
    
    if player_final_score == dealer_final_score:
        print("DRAW.")
        payout = 1
    elif player_final_score > dealer_final_score:
        print("YOU WIN!")
        payout = 3/2
    else:
        print("YOU LOSE.")
        payout = 0
    
    print(f"Total Payout: {payout}")    
    return payout


# testing
deck = Deck()
dealer = Hand()
player = Hand()

# deal_cards(deck, dealer, player)
play_blackjack(deck, dealer, player)