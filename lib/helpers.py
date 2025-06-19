# lib/helpers.py
from models.division import Division
from models.fighter import Fighter


def exit_program():
    print("Goodbye!")
    exit()

#division functions:
def list_divisions():
    divisions = Division.get_all()
    print("Please see all divisions list below:")
    for index, division in enumerate(divisions, start=1):
        print(f"{index}: {division.name}")
    return divisions

def find_division_by_id(user_input):
    # use a trailing underscore not to override the built-in id function
    division = Division.find_by_id(user_input)
    return division if division else print(f'Division {user_input} not found')


def create_new_division():
    name = input("Enter the new division name: ")
    weight = input("Enter the new division weight requirement(lbs): ")
    try:
        division= Division.create(name, weight)
        print(f'Successfully added new fighter: {division.name}')
    except Exception as exc:
        print("Error creating new division: ", exc)

def delete_division(user_input):
    if division := Division.find_by_id(user_input):
        division.delete()
        print(f'Department {user_input} deleted')
    else:
        print(f'Department {user_input} not found') 

#fighter functions:
def create_new_fighter(user_input):
    name = input("Enter the fighter's name: ")
    record = input("Enter the fighter's record: ")
    division_id = find_division_by_id(user_input).id
    try:
        fighter = Fighter.create(name, record, division_id)
        print(f'Successfully added new fighter: {fighter.name}')
    except Exception as exc:
        print("Error creating new fighter: ", exc)

def list_division_fighters(user_input):
    if division := Division.find_by_id(user_input):
        all_fighters_in_this_division = division.fighters()
        for index, fighter in enumerate(all_fighters_in_this_division, start=1):
            print(f"{index}: {fighter.name}")
    else:
        print(f'Division {user_input} not found')

def find_fighter_by_id(user_input1, user_input2):
    # use a trailing underscore not to override the built-in id function
    division = Division.find_by_id(user_input1)
    all_fighters_in_this_division = division.fighters()
    fighter = all_fighters_in_this_division[user_input2-1]
    print(f'Name: {fighter.name}, record: {fighter.record}.') if fighter else print(f'Fighter #{user_input2} not found')
    return fighter

def update_fighter(user_input1, user_input2):
    fighter = find_fighter_by_id(user_input1, user_input2)
    if fighter:
        try:
            name = input("Enter the fighter's new name: ")
            fighter.name = name
            record = input("Enter the fighter's new record: ")
            fighter.record = record
            division_name = input("Enter the fighter's new division name: ")
            division_id = Division.find_by_name(division_name).id
            fighter.division_id = division_id

            fighter.update()
            print(f'Successfuly update fighter: {fighter.name}')
        except Exception as exc:
            print("Error updating employee: ", exc)

    else:
        print(f'Fighter {user_input2} not found')

def delete_fighter(user_input1, user_input2):
    division = Division.find_by_id(user_input1)
    all_fighters_in_this_division = division.fighters()
    fighter = all_fighters_in_this_division[user_input2-1]
    if fighter:
        print(f'Fighter: {fighter.name} deleted')
        fighter.delete()
    else:
        print(f'Fighter {user_input2} not found')
