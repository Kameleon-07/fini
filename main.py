import sqlite3
import os
import prompts

HOME_PATH = os.getenv("HOME")

def handle_command(command):
    command_parsed = command.split(" ")
    match command_parsed[0]:
        case "exit":
            exit(0)
        case "income":
            prompts.income_prompt()
            
        case "expense":
            prompts.expense_prompt()
        case _:
            return


def initialize_database(path=f'{HOME_PATH}/fini'):
    if(not os.path.isdir(path)):
        os.makedirs(path)

    fini_db = sqlite3.connect(f'{path}/fini.db')
    fini_cursor = fini_db.cursor()

    fini_cursor.execute('''
        CREATE TABLE IF NOT EXISTS INCOME (
            id INTEGER PRIMARY KEY,
            day,
            month,
            year,
            amount INTEGER,
            category TEXT
        )
        ''')
    fini_cursor.execute('''
        CREATE TABLE IF NOT EXISTS EXPENSE (
            id INTEGER PRIMARY KEY,
            day,
            month,
            year,
            amount INTEGER,
            category TEXT
        )
        ''')
    fini_db.commit()

    print(f"Using database at {path}/fini.db")

    return fini_db, fini_cursor

def main():
    fini_db, fini_cursor = initialize_database()
    command = ""

    while True:
        try:
            command = input("> ")
        except KeyboardInterrupt:
            print("\rQuitting...")
            return
        finally:
            interpreter(command)
        

if __name__ == "__main__":
    main()