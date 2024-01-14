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
    win_payout_ratio = 3/2
    draw_payout_ratio = 1
    lose_payout_ratio = 0
    
    i = 0
    while True:
        if player.get_score() > 21:
            print(f"BUST! YOU LOSE!")
            return lose_payout_ratio
        elif player.get_score() == 21:
            break 
        
        if i == 0:
            deal_cards(deck, dealer, player)
            if player.get_score() == 21:
                print("BLACKJACK!")
                return win_payout_ratio
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
            return win_payout_ratio   
        elif dealer.get_score() >= 17:
            break
        new_card = deck.draw_one_card()
        dealer.add_one_card("up", new_card)
        display_table(dealer, player)
    
    player_final_score = player.get_score()
    dealer_final_score = dealer.get_score()
    
    if player_final_score == dealer_final_score:
        print("DRAW.")
        return draw_payout_ratio
    elif player_final_score > dealer_final_score:
        print("YOU WIN!")
        return win_payout_ratio
    else:
        print("YOU LOSE.")
        return lose_payout_ratio


# # testing
# deck = Deck()
# dealer = Hand()
# player = Hand()

# play_blackjack(deck, dealer, player)