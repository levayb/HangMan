import sys
import random
import os
import time
from asyncio.tasks import sleep


def exit_fuckin_funcion():
    os._exit()


def make_empty_letter_list(word):
    letter_list = []
    for i in range(len(word) - 1):
        letter_list.append("_")

    return letter_list


def cls():
    os.system("clear")


def scannin_word_for_letter(word, letter_list, letter):
    word_length = len(word)
    for i in range(word_length):
        if word[i] == letter:
            letter_list[i] = letter
    return letter_list


""" def select_game_language_menu():
    # A játék kezdő menüje, ahol zászlók közül kiválasztja a játékos a kívánt nyelvet a billenytyűzet nyilaival.
    # Fel és le lehet mozogni és egy hurok mutatja melyik menuponton vagyunk éppen.
    pass


def game_menu():
    # 1.) New game
    # 2.) Change game option
    # 3.) My score
    # 4.) Quit to main menu
    # 5.) Quit Game
    pass
 """

def welcome_msg():
    f = open("rope.txt", "r")
    rope = f.read()
    cls()
    print(rope)
    time.sleep(1)
    cls()
    f = open("i_wanna.txt", "r")
    wanna = f.read()
    print(wanna)
    user = input("Enter your Name: ")
    if user != "":
        print("\nHello", user, "What if I put a rope around your neck? ")
        print("\nIt's time to hang sombody!")
        time.sleep(1)
    else:
        f = open("evilsmile.txt", "r")
        evil = f.read()
        print(evil)
        print("\nHello random dude I a have a gift for ya! Somthing is missig around  your useless neck. We must fix that")
        print("\nIt's time to hang sombody!")
    time.sleep(1)


def game_rules():
    cls()
    print((12 * "\n"))
    rules = ('''\n\t\t\t\t\t\tLet's look at the rules:
    \n\t\t\t\t\t\t\tThis is a hang man game. So you can take 10 mistakes before you being hanged
    \n\t\t\t\t\t\t\tA word will be chosen at random and
    \n\t\t\t\t\t\t\tyou must try to guess the word correctly letter by letter
    \n\t\t\t\t\t\t\tbefore you run out of attempts. Good luck!''')
    print(rules)
    next_step = input("\n\t\t\t\t\t\t\tPress enter: ")


def winner_msg():
    with open("winner.txt", "r") as open_file:
        print(open_file.read())


def loose_msg():
    with open("rip.txt", "r") as open_file:
        print(open_file.read())


def file_switcher(choice):
    name = ""
    if choice == "1":
        name = "name_word.txt"
        return name
    elif choice == "2":
        name = "animals.txt"
        return name
    elif choice == "3":
        name = "python_commands.txt"
        return name


def choose_random_word(choice):
    filename = file_switcher(choice)
    with open(filename, "r") as open_file:
        words = []
        words = open_file.readlines()
        chosen = random.choice(words)
    return chosen


def user_input():
    user_letter_input = input("Guess a letter: ")
    save_user_input(user_letter_input)
    return user_letter_input


def save_user_input(user_input):
    with open("user_guess.txt", "a+") as open_file:
        open_file.write(user_input)


def load_previous_inputs():
    with open("user_guess.txt", "r") as open_file:
        guesses = open_file.read()
    return list(guesses)


def clear_input_buffer():
    with open("user_guess.txt", "w+") as open_file:
        open_file.write("")


def print_current_health_based_on_missing_healt(missing_health):
    health = 10 - missing_health
    with open("Health.txt", "r") as open_file:
        lines = open_file.readlines()
        print(lines[health])


def increase_missing_health(missing_health):
    missing_health += 1
    return missing_health


def letter_list_is_full(letter_list):
    for letter in letter_list:
        if letter == "_":
            return False
    return True



def print_current_hangman_parts(missing_health):

    if missing_health == 0:
        with open("hangman0.txt", "r") as open_file:
            print(open_file.read())

    elif missing_health == 1:
        with open("hangman1.txt", "r") as open_file:
            print(open_file.read())

    elif missing_health == 2:
        with open("hangman2.txt", "r") as open_file:
            print(open_file.read())

    elif missing_health == 3:
        with open("hangman3.txt", "r") as open_file:
            print(open_file.read())

    elif missing_health == 4:
        with open("hangman4.txt", "r") as open_file:
            print(open_file.read())

    elif missing_health == 5:
        with open("hangman5.txt", "r") as open_file:
            print(open_file.read())

    elif missing_health == 6:
        with open("hangman6.txt", "r") as open_file:
            print(open_file.read())

    elif missing_health == 7:
        with open("hangman7.txt", "r") as open_file:
            print(open_file.read())

    elif missing_health == 8:
        with open("hangman8.txt", "r") as open_file:
            print(open_file.read())

    elif missing_health == 9:
        with open("hangman9.txt", "r") as open_file:
            print(open_file.read())


