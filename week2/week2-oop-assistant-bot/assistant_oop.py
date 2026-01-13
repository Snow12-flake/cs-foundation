import time
import random

class Assistant:
    def __init__(self,name):
        self.name = name

    # method to tell the current time
    def tell_time(self):
        print("Current time: ",time.strftime("%H:%M:%S"))

    # method to tell a joke
    def tell_joke(self):
        jokes = ["Why did the cat join a band?Because it wanted to be a purr-cussionist!",
                 "What do you call a fake noodle? An impasta!",
                 "Why did the scarecrow win an award? Because he was outstanding in the field!",
                 "Why did the coffee file a police report? It got mugged!",
                 "Why do programmers hate nature? Too many bugs"]
        print(random.choice(jokes))

    # method to calculate an expression
    def calc(self):
        expression = input("Enter the expression: ")
        try:
            result = eval(expression)
            print("Result",result)
        except:
            print("Invaid expression")

    # displays the menu of commands
    def show_help(self):
        print("Available commands:")
        print("time - Show the current time")
        print("joke - tell a joke")
        print("calc - Calculate an expression")
        print("help - Show this menu")
        print("quit - Exit the bot")    # type quit to exit the bot

    def run(self):
        print(f"Hello, I am {self.name}")
        while True:
            cmd = input("How can i help you: ")
            if cmd.lower() == "quit":
                print("Goodbye!")
                break
            elif cmd == "time":
                self.tell_time()
            elif cmd == "joke":
                self.tell_joke()
            elif cmd == "expression":
                self.calc()
            elif cmd == "help":
                self.show_help()
            else:
                print("Unknown command. Type 'help' for options.")

assistant = Assistant("Kylie")
assistant.run()