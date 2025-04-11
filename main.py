"""
Main page, handles CLI choice logic
"""
main_input_options = ("Søk opp statistikk", "Vis datagrunnlag")  # List of function options  TODO: If time: patient search? List patient from ID etc.
EXIT_OPTION = len(main_input_options) + 1  # Dynamically sets index for exit option into constant
print(" == FlytStat ==\n\nVelg ønsket funksjon:")


# Indexes 'input_options' list using the enumerate function, starting at 1 to make the positions 1-based.
for index, value in enumerate(main_input_options, start=1):
    print(f"[{index}]  {value}")
print(f"[{len(main_input_options)+1}]  Avslutt ...")  # Dynamically set

print()
print()
user_choice = int(input("Valg: "))

# While I could do this with an if/else statement, a match-case is more readable.
match user_choice:
    case 1:
        print(1)
        # Add another dialogue prompt for which plot the user wants
    
    case 2:
        print(2)
        # Add a function (in own function file?) that returns the metadata
        # Add meta info as an input option, min-max of source date column to see date range, number of patients, etc.

    case EXIT_OPTION:
        print("Bye!")
    case _:
        raise KeyError(f"{str(user_choice)} is not a valid entry.")
# Wrap entire pipeline in a while True-loop? Add a "return to main" within the subsections, that clears the terminal if possible?