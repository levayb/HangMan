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
    user = input(texts[LANG]["welcome_msg input"])
    if user != "":
        print(texts[LANG]["welcome_msg pritn1.1"], user, texts[LANG]["welcome_msg pritn1.2"])
        print(texts[LANG]["rule print 2"])
        next_step = input(texts[LANG]["next step"])
    else:
        f = open("evilsmile.txt", "r")
        evil = f.read()
        print(evil)
        print(texts[LANG]["rule print 3"])
        print(texts[LANG]["rule print 4"])
        next_step = input(texts[LANG]["next step"])


def game_rules():
    cls()
    print((13 * "\n"))
    with open("helloka.txt", "r") as f:
        hi = f.readlines()
        for line in hi:
            print(("\t" * 6) + line.strip())
    print("\n")
    print("\t" * 6 + texts[LANG]["rule print 1"] + "\n")
    print("\t" * 6 + texts[LANG]["rule print 2"] + "\n")
    print("\t" * 6 + texts[LANG]["rule print 3"] + "\n")
    print("\t" * 6 + texts[LANG]["rule print 4"] + "\n")
    print("\t" * 6 + texts[LANG]["rule print 5"] + "\n")
    next_step = input("\t" * 6 + texts[LANG]["next step"] + "\n")


def winner_msg():
    with open("winner.txt", "r") as open_file:
        print(open_file.read())


def loose_msg():
    with open("rip.txt", "r") as open_file:
        print(open_file.read())


def file_switcher(choice):
    name = ""
    if choice == "1":
        name = texts[LANG]["choice1"]
        return name
    elif choice == "2":
        name = texts[LANG]["choice2"]
        return name
    elif choice == "3":
        name = texts[LANG]["choice3"]
        return name


def choose_random_word(choice):
    filename = file_switcher(choice)
    with open(filename, "r") as open_file:
        words = []
        words = open_file.readlines()
        chosen = random.choice(words)
    return chosen


def user_input():
    user_letter_input = input(texts[LANG]["letter input"])
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
    print(texts[LANG]['used letters'], load_previous_inputs(), "\n")
    print(letter_list, "\n")
    print_current_hangman_parts(missing_health)
    print()
    input_character = user_input()
    cls()
    return input_character


def game_loop(game_in_progress, missing_health, letter_list,
              choosen_word, original_letter_list, user_choice):
    cls()
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
            print(texts[LANG]["game word"])
            print(choosen_word)
            time.sleep(2)
            cls()
            loose_msg()
            game_in_progress = False
            time.sleep(2)

        elif letter_list_is_full(letter_list):
            print(letter_list)
            winner_msg()
            game_in_progress = False
            time.sleep(2)


# def start_a_new_game():
#     os.system("clear")
#     name = input("Enter your name:\n")
#     if name == "":
#         with open("random.txt", "r") as open_file:
#             random_user_names = open_file.readlines()
#         random_name = random.choice(random_user_names)
#         print(random_name)
#         with open("list_of_gamers.txt", "a") as open_file:
#             open_file.write(random_name)
#         return random_name
#     else:
#         with open("list_of_gamers.txt", "a") as open_file:
#             open_file.write(name + "\n")
#         return name


def main_menu_interface():
    print_menu = []
    with open("helloka.txt", "r") as f:
        hi = f.readlines()
        for line in hi:
            print_menu.append(("\t" * 6) + line.strip())
    print_menu.append("\n")
    print_menu.append("\t" * 6 + "1.) " + texts[LANG]["menu1"] + "\t" + "👨" + "\n")
    print_menu.append("\t" * 6 + "2.) " + texts[LANG]["menu2"] + "\t" + "🦁" + "\n")
    print_menu.append("\t" * 6 + "3.) " + texts[LANG]["menu3"] + "\t" + texts[LANG]["emoji"] + "\n")
    print_menu.append("\t" * 6 + "4.) " + texts[LANG]["menu4"] + "\n")
    print_menu.append("\t" * 6 + "5.) " + texts[LANG]["menu5"] + "\n")
    return print_menu


def print_menu_interface(menu):
    os.system("clear")
    print((13 * "\n"))
    for i in range(0, len(menu)):
        print(menu[i])


def user_choice():
    choice = input("\t" * 6 + texts[LANG]["select option"])
    return choice


def menu_choice(LANGuage_choise):
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
            game_loop(game_in_progress, missing_health, letter_list, choosen_word, original_letter_list, choice)

        elif choice == "2":
            os.system("clear")
            welcome_msg()
            game_in_progress, missing_health, letter_list, choosen_word, original_letter_list = game_loop_pre_definitions(choice)
            game_loop(game_in_progress, missing_health, letter_list, choosen_word, original_letter_list, choice)

        elif choice == "3":
            os.system("clear")
            welcome_msg()
            game_in_progress, missing_health, letter_list, choosen_word, original_letter_list = game_loop_pre_definitions(choice)
            game_loop(game_in_progress, missing_health, letter_list, choosen_word, original_letter_list, choice)

        elif choice == "4":
            os.system("clear")
            game_rules()

        elif choice == "5":
            escape_progi = True

