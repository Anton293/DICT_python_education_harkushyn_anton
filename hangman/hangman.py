import random
import json

list_words = json.load(open('list_word.json'))
selected_word = random.choice(list_words)
hint_letters_local = []
re_entry_arrs = []
#######################################
def test_repeat_input(txt):
    if not txt in re_entry_arrs:
        re_entry_arrs.append(txt)
        return False
    else:
        return True


def progres_func():
    hint_letters_local.clear()
    re_entry_arrs.clear()
    for i in range(len(selected_word)):
        hint_letters_local.append("-")
#######################################

def play_game(number_of_attempts):
    progres_func()
    for i in range(99):
        if number_of_attempts < 1:
            print("---You lost!---")
            break
        elif ''.join(hint_letters_local) != selected_word:
            print(''.join(hint_letters_local))
            input_letter = input("Input a letter: >")
            if input_letter == 'menu' or input_letter == 'exit':
                break
            elif input_letter == '/fraund2022':
                print(selected_word)
        else:
            break

        if input_letter.isupper():
            print("Please enter a lowercase English letter.")
        elif len(input_letter) != 1:
            print("You should input a single letter.")
        elif test_repeat_input(input_letter):
            if input_letter in selected_word:
                print("No improvements")
            else:
                print("You've already guessed this letter.")
        elif input_letter in selected_word:
            for l in range(len(selected_word)):
                if input_letter == selected_word[l] and hint_letters_local[l] != selected_word[l]:
                    hint_letters_local[l] = selected_word[l]
                if ''.join(hint_letters_local) == selected_word:
                    print(f"{'-'*9}{selected_word}{'-'*9}\nYou guessed the word!\nYou survived!")
                    break
        else:
            print("That letter doesn't appear in the word")
            number_of_attempts -= 1


while True:
    print(f"{'-'*20}HANGMAN{'-'*20}")
    inp_txt = input('Type "play" to play the game, "exit" to quit: >')
    if inp_txt == "play":
        play_game(8)
    elif inp_txt == "exit":
        print("Exit...")
        break
