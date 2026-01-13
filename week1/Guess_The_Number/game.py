import random
import json

# Highscore setup

highscore_file = "highscore.json"

# Checking if the json file exists
try:
    with open(highscore_file,"r") as file:
        data = json.load(file)
        highscore = data.get("highscore")
except:
    highscore = None

# Game setup

secret_number = random.randint(1,100)
attempts = 0
max_attempts = 6  

print("Welcome to Guess the number game!")
print("I'm thinking of a number between 1 and 50")
print(f"You have {max_attempts} number of attempts to guess the number and win")

# Game loop

while attempts < max_attempts:
    guess = (input("Enter your guess: "))

    #Cheat mode
    if guess.lower() == "cheat":
        print(f"ssshhh the secret number is {secret_number}")
        continue
    
    #Input validation to make sure the user enters a number
    try:    
        guess = int(guess)
    except ValueError:
        print("Invalid input! Please a number")
        continue

    attempts +=1

    # Guess evaluation
    if guess < secret_number:
        print("guess is too low")
    elif guess > secret_number:
        print("guess is too high")
    else:
        print(f"Congratulations! You guessed the number right in {attempts} attempts")

        # recording the highscore
        if highscore is None or attempts < highscore:
            highscore = attempts
            with open(highscore_file,"w") as file:
                json.dump({"highscore":highscore},file)
            print(f"New high score: {highscore} attempts!")
        break
else:
    print(f"You have used up all your attempts. The number was {secret_number}")





