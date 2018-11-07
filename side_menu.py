def select_lenguage():
    print_menu = []
    with open("helloka.txt", "r") as f:
        hi = f.readlines()
        for line in hi:
            print_menu.append(("\t" * 6) + line.strip())
    print_menu.append("\n")
    print_menu.append(("\t" * 6) + "1.) English" + "\t\t" + "english flag" + "\n")
    print_menu.append(("\t" * 6) + "2.) Magyar" + "\t" + "magyar zászló" + "\n")
    return print_menu

def hungarian_menu():
    print_menu = []
    with open("helloka.txt", "r") as f:
        hi = f.readlines()
        for line in hi:
            print_menu.append(("\t" * 6) + line.strip())
    print_menu.append("\n")
    print_menu.append(("\t" * 6) + "1.) Játék indítás nevekkel" + "\t\t" + "👶" + "\n")
    print_menu.append(("\t" * 6) + "2.) Játék indítás állat névvel" + "\t" + "👦" + "\n")
    print_menu.append(("\t" * 6) + "3.) Játék indítás népies szavak" + "\t" + "💀" + "\n")
    print_menu.append(("\t" * 6) + "4.) Szabályok" + "\n")
    print_menu.append(("\t" * 6) + "5.) Kilépés" + "\n")
    return print_menu


def communicate_with_user_in_game_loop(missing_health, letter_list):
    print_current_health_based_on_missing_healt(missing_health)
    print("Használt betűk:", load_previous_inputs(), "\n")
    print(letter_list, "\n")
    print_current_hangman_parts(missing_health)
    print()
    input_character = user_input()
    cls()
    return input_character


def user_input():
    user_letter_input = input("Írj egy betűt: ")
    save_user_input(user_letter_input)
    return user_letter_input

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
    user = input("Add meg a neved: ")
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



def szabályzat():
    cls()
    print((12 * "\n"))
    rules = ('''\n\t\t\t\t\t\tNézzük a szabályokat:
    \n\t\t\t\t\t\t\tEz egy akasztófa játék. 10 hibázási lehetőséged van mielőtt felakasztanak!
    \n\t\t\t\t\t\t\tA kitalálandó szó véletlenszerűen lesz kiválasztva az általad választott játékmód szerint.
    \n\t\t\t\t\t\t\tTippelj pontosan és bölcsen betűről betűre, mielőtt kifutsz a lehetőségeidből. 
    \n\t\t\t\t\t\t\tSok szerencsét! ''')
    print(rules)
    next_step = input("\n\t\t\t\t\t\t\tPress enter: ")