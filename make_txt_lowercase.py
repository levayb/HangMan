def vmi():
    with open("name_word.txt", "r") as open_file:
        nevek = open_file.read
        return nevek 

nevek = vmi()
nevek = nevek.lower()
with open("name_word.txt" , "w") as open_file:
    open_file.write(nevek)
