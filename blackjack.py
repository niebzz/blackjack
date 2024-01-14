from card_stuff import Deck, Hand


def set_table(deck: Deck, dealer: Hand, player: Hand):
    dealer.add_one_card("down", deck.draw_one_card())
    player.add_one_card("up", deck.draw_one_card())
    dealer.add_one_card("up", deck.draw_one_card())
    player.add_one_card("up", deck.draw_one_card())

    dealer.display_hand()
    print(f"Dealer Score: {dealer.get_score()}")
    player.display_hand()
    print(f"Player Score: {player.get_score()}")

def ask_move():
    while True:
        moves = ["hit", "stand", "h", "s"]
        user_input = input(f"Would you like to '(H)it' or '(S)tand'? Press '(Q)uit to quit.").lower()
        if user_input in ["quit", "q"]:
            exit()
        if user_input in moves:
            if user_input in ["hit", "h"]:
                return "hit"
            elif user_input in ["stand", "s"]:
                return "stand"
            print("Invalid input.")
        
        
def display_table(dealer: Hand, player: Hand):
    dealer.display_hand()
    print(f"Dealer Score: {dealer.get_score()}")
    player.display_hand()
    print(f"Player Score: {player.get_score()}")
    
def play_blackjack():
    pass
    
def main():
    deck = Deck()
    dealer = Hand()
    player = Hand()
    
    set_table(deck, dealer, player)
    
    while True:
        if player.get_score() > 21:
            print(f"BUST! YOU LOSE!")
            exit()
        move = ask_move()
        if move == "hit":
            new_card = deck.draw_one_card()
            player.add_one_card("up", new_card)
            display_table(dealer, player)
        elif move == "stand":
            display_table(dealer, player)
            print(f"Player Final Score: {player.get_score()}")
            break
    
    dealer.flip_face_down_card()
    display_table(dealer, player)
    
    while True:
        if dealer.get_score() > 21:
            print("DEALER BUSTED! YOU WIN!")
            exit()   
        elif dealer.get_score() >= 17:
            display_table(dealer, player)
            break
        new_card = deck.draw_one_card()
        dealer.add_one_card("up", new_card)

    
    display_table(dealer, player)
    p_final = player.get_score()
    d_final = dealer.get_score()
    
    print("OUTCOME:")
    if p_final == d_final:
        print("DRAW.")
    elif p_final > d_final:
        print("YOU WIN!")
    else:
        print("YOU LOSE.")
            
    
    
if __name__ == "__main__":
    main()