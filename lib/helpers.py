# lib/helpers.py
from models.division import Division
from models.fighter import Fighter


def exit_program():
    print("Goodbye!")
    exit()

#division functions:
def list_divisions():
    divisions = Division.get_all()
    print("Performing useful function#1.")
    for index, division in enumerate(divisions, start=1):
        print(f"{index}: {division.name}")
def find_division_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ") - 1
    department = Division.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


#fighter functions:
