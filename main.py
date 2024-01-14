from card_stuff import Deck, Hand








def ask_bet(money: int):
    while True:
        print(f"You have ${money} available to play.")
        user_input = input(f"How much $ would you like to bet? [0-{money}]:")# Press 'quit' to exit.")
        if user_input == "quit":
            exit()
        try:
            bet = int(user_input)
        except:
            break
        if 0 <= bet <= money: 
            return bet
        

    
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