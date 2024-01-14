def ask_move():
    while True:
        moves = ["hit", "stand", "h", "s"]
        user_input = input(f"Would you like to '(H)it' or '(S)tand'?").lower()
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
        user_input = input(f"How much $ would you like to bet? [0-{money}]:")# Press 'quit' to exit.")
        if user_input == "quit":
            exit()
        try:
            bet = int(user_input)
        except:
            break
        if 0 <= bet <= money: 
            return bet
        