import time
import random

# function to tell the current time
def tell_time():
    print("Current time: ",time.strftime("%H:%M:%S"))

# function to tell a joke
def tell_joke():
    jokes = ["Why did the cat join a band?Because it wanted to be a purr-cussionist!","What do you call a fake noodle? An impasta!","Why did the scarecrow win an award? Because he was outstanding in the field!","Why did the coffee file a police report? It got mugged!"]
    print(random.choice(jokes))

# function to calculate an expression
def calc():
    expression = input("Enter the expression: ")
    try:
        result = eval(expression)
        print("Result",result)
    except:
        print("Invaid expression")

# displays the menu of commands
def show_help():
    print("Available commands:")
    print("time - Show the current time")
    print("joke - tell a joke")
    print("calc - Calculate an expression")
    print("help - Show this menu")
    print("quit - Exit the bot")    # type quit to exit the bot

# assistant bot REPL loop
while True:
    cmd = input("enter Command: ")
    if cmd.lower() == "quit":
        print("Goodbye!")
        break
    elif cmd == "time":
        tell_time()
    elif cmd == "joke":
        tell_joke()
    elif cmd == "expression":
        calc()
    elif cmd == "help":
        show_help()
    else:
        print("Unknown command. Type 'help' for options.")