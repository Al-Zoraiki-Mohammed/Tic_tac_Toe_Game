"""
This module is the entry point to the program(game).
This module should be run locally to start the game.

Functions:
    - run_game(): Runs a Tic Tac Toe game with a menu for different actions. 
    
"""
import actions


def run_game():
    """
    Runs a Tic Tac Toe game with a menu for different actions.

    Menu Options:
        1 --> Play: Starts a new game of Tic Tac Toe.
        2 --> View win log: Displays the log of previous game winners.
        3 --> Clear win log: Clears the log of previous game winners.
        4 --> Exit: Exits the game.

    Returns:
        None
    """
    menu_message = """
                    1 --> Play\n
                    2 --> View win log\n
                    3 --> Clear win log\n
                    4 --> Exit 
                    """
    while True:
        print(f"Tic Tac Toe game :) \n {menu_message}")
        choice = input("Type your choice: ")
        if choice.strip() == "1":
            actions.play()
        elif choice.strip() == "2":
            actions.view_win_log()
        elif choice.strip() == "3":
            actions.clear_win_log()
        elif choice.strip() == "4":
            actions.exit_game()
            break
        else:
            print(f"Sorry, {choice} is unknown choice! :(")


if __name__ == "__main__":
    run_game()
