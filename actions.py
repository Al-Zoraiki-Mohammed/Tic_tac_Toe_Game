"""
Module to manage a Tic Tac Toe game, including logging game details.

Functions:
    - log_fun(game_round=0, winner=""): Saves game logs to a file named 'logs_file.txt'.
    - play(): Controls the game rounds and players and calls 'game_logic' function.
    - view_win_log(): View win logs stored in 'logs_file.txt'.
    - clear_win_log(): Clear win logs stored in 'logs_file.txt'.
    - exit(): Shows an exit message when the user chooses to exit the game.
"""
from datetime import datetime
from logic import game_logic


def log_fun(game_round=0, winner=""):
    """
    Saves game logs to a file named 'logs_file.txt'

    Parameters:
        game_round (int): The round number of the game (default is 0).
        winner (str): The name of the winner (default is an empty string).

    Returns:
        str: A string containing the game round number and the winner's name.
    """
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open("logs_file.txt", 'a', encoding='utf-8') as file:
        file.write(f'At: {current_datetime}, Game Round: {game_round}, Winner: {winner}\n')
    return f"Game Round: {game_round}, Winner is: {winner}\n"


def play():
    """
    Controls the game rounds and players.
    Calls the game logic 'log_fun' function and receive the winner.

    Returns:
        None
    """
    first_player = input('Type first player name: ')
    second_player = input('Type second player name: ')
    play_again = 'y'

    game_round = 0
    while play_again.lower().strip() in ('y', 'yes', 'yep'):
        game_round += 1
        print(f'\nGame round {game_round} between {first_player} and {second_player} started !')
        winner = game_logic(first_player, second_player)
        print(f'Game round {game_round} between {first_player} and {second_player} Ended !')
        round_logs = log_fun(game_round, winner)
        print(round_logs)
        play_again = input('Do you wanna play again y/n: ')


def view_win_log():
    """
    View win logs stored in 'logs_file.txt'.

    Returns:
        None
    """
    print("view win log: ")
    is_empty = True
    with open("logs_file.txt", 'r', encoding='utf-8') as file:
        for line in file:
            print(line)
            is_empty = False
    if is_empty:
        print('No history yet, log empty  ..!')


def clear_win_log():
    """
    Clear win logs stored in 'logs_file.txt'.

    Returns:
        None
    """
    with open('logs_file.txt', 'w', encoding='utf-8'):
        pass
    print('win log has been cleared successfully ..!')


def exit_game():
    """
     -To show an exist message when user choose to exist.
     - Actual exist performed by break 'run_game' function.

     Returns:
        None
    """
    print()
    print("--" * 10 + "Exist game ! Good bye :)" + "--" * 10)
    print()