def LANGuage_switcher():
    print_LANGuage_menu = []
    with open("helloka.txt", "r") as f:
        hi = f.readlines()
        for line in hi:
            print_LANGuage_menu.append(("\t" * 6) + line.strip())
    print_LANGuage_menu.append("\n")
    print_LANGuage_menu.append("\t" * 6 + "1.)English       " + "🇬🇧" + "\n")
    print_LANGuage_menu.append("\t" * 6 + "2.)Magyar        " + "🇭🇺" + "\n")
    return print_LANGuage_menu

def print_LANGuage_interface(menu):
    os.system("clear")
    print((13 * "\n"))
    for i in range(0, len(menu)):
        print(menu[i])


def select_input():
    select = input("\t" * 6 + "Choose\Válassz: ")
    return select


def LANGuage_choise():
    escape_menu = False
    while not escape_menu:
        menu = LANGuage_switcher()
        print_LANGuage_interface(menu)
        select = input("\t" * 6 + "Choose\Válassz: ")
        if select == "3":
            menu_choice(LANG)
        else:
            return select


def main():
    global LANG
    print_LANGuage_interface(LANGuage_switcher())
    inputka = select_input()
    if inputka == "1":
        LANG = "eng"
    elif inputka == "2":
        LANG = "hun"
    print_LANGuage_interface(LANGuage_switcher())
    menu_choice(LANG)


LANG = ""

texts = {
    'hun': {
        'menu1': 'Játék indítás nevekkel',
        'menu2': 'Játék indítás állat névvel',
        'menu3': 'Játék indítás népies szavak',
        'emoji': '🏡',
        'menu4': 'Szabályok',
        'menu5': 'Kilépés',
        'used letters': 'Használt betűk:',  # 201
        'select option': 'Add meg a kívánt menüpont számát: ',
        'letter input': 'Írj egy betűt: ',  # 104. sor
        'choice1': 'nevek.txt',  # 86.sor
        'choice2': 'állatok.txt',  # 89.sor
        'choice3': 'népies.txt',  # 92.sor
        'next step': 'Nyomj entert: ',  # 70.sor
        'rule print 1': 'Nézzük a szabályokat:',  # 64.sor
        'rule print 2': 'Ez egy akasztófa játék. 10 hibázási lehetőséged van mielőtt felakasztanak!',  # 65.sor
        'rule print 3': 'A kitalálandó szó véletlenszerűen lesz kiválasztva az általad választott játékmód szerint.',  # 66.sor
        'rule print 4': 'Tippelj pontosan és bölcsen betűről betűre, mielőtt kifutsz a lehetőségeidből.',  # 67.sor
        'rule print 5': 'Sok szerencsét!',  # 68.sor
        'welcome_msg input': 'Add meg a neved: ',  # 42.sor
        'welcome_msg pritn1.1': '\nSzia',  # 44.sor
        'welcome_msg pritn1.2': 'mit szólnál, ha az idei divat szerint a nyakad köré tennénk egy kötelet?',  # 44.sor
        'welcome_msg pritn2': '\nItt az idő felkötni valakit!',  # 44.sor
        'welcome_msg pritn3': '\nÜdvözöllek idegen van egy ajándékom számodra!\nValami hianyzik arról a haszontalan nyakaról.',  # 51.sor
        'welcome_msg pritn4': '\nEzt surgősen korrigálnunk kell!😈😈😈\nItt az idő felavatni az új kötelet!',  # 52.sor
        'game word': 'Ezt kellett volna kitalálni 😈😈😈😈😈😈',
    },


    'eng': {
        'menu1': 'Start a game with names\t',
        'menu2': 'Start a game with animals species',
        'menu3': 'Start a game with programmer words',
        'emoji': '🐍',
        'menu4': 'Rules',
        'menu5': 'Quit',
        'used letters': 'Used letters:',  # 201
        'select option': 'Enter a number to select an option: ',
        'letter input': 'Guess a letter: ', #104
        'choice1': 'name_word.txt', #86
        'choice2': 'animals.txt',
        'choice3': 'python_commands.txt',
        'next step': 'Press enter:',
        'rule print 1': "Let's look at the rules:",
        'rule print 2': 'This is a hang man game. So you can take 10 mistakes before you being hanged',
        'rule print 3': 'A word will be chosen at random and',
        'rule print 4': 'you must try to guess the word correctly letter by letter',
        'rule print 5': 'before you run out of attempts. Good luck!',
        'welcome_msg input': 'Enter your Name: ',
        'welcome_msg pritn1.1': '\nHello',
        'welcome_msg pritn1.2': 'What if I put a rope around your neck?',
        'welcome_msg pritn2': "\nIt's time to hang sombody!",
        'welcome_msg pritn3': '\nHello random dude I a have a gift for ya! Somthing is missig around  your useless neck. We must fix that',
        'welcome_msg pritn4': "\nIt's time to hang sombody!",
        'game word': 'This is what you had to know!😈😈😈😈😈😈',
    }
}

if __name__ == '__main__':
    main()
