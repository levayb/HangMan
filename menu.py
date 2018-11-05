import sys
import random
import os

def start_a_new_game():
    os.system("clear")
    name = input("Enter your name:\n")
    if name == "":
        with open("random.txt", "r") as open_file:
            random_user_names = open_file.readlines()
        random_name = random.choice(random_user_names)
        print(random_name)
        with open("list_of_gamers.txt", "a") as open_file:
            open_file.write(random_name + "\n")
        return random_name
    else:
        with open("list_of_gamers.txt", "a") as open_file:
            open_file.write(name + "\n")
        return name

print(start_a_new_game())