from cards import Deck, Hand

deck = Deck()
dealer = Hand()
player = Hand()


dealer.add_one_card("down", deck.draw_one_card())
dealer.add_one_card("up", deck.draw_one_card())
dealer.add_one_card("up", deck.draw_one_card())

dealer.display_hand()

def calculate_score(hand: Hand):
    cards = hand.get_cards
