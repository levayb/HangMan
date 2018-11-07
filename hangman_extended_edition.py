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