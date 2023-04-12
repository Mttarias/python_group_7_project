import sys


def menu():
    choice = 0
    while choice < 1 or choice > 4:
        print("""
        1. Text Adventure
        2. Dice
        3. Rock Paper Scissor
        4. Exit
        """)

        choice = int(input("Enter your selection: "))
        match choice:
            case 1:
                #function, remove break
                break
            case 2:
                #function, remove break
                break
            case 3:
                #function, remove break
                break
            case 4:
                sys.exit("Goodbye.")
            case _:
                print("Please make a valid selection")