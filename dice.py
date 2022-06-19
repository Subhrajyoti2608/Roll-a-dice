import random
dice = True,

while dice:
    no=random.randint(1,6)
    if no == 1 :
        print("[-----]")
        print("[-----]")
        print("[  0  ]")
        print("[-----]")
        print("[-----]")
    if no == 2 :
        print("[-----]")
        print("[-----]")
        print("[0   0]")
        print("[-----]")
        print("[-----]")
    if no == 3 :
        print("[-----]")
        print("[-----]")
        print("[ 000 ]")
        print("[-----]")
        print("[-----]")
    if no == 4 :
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    if no == 5 :
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    if no == 6 :
        print("[-----]")
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
        print("[-----]")
    another_roll = input("Press y to roll again and n to exit: ")
    if another_roll.lower() == "y":
        continue
    else:
        break