# lib/cli.py

from helpers import (
    exit_program,
    list_divisions,
    find_division_by_id,
    list_fighters,
)


def main():
    while True:
        menu()
        choice = input("> ").upper()
        if choice == "E":
            exit_program()
        elif choice == "D":
            list_divisions()
            division_menu()
            choice = input("> ").upper()
            if choice == "E":
                exit_program()
            elif choice == "1":
                find_division_by_id()
            elif choice == "B":
                pass
            else:
                print("Invalid choice")
        else:
            print("Invalid choice")


def menu():
    print("*******************************************")
    print("Please select an option:")
    print('To Exit the program, press "E"')
    print('To shown current divisions, press "D"')
    print("*******************************************")

def division_menu():
    print("*******************************************")
    print("Please select an option:")
    print('To Exit the program, press "E"')
    print('To select a division, press the correspoding tag number shown above')
    print('Go back to previous menu, press "B"')
    print("*******************************************")

def division_menu():
    print("*******************************************")
    print("Please select an option:")
    print('To Exit the program, press "E"')
    print('To select a division, press the correspoding tag number shown above')
    print("1. Shown detail about this division")
    print("2. Shown all fighters in current division")
    print("9. Return to main menu")
    print("*******************************************")


if __name__ == "__main__":
    main()
