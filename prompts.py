import os

def clean_screen():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")    

def display_income_help():
    print("--HELP--")
    print("exit: Return to main prompt")
    print("add: Add income entry")
    print("delete: Delete income entry")
    return

def display_expense_help():
    print("--HELP--")
    print("exit: Return to main prompt")
    print("add: Add expense entry")
    print("delete: Delete expense entry")
    return


def income_prompt():
    clean_screen()
    print("--Income--")
    print("Type 'help' to display commands")
    while True:
        try:
            command = input("> ")
            match command:
                case "help":
                    display_income_help()
                case "exit":
                    print("Quitting income menu...")
                    return
                case "add":
                    print("Not implemented yet.")
                    return
                case "delete":
                    print("Not implemented yet.")
                    return
                
        except KeyboardInterrupt:
            print("Quitting income menu...")
            return

def expense_prompt():
    clean_screen()
    print("--Expense--")
    print("Type 'help' to display commands")
    while True:
        try:
            command = input("> ")
            match command:
                case "help":
                    display_expense_help()
                case "exit":
                    print("Quitting expense menu...")
                    return
                case "add":
                    print("Not implemented yet.")
                    return
                case "delete":
                    print("Not implemented yet.")
                    return
                
        except KeyboardInterrupt:
            print("Quitting expense menu...")
            return 