def game_loop_pre_definitions(choice):
    choosen_word = choose_random_word(choice)
    original_letter_list = make_empty_letter_list(choosen_word)
    letter_list = make_empty_letter_list(choosen_word)
    missing_health = 0
    game_in_progress = True
    return game_in_progress, missing_health, letter_list, choosen_word, original_letter_list


def communicate_with_user_in_game_loop(missing_health, letter_list):
    print_current_health_based_on_missing_healt(missing_health)
    print("Used letters:", load_previous_inputs(), "\n")
    print(letter_list, "\n")
    print_current_hangman_parts(missing_health)
    print()
    input_character = user_input()
    cls()
    return input_character


def game_loop(game_in_progress, missing_health, letter_list,
              choosen_word, original_letter_list):
    while game_in_progress:

        input_character = communicate_with_user_in_game_loop(
            missing_health, letter_list)

        letter_list = scannin_word_for_letter(
            choosen_word, letter_list, input_character)

        if letter_list == original_letter_list:
            missing_health = increase_missing_health(missing_health)
        else:
            for i in range(0, len(letter_list)):
                original_letter_list[i] = letter_list[i]

        if missing_health >= 10:
            with open("hangman10.txt", "r") as open_file:
                print(open_file.read())
            time.sleep(1)
            cls()
            loose_msg()
            game_in_progress = False

        elif letter_list_is_full(letter_list):
            print(letter_list)
            winner_msg()
            game_in_progress = False
            time.sleep(1)


def start_a_new_game():
    os.system("clear")
    name = input("Enter your name:\n")
    if name == "":
        with open("random.txt", "r") as open_file:
            random_user_names = open_file.readlines()
        random_name = random.choice(random_user_names)
        print(random_name)
        with open("list_of_gamers.txt", "a") as open_file:
            open_file.write(random_name)
        return random_name
    else:
        with open("list_of_gamers.txt", "a") as open_file:
            open_file.write(name + "\n")
        return name


def select_game_language_menu():
    os.system("clear")
    pass


def main_menu_interface():
    print_menu = []
    with open("helloka.txt", "r") as f:
        hi = f.readlines()
        for line in hi:
            print_menu.append(("\t" * 6) + line.strip())
    print_menu.append("\n")
    print_menu.append(("\t" * 6) + "1.) Start a game with names" + "\t\t" + "👶" + "\n")
    print_menu.append(("\t" * 6) + "2.) Start a game with animals species" + "\t" + "👦" + "\n")
    print_menu.append(("\t" * 6) + "3.) Start a game with programmer words" + "\t" + "💀" + "\n")
    print_menu.append(("\t" * 6) + "4.) Rules" + "\n")
    print_menu.append(("\t" * 6) + "5.) Quit" + "\n")
    return print_menu


def print_menu_interface(menu):
    os.system("clear")
    print((13 * "\n"))
    for i in range(0, len(menu)):
        print(menu[i])


def user_choice():
    choice = input(("\t" * 6) + "Enter a number to select an option: ")
    return choice


def menu_choice():
    escape_progi = False
    while not escape_progi:
        clear_input_buffer()
        menu = main_menu_interface()
        print_menu_interface(menu)
        choice = user_choice()
        if choice == "1":
            os.system("clear")
            welcome_msg()
            game_in_progress, missing_health, letter_list, choosen_word, original_letter_list = game_loop_pre_definitions(choice)
            game_loop(game_in_progress, missing_health, letter_list, choosen_word, original_letter_list)

        elif choice == "2":
            os.system("clear")
            welcome_msg()
            game_in_progress, missing_health, letter_list, choosen_word, original_letter_list = game_loop_pre_definitions(choice)
            game_loop(game_in_progress, missing_health, letter_list, choosen_word, original_letter_list)

        elif choice == "3":
            os.system("clear")
            welcome_msg()
            game_in_progress, missing_health, letter_list, choosen_word, original_letter_list = game_loop_pre_definitions(choice)
            game_loop(game_in_progress, missing_health, letter_list, choosen_word, original_letter_list)

        elif choice == "4":
            os.system("clear")
            game_rules()

        elif choice == "5":
            escape_progi = True


def main():
    menu_choice()


if __name__ == '__main__':
    main()


# print(start_a_new_game())
""" print_menu_interface(menu)
key = getkey()
pointer = "👈"
 """
""" while:
    for i in range(0, len(menu)):
        if key == getkey.UP:
            menu.append("👈") """

# print("👈👈👈👈")
