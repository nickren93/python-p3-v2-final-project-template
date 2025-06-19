# Phase 3 Project: UFC Fighters & Divisions Look Up CLI

## Introduction

This is a simple command-line interface (CLI) application that allows a user on the current machine to create, read, update, and delete information about UFC divisions and fighters. The user can enter input as instructed by prompts. A CLI is essentially an interactive script that prompts the user and performs operations based on the input.

The directory structure of this application is shown below, starting from the root folder (python-p3-v2-final-project-template):

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   ├── division.py
    │   └── fighter.py
    ├── cli.py
    ├── debug.py
    ├── seed.py
    ├── menus.py
    └── helpers.py
└── ufc.db

```
The main functionality for these files is explained in the "CLI Files and Functions" section below..

---

## Getting Started & Environment Setup

From the project’s root directory, open your terminal and run the following commands to install dependencies and set up a virtual environment:

```console
pipenv install
pipenv shell
```

To start the CLI application, run the following commands:

```console
python lib/seed.py
python lib/cli.py
```
---

## CLI Files and Functions

To use the CLI, start with cli.py inside the lib folder.
Important: Run seed.py first to set up the database with some starter data.

The cli.py file imports functions from several modules, with the two key ones being menus.py and helpers.py.

---

### menus.py:
This file displays various menus to guide the user through the app.

**menu()**
    Displays the welcome and main instructions when the user first enters the CLI.

**ufc_menu()**
    Shown after the user types D in the main menu. Displays the list of divisions and related options.

**division_menu()**
    Displayed after the user selects a valid division tag number. Shows options for managing fighters and the division

**fighter_menu()**
    Shown after the user selects a valid fighter. Provides options to update or delete that fighter.

---

### helpers.py:

This file contains helper functions related to the Division and Fighter classes located in models/division.py and models/fighter.py. These helpers call ORM methods in the corresponding classes.

**exit_program()**
    Exits the program when the user enters E.

**list_divisions()**
    Lists all current divisions stored in the database.

**find_division_by_id(user_input)**
    Finds and displays a division by its ID, if valid.

**create_new_division()**
    Allows the user to create a new division (triggered by typing A in the UFC menu).

**delete_division(user_input)**
    Deletes a division from the database (available inside a division’s menu)..

**create_new_fighter(user_input)**
    Lets the user create a new fighter within a selected division.

**list_division_fighters(user_input)**
    Lists all fighters in a selected division.

**find_fighter_by_id(user_input1, user_input2)**
    Finds and displays a fighter based on division and fighter selection.

**update_fighter(user_input1, user_input2)**
    Updates a fighter’s information, including name, record, and division.

**delete_fighter(user_input1, user_input2)**
    Deletes a fighter from the database.

---

### seed.py

This script initializes the database and populates it with basic tables and sample data.
Run this before starting the CLI.

---

### menus.py:

This file together with lib/__init__.py help creating database and populate the database with 
some basic tables and data. Recommend to run this before using the cli.py.

---

### division.py

Defines the Division class, with properties, validation logic, and ORM methods to interact with the database and related fighters. 

---

### fighter.py

Defines the Fighter class, with properties, validation logic, and ORM methods to manage fighter data and their division relationship.

---

### __init__.py

Initializes the SQLite database connection and provides shared access to the connection and cursor throughout the app.

---

## Contributor
    Sitong Ren

---

## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
- [Click documentation](https://click.palletsprojects.com/en/stable/)
