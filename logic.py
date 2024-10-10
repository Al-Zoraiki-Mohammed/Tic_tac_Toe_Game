"""
This module contains the logic of the game with basic functionalities.
"""

import os

p = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}


def update_board():
    """
    Generates and returns a string representing the current state of
    the game board.

    Returns:
        str: A string representing the current game board with player positions
    """
    board = f"""
                -------------
                | {p[1]} | {p[2]} | {p[3]} |
                -------------
                | {p[4]} | {p[5]} | {p[6]} |
                -------------
                | {p[7]} | {p[8]} | {p[9]} |
                -------------
            """
    print(board)


def clean_screen():
    """
    Clears the terminal screen (Windows and Unix/Linux systems).
    Returns:
        None
    """
    os.system('cls' if os.name == "nt" else "clear")


def check_winners(first_player, second_player):
    """
    Checks for a winner.

    Parameters:
        first_player (str): The name of the first player.
        second_player (str): The name of the second player.

    Returns:
        tuple: A tuple containing the winner's name
                and a boolean indicating if the game is over.
    """
    if (p[1] == p[2] == p[3] == '+' or
            p[4] == p[5] == p[6] == '+' or
            p[7] == p[8] == p[9] == '+' or
            p[1] == p[4] == p[7] == '+' or
            p[2] == p[5] == p[8] == '+' or
            p[3] == p[6] == p[9] == '+' or
            p[1] == p[5] == p[9] == '+' or
            p[3] == p[5] == p[7] == '+'):
        return first_player, False
    elif (p[1] == p[2] == p[3] == '*' or
          p[4] == p[5] == p[6] == '*' or
          p[7] == p[8] == p[9] == '*' or
          p[1] == p[4] == p[7] == '*' or
          p[2] == p[5] == p[8] == '*' or
          p[3] == p[6] == p[9] == '*' or
          p[1] == p[5] == p[9] == '*' or
          p[3] == p[5] == p[7] == '*'):
        return second_player, False
    else:
        return "", True


def game_logic(first_player="me", second_player="you"):
    """
    - Simulates the game  between two players.
    - Manages the game flow, player turns and interact with players.

    Parameters:
        first_player (str): The name of the first player (default is "mama").
        second_player (str): The name of the second player (default is "nana").

    Returns:
        str: The outcome of the game - winner's name, draw, or quit.
    """
    vacancies = [i + 1 for i in range(9)]
    for i in vacancies:
        p[i] = str(i)
    update_board()
    is_game_running = True
    winner = ""
    while len(vacancies) > 0 and is_game_running:
        first = input(f"{first_player} turn, type place number or q to quit: ").strip()
        if first.isdigit():
            if int(first) in vacancies:
                p[int(first)] = '+'
                vacancies.remove(int(first))
                clean_screen()
                update_board()
            else:
                print('you lost your turn due to incorrect input :( ')
        elif first.lower() == 'q':
            return 'Quit game'
        else:
            print('you lost your turn due to incorrect input :( ')
        winner, is_game_running = check_winners(first_player, second_player)
        if not is_game_running or len(vacancies) == 0:
            break
        second = input(f"{second_player} turn, type place number or q to quit: ").strip()
        if second.isdigit():
            if int(second) in vacancies:
                p[int(second)] = '*'
                vacancies.remove(int(second))
                clean_screen()
                update_board()
            else:
                print('you lost your turn due to incorrect input :( ')
        elif second.lower() == 'q':
            return 'Quit game'
        else:
            print('you lost your turn due to incorrect input :( ')
        winner, is_game_running = check_winners(first_player, second_player)
        if not is_game_running or len(vacancies) == 0:
            break
    if len(vacancies) == 0 and is_game_running:
        return "Ends in a draw"
    else:
        return winner
