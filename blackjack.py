from cards import Deck, Hand



def set_table(deck: Deck, dealer: Hand, player: Hand):

    dealer.add_one_card("down", deck.draw_one_card())
    player.add_one_card("up", deck.draw_one_card())
    dealer.add_one_card("up", deck.draw_one_card())
    player.add_one_card("up", deck.draw_one_card())

    dealer.display_hand()
    print(f"Dealer Score: {dealer.get_score()}")
    player.display_hand()
    print(f"Player Score: {player.get_score()}")


def main():
    deck = Deck()
    dealer = Hand()
    player = Hand()
    
    set_table(deck, dealer, player)
    

if __name__ == "__main__":
    main()