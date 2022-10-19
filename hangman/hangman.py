"""head_module."""
import random


list_words = ["python", "java", "javascript", "php"]
hint_letters_global = []
re_entry_arr = []


def check_repeat_input(txt: str, write_letter=False):
    """check repeat input"""
    if txt in re_entry_arr:
        return True
    elif write_letter:
        re_entry_arr.append(txt)
        return None
    return False


def clear_data(selected_word: str):
    """clear data"""
    hint_letters_global.clear()
    re_entry_arr.clear()
    return ['-' for _ in selected_word]


def checking_input_letter(input_letter: str, selected_word: str):
    """check letters. check finish. write letter in hint"""
    for i, _ in enumerate(selected_word):
        if input_letter == selected_word[i] and hint_letters_global[i] != selected_word[i]:
            hint_letters_global[i] = selected_word[i]
        if ''.join(hint_letters_global) == selected_word:
            print(f"{'-'*9}{selected_word}{'-'*9}\nYou guessed the word!\nYou survived!")
            break


def input_commands_and_letter(selected_word: str):
    """check commands or finish"""
    if ''.join(hint_letters_global) != selected_word:
        print(''.join(hint_letters_global))
        return input("Input a letter: >")
    return True


def play_game(number_of_attempts: int):
    """head function"""
    global hint_letters_global
    selected_word = random.choice(list_words)
    hint_letters_global = clear_data(selected_word)
    while True:
        input_letter = input_commands_and_letter(selected_word)
        if number_of_attempts < 1:
            print("---You lost!---")
        elif input_letter == 'exit' or input_letter is True:
            return
        elif input_letter.isupper():
            print("Please enter a lowercase English letter.")
        elif len(input_letter) != 1:
            print("You should input a single letter.")
        elif check_repeat_input(input_letter) and input_letter in selected_word:
            print("No improvements")
        elif check_repeat_input(input_letter) and input_letter not in selected_word:
            print("You've already guessed this letter.")
        elif input_letter in selected_word:
            checking_input_letter(input_letter, selected_word)
        else:
            print("That letter doesn't appear in the word :(")
            number_of_attempts -= 1
        check_repeat_input(input_letter, True)


def start():
    """start game"""
    while True:
        print(f"{'-'*20}HANGMAN{'-'*20}")
        inp_txt = input('Type "play" to play the game, "exit" to quit: >')
        if inp_txt == "play":
            play_game(8)
        elif inp_txt == "exit":
            print("Exit...")
            break


start()
