import sqlite3
import os

HOME_PATH = os.getenv("HOME")

def interpreter(command):
    # Command interpreting
    pass

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

    return fini_db, fini_cursor

def main():
    fini_db, fini_cursor = initialize_database()
    command = ""

    while True:
        try:
            command = input("> ")
        except KeyboardInterrupt:
            print("\rQuitting...")
            break
        finally:
            if(command == "exit"):
                break
        

if __name__ == "__main__":
    main()