# lib/cli.py

from helpers import (
    exit_program,
    list_divisions,
    find_division_by_id,
    list_division_fighters,
    find_fighter_by_id,
    update_fighter,
    delete_fighter,
    create_new_fighter,
    delete_division,
    create_new_division
)


def main():
    while True:

        menu()
        choice_1 = input("> ").upper()
        
        if choice_1 == "E":
            exit_program()
        
        #get into ufc_menu with the list of all current divisions
        elif choice_1 == "D":
            while True:
                divisions = list_divisions()
                ufc_menu()
                choice_2 = input("> ").upper()

                if choice_2 == "E":
                    exit_program()

                #get back to the previous menu
                elif choice_2 == "B":
                    break

                elif choice_2 == "A":
                    create_new_division()

                #check if user choose a valid division #
                elif choice_2.isdigit() and 1 <= int(choice_2) <= len(divisions):
                    division = find_division_by_id(int(choice_2))
                    #get into division_menu if a valid division number is chosen by user:
                    if division:
                        print(f'Welcome to {division.name}, division weight: {division.weight}. ' +
                                f"Please see the list of fighters below in this division") if division else print(f'Division {choice_2} not found')
                        while True:
                            all_fighters_in_this_division = division.fighters()
                            list_division_fighters(choice_2)
                            division_menu()
                            choice_3 = input("> ").upper()

                            #to exit the app
                            if choice_3 == "E":
                                exit_program() 
                            #to go back to previous menu
                            elif choice_3 =="B":
                                break
                            #check if user choose a valid fighter #
                            elif choice_3.isdigit() and 1 <= int(choice_3) <= len(all_fighters_in_this_division):
                                fighter = find_fighter_by_id(int(choice_2), int(choice_3))
                                if fighter:
                                    #if user chose a valid fighter#, get into fighter menu:
                                    while True:
                                        fighter_menu()
                                        choice_4 = input("> ").upper()

                                        #to exit the app
                                        if choice_4 == "E":
                                            exit_program()
                                        #to go back to previous menu (fighter list)
                                        elif choice_4 == "B":
                                            break  
                                        elif choice_4 == "U":
                                            update_fighter(int(choice_2), int(choice_3))
                                        elif choice_4 == "D":
                                            delete_fighter(int(choice_2), int(choice_3))
                                        else:
                                            print("Invalid choice")
                            #Add a new fighter into this division if user type "A"
                            elif choice_3 =="A":
                                create_new_fighter(int(choice_2))
                            #Delete the current division, if user type "D"
                            elif choice_3 =="D":
                                delete_division(int(choice_2))
                                break
                            else:
                                print("Invalid choice")
            
                #if user input is invalid
                else:
                    print("Invalid choice")
        else:
            print("Invalid choice")


def menu():
    print("*******************************************")
    print("Welcome to UFC division and fighter look up App !!")
    print("Please select an option:")
    print('To Exit the program, press "E"')
    print('To shown current divisions, press "D"')
    print("*******************************************")

def ufc_menu():
    print("*******************************************")
    print("Please select an option:")
    print('To Exit the program, press "E"')
    print('To select a division, press the correspoding tag number shown above')
    print('To add a new division to UFC, press "A"')
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
