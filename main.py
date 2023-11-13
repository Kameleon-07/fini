import sqlite3
import os


HOME_PATH = os.getenv("HOME")
if(not os.path.isdir(f"{HOME_PATH}/fini")):
    os.makedirs(f"{HOME_PATH}/fini/")

income_db = sqlite3.connect(f'{HOME_PATH}/fini/income.db')
expenses_db = sqlite3.connect(f'{HOME_PATH}/fini/expenses.db')

command = ""

while True:
    try:
        command = input("> ")
    except KeyboardInterrupt:
        print("\rQuitting...")
        break

    
    if(command == "exit"):
        break
    print(command)