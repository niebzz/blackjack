def ask_move():
    while True:
        moves = ["hit", "stand", "h", "s"]
        user_input = input(f"Would you like to '(H)it' or '(S)tand'? Press 'quit' to exit:").lower()
        if user_input in ["quit", "q"]:
            exit()
        if user_input in moves:
            if user_input in ["hit", "h"]:
                return "hit"
            elif user_input in ["stand", "s"]:
                return "stand"
            print("Invalid input.")