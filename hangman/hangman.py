"""head_module."""
import random


class Game:
    """class game"""
    def __init__(self):
        self.hint_letters_global = []
        self.list_words = ["python", "java", "javascript", "php"]
        self.re_entry_arr = []
        self.number_of_attempts = 8

    def check_repeat_input(self, txt: str, write_letter=False):
        """check repeat input"""
        if txt in self.re_entry_arr:
            return True
        elif write_letter:
            self.re_entry_arr.append(txt)
            return None
        return False

    def clear_data(self, selected_word: list):
        """clear data"""
        self.hint_letters_global.clear()
        self.re_entry_arr.clear()
        return ['-' for _ in selected_word]

    def checking_input_letter(self, input_letter: str, selected_word: list):
        """check letters. check finish. write letter in hint"""
        for i, _ in enumerate(selected_word):
            if input_letter == selected_word[i] and self.hint_letters_global[i] != selected_word[i]:
                self.hint_letters_global[i] = selected_word[i]
            if ''.join(self.hint_letters_global) == selected_word:
                print(f"{'-' * 9}{selected_word}{'-' * 9}\nYou guessed the word!\nYou survived!")
                return

    def input_commands_and_letter(self, selected_word: list):
        """check commands or finish"""
        print(''.join(self.hint_letters_global))
        if ''.join(self.hint_letters_global) != selected_word:
            return input("Input a letter: >")

    def play_game(self):
        """head function"""
        selected_word = random.choice(self.list_words)
        self.hint_letters_global = Game().clear_data(selected_word)
        while True:
            input_letter = Game().input_commands_and_letter(selected_word)
            if self.number_of_attempts < 1:
                print("---You lost!---")
            elif input_letter == 'exit':
                return
            elif input_letter.isupper():
                print("Please enter a lowercase English letter.")
            elif len(input_letter) != 1:
                print("You should input a single letter.")
            elif Game().check_repeat_input(input_letter) and input_letter in selected_word:
                print("No improvements")
            elif Game().check_repeat_input(input_letter) and input_letter not in selected_word:
                print("You've already guessed this letter.")
            elif input_letter in selected_word:
                Game().checking_input_letter(input_letter, selected_word)
            else:
                print("That letter doesn't appear in the word :(")
                self.number_of_attempts -= 1
            Game().check_repeat_input(input_letter, True)


def start():
    """start game"""
    while True:
        print(f"{'-' * 20}HANGMAN{'-' * 20}")
        inp_txt = input('Type "play" to play the game, "exit" to quit: >')
        if inp_txt == "play":
            Game().play_game()
        elif inp_txt == "exit":
            print("Exit...")
            break


start()
