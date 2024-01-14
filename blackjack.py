from card_stuff import Deck, Hand
from table_logic import deal_cards, display_table
from user_input import ask_move, ask_bet


def play_blackjack(deck: Deck, dealer: Hand, player: Hand) -> int:
    win_payout_ratio = 3/2
    draw_payout_ratio = 1
    lose_payout_ratio = -1

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
        print(f"YOU LOSE. (dealer had {dealer_final_score} points)")
        return lose_payout_ratio


def main():
    print("""
####################################
#       WELCOME TO BLACKJACK       #
####################################
          """)

    card_deck = Deck()
    dealer_hand = Hand()
    player_hand = Hand()

    MONEY = 50
    while MONEY > 0:
        bet = ask_bet(MONEY)
        payout_ratio = play_blackjack(card_deck, dealer_hand, player_hand)

        MONEY += int(bet * payout_ratio)

        dealer_hand.reset_hand()
        player_hand.reset_hand()

    print("GAME OVER! YOU LOST ALL OF YOUR MONEY.")


if __name__ == "__main__":
    main()
