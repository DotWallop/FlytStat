# import pandas as pd
# from plots import *


# === INIT ===
traceback.install(show_locals=True)

print("[bold cyan]Velkommen!\n\nVelg ønsket funksjon:[/]")
# List of function options. 
input_options = ("Søk opp statistikk", "Vis datagrunnlag")

# Indexes 'input_options' list using the enumerate function, starting at 1 to make the positions 1-based.
for index, value in enumerate(input_options, start=1):
    print(f"{index}:  {value}")

print()
print()
user_choice = int(input("Valg: "))

# While I could do this with an if/else statement, a match-case is more readable. Mapped into variables 
match user_choice:
    case 1:
        pass
        # Add another dialogue prompt for which plot the user wants
    
    case 2:
        pass
        # Add a function (in own function file?) that returns the metadata
        # Add meta info as an input option, min-max of source date column to see date range, number of patients, etc.

    case _:
        raise KeyError(f"{str(user_choice)} is not a valid entry.")
# Wrap entire pipeline in a while True-loop? Add a "return to main" within the subsections, that clears the terminal if possible?