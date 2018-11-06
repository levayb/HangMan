import sys
import random
import os
from hangman import *

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
    print((14 * "\n"))
    print_menu.append(("\t" * 7) + "1.) Start a new game")
   # print_menu.append(("\t" * 7) + "2.) Continue")
    print_menu.append(("\t" * 7) + "2.) rules")
   # print_menu.append(("\t" * 7) + "4.) Credits")
    print_menu.append(("\t" * 7) + "3.) Quit")
    return print_menu

def print_menu_interface(menu):
    os.system("clear")
    for i in range(0, len(menu)):
        print(menu[i])

def menu_choice():
    menu = main_menu_interface()
    print_menu_interface(menu)
    choice = input()
    while True:
        if choice == "1":
            os.system("clear")
            welcome_msg()
            game_in_progress, missing_health, letter_list, choosen_word, original_letter_list = game_loop_pre_definitions()
            game_loop(game_in_progress, missing_health, letter_list, choosen_word, original_letter_list)
        elif choice == "2":
            os.system("clear")
            begining_part()

        elif choice == "3":
            break

menu_choice()
















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