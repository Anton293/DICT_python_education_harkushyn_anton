"""rock paper scissors"""

import itertools
from random import randint


def kill(player_choice: str, choice_other_player: str, arr: list) -> bool:
    """Check if the player_choice beats the choice_other_player

    Parameters:
    player_choice (str): The choice of the player
    choice_other_player (str): The choice of the other player
    arr (list): The list of choices

    Returns:
    bool: True if the player_choice beats the choice_other_player, False otherwise
    """
    i = 0
    arr = arr[::-1]
    double_arr = arr + arr
    for killer, victim in itertools.combinations(double_arr, 2):
        if killer == player_choice and i <= int((len(arr) / 2)) - 1:
            i += 1
            if victim == choice_other_player:
                return True
    return False


def check_commands(selected_user: str, count_player: int) -> bool:
    """Check if the user input is a command

    Parameters:
    selected_user (str): The input of the user
    count_player (int): The score of the player

    Returns:
    bool: True if the user input is a command, False otherwise
    """
    if selected_user == "!exit":
        print("Bye!")
        exit(0)
    elif selected_user == "!rating":
        print(f"Your rating: {count_player}")
        return True
    return False


def check_input_user(selected_user: str, items_array: list):
    """Check if the user input is a valid choice

    Parameters:
    selected_user (str): The input of the user
    items_array (list): The list of choices

    Returns:
    Union[str, bool]: The selected_user if it is a valid choice, False otherwise
    """
    if selected_user in items_array:
        return selected_user
    return False


def read_file(key: str) -> int:
    """Read the score of the player from the rating.txt file

    Parameters:
    key (str): The name of the player

    Returns:
    int: The score of the player, 0 if the player is not in the file
    """
    try:
        with open("rating.txt") as f:
            for line in f:
                name, score = line.split()
                if name == key:
                    return int(score)
    except FileNotFoundError:
        print("Rating file not found. Starting with default rating of 0.")
        return 0
    except ValueError:
        print("Rating file is corrupt. Starting with default rating of 0.")
        return 0
    return 0


def game(user: str, items_array: list) -> None:
    """The main function of the game

    Parameters:
    user (str): The name of the player
    items_array (list): The list of choices
    """
    count_player = read_file(user)
    while True:
        selected_user = input(">")
        if check_commands(selected_user, count_player):
            continue
        if not check_input_user(selected_user, items_array):
            print("Invalid input")
            continue

        computer_choice = items_array[randint(0, len(items_array) - 1)]
        if kill(computer_choice, selected_user, items_array):
            print(f"Sorry, but the computer chose <{computer_choice}>")
        elif kill(selected_user, computer_choice, items_array):
            print(f"Well done. The computer chose <{computer_choice}> and failed")
            count_player += 100
        else:
            print(f"There is a draw ({computer_choice})")
            count_player += 50


def main():
    """begin function init game"""
    user = input('Enter your name: ')
    print(f"Hello, {user}")
    if len(role := input("Install value >")) <= 1:
        role = ["paper", "scissors", "rock"]
    else:
        role = role.split(",")
    
    count_victim = int((len(role) / 2))
    print(*role, sep=f' {"<"*count_victim} ')
    print("Okay, let's start.")
    game(user, role)


if __name__ == '__main__':
    main()
