name = input()
while name != "Welcome!":
    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    chek = len(name)
    if chek < 5:
        print(f"{name} goes to Gryffindor.")
    elif chek == 5:
        print(f"{name} goes to Slytherin.")
    elif chek == 6:
        print(f"{name} goes to Ravenclaw.")
    elif chek > 6:
        print(f"{name} goes to Hufflepuff.")
    name = input()
if name == "Welcome!":
    print("Welcome to Hogwarts.")
