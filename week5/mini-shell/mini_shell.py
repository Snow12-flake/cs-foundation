import os # Built-in module for basic OS tasks
import subprocess # Built-in module to run external commands

# Infinite loop = REPL keeps prompting until user quits
while True:

    # Prompt user for command
    cmd = input("mini-shell> ").strip() # strip whitespace

    # Exit conditions
    if cmd in ['exit', 'quit']:
        print(f"you've chosen to {cmd} the mini-shell")
        break

    parts = cmd.split() # Lets us access command name (parts[0]) and arguments (parts[1:])

    if not cmd:  # Skip empty imputs
        continue

    # Built in change directory function uses os.chdir to move around
    if parts[0] == 'cd':

        # try-except to handle errors like invalid path
        try:
            target = parts[1] 
            if len(parts) > 1:  #If path provided, use it
                target = parts[1]

            # No path? Go to home directory
            else :              
                target = os.path.expanduser("~")

            #Change the working directory
            os.chdir(target)
            print(f"Changed to {os.getcwd()}")  # = current working directory
        except Exception as e:
            print(f"cd error: {e}")

    # Buit in list directory function , Python alternative to os.listdir
    elif parts[0] == 'ls':
        try:
            for item in os.listdir('.'):
                print(item)
        except Exception as e :
            print(f"ls error: {e}")

    # Built in make directory 
    elif parts[0] == 'mkdir':
        try:
            os.mkdir(parts[1])
            print(f"Created {parts[1]}")
        except Exception as e:
            print(f"mkdir error: {e}")
        except FileExistsError:
            print(f"Error: {parts[1]} already exists")

    else:
        try:
            result = subprocess.run(parts, capture_output= True, text=True)

            # Print success output if any
            if result.stdout:
                print(result.stdout)

            # Print errors if command failed
            if result.stderr:
                print("Error:", result.stderr)

        except Exception as e:
            print(f"Command error: {e}")       

print("Mini shell shut down complete")