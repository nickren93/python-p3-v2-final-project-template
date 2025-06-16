# lib/cli.py

from helpers import (
    exit_program,
    list_divisions,
    find_division_by_id,
    list_division_fighters,
    find_fighter_by_id
)


def main():
    main_menu = True
    while main_menu:
        menu()
        choice_1 = input("> ").upper()
        if choice_1 == "E":
            exit_program()
        elif choice_1 == "D":
            list_divisions()
            ufc_menu()
            choice_2 = input("> ").upper()
            if choice_2 == "E":
                exit_program()
            #get into division_menu, if user choose a division #
            elif choice_2 == "1" or choice_2 == "2":
                if find_division_by_id(int(choice_2)):
                    list_division_fighters(choice_2)
                    division_menu()
                    choice_3 = input("> ").upper()
                    #to exit the app
                    if choice_3 == "E":
                        exit_program() 
                    #get into fighter_menu, if user choose a fighter #
                    elif choice_3 == "1" or choice_3 == "2" or choice_3 == "3":
                        if find_fighter_by_id(int(choice_2), int(choice_3)):
                            fighter_menu()
            #get back to the previous menu
            elif choice_2 == "B":
                pass
            #if user input is invalid
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

def ufc_menu():
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
    print('To select a fighter, press the correspoding tag number shown above')
    print('To add a new fighter to this division, press "A"')
    print('To delete this division, press "D"')
    print('Go back to previous menu, press "B"')
    print("*******************************************")

def fighter_menu():
    print("*******************************************")
    print("Please select an option:")
    print('To Exit the program, press "E"')
    print('To update info about this fighter, press "U"')
    print('To delete this fighter, press "D"')
    print('Go back to previous menu, press "B"')
    print("*******************************************")

if __name__ == "__main__":
    main()
