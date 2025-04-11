"""
Main page, handles CLI choice logic
"""
import pages.statistics_page as sub_stats
main_page_choices = ("Vis statistikk", "Vis datagrunnlag")  # List of function options  TODO: If time: patient search? List patient from ID etc.
exit_option = len(main_page_choices) + 1  # Dynamically sets index for exit option
print("*"*18 + "\n     FlytStat     \n" + "*"*18)

while True:
    print("\nVelg ønsket funksjon:")
    print("—"*23)  # Horizontal seperator

    # Indexes 'input_options' list using the enumerate function, starting at 1 to make the positions 1-based.
    for index, value in enumerate(main_page_choices, start=1):
        print(f"[{index}]  {value}")
    print(f"[{exit_option}]  Avslutt")  # Dynamically set
    print("—"*23)  # Horizontal seperator

    try:
        user_choice = int(input("Valg: "))
    except ValueError:
        print(f"Ugyldig valg... Vennligst skriv inn et tall mellom 1 og {len(main_page_choices)}.")

    # While I could do this with an if/else statement, a match-case is more readable.
    match user_choice:
        case 1:
            sub_stats.run()
            input("Trykk på Enter-tasten for å returnere til menyen ...")  # A loop pause, preventing menu from automatically popping up

        case 2:
            print(2)
            input("Trykk på Enter-tasten for å returnere til menyen ...")  # A loop pause, preventing menu from automatically popping up
            # TODO: Add a function (in own function file?) that returns the metadata
            # TODO: Add meta info as an input option, min-max of source date column to see date range, number of patients, etc.

        case _ if user_choice == exit_option:  # After some trial and error I found this works, not sure if it is best practice.
            break
        case _:
            print(f"Ugyldig valg... Vennligst skriv inn et tall mellom 1 og {len(main_page_choices)}.")