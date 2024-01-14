def ask_move() -> str:
    while True:
        moves = ["hit", "stand", "h", "s"]
        user_input = input(f"Would you like to '(H)it' or '(S)tand'?") \
            .lower().strip()
        if user_input in ["quit", "q"]:
            exit()
        if user_input in moves:
            if user_input in ["hit", "h"]:
                return "hit"
            elif user_input in ["stand", "s"]:
                return "stand"
            print("Invalid input.")
            
            
def ask_bet(money: int) -> int:
    while True:
        print(f"You have ${money} available to play.")
        user_input = input(f"How much $ would you like to bet? [0-{money}]:") \
            .lower().strip()
        if user_input == "quit":
            exit()
        try:
            bet = int(user_input)
        except:
            continue
        if bet >= 0:
            if bet <= money: 
                return bet
        
