from card_stuff import Deck, Hand


def deal_cards(deck: Deck, dealer: Hand, player: Hand):
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
        user_input = input(f"Would you like to '(H)it' or '(S)tand'? Press 'quit' to exit.").lower()
        if user_input in ["quit", "q"]:
            exit()
        if user_input in moves:
            if user_input in ["hit", "h"]:
                return "hit"
            elif user_input in ["stand", "s"]:
                return "stand"
            print("Invalid input.")


def ask_bet(money: int):
    while True:
        print(f"You have ${money} available to play.")
        user_input = input(f"How much $ would you like to bet? [0-{money}].")# Press 'quit' to exit.")
        if user_input == "quit":
            exit()
        try:
            bet = int(user_input)
        except:
            break
        if 0 <= bet <= money: 
            return bet
        
        
def display_table(dealer: Hand, player: Hand):
    print("-----------------------")
    dealer.display_hand()
    print(f"Dealer Score: {dealer.get_score()}")
    player.display_hand()
    print(f"Player Score: {player.get_score()}")
    
    
def play_blackjack(deck: Deck, dealer: Hand, player: Hand):
    while True:
        if player.get_score() > 21:
            print(f"BUST! YOU LOSE!")
            break
        elif player.get_score() == 21:
            print(f"BLACKJACK!")
            break
        
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
    
    dealer.flip_face_down_card()
    display_table(dealer, player)
    
    while True:
        if dealer.get_score() > 21:
            print("DEALER BUSTED! YOU WIN!")
            break   
        elif dealer.get_score() >= 17:
            display_table(dealer, player)
            break
        new_card = deck.draw_one_card()
        dealer.add_one_card("up", new_card)
        display_table(dealer, player)
    
    display_table(dealer, player)
    p_final = player.get_score()
    d_final = dealer.get_score()
    
    if p_final == d_final:
        print("DRAW.")
        payout = 1
    elif p_final > d_final:
        print("YOU WIN!")
        payout = 3/2
    else:
        print("YOU LOSE.")
        payout = 0
        
    return payout


    
def main():
    deck = Deck()
    dealer = Hand()
    player = Hand()
    
    MONEY = 50
    i = 0
    while MONEY > 0:
        bet = ask_bet(int(MONEY))
        # print(type(bet))
        if i == 0:
            deal_cards(deck, dealer, player)
                
        MONEY -= bet
        payout = play_blackjack(deck, dealer, player)
        MONEY += payout * bet
        i+= 1
    
    print(f"Game Over. {i} games played.")
    
if __name__ == "__main__":
    main()