"""
Main page, handles CLI choice logic.
Staggered import to ensure proper handling of dependencies (lazy loading concept)
"""
from common import HASHED_SHEET_PATH
import pages.statistics_page as sub_stats
import pages.metadata_page as meta_page
import scripts.npr_hashing as hash_script

main_page_choices = ("Vis statistikk", "Vis datagrunnlag")  # List of function options
exit_option = len(main_page_choices) + 1  # Dynamically sets index for exit option
print("*"*18 + "\n     FlytStat     \n" + "*"*18)

if not HASHED_SHEET_PATH.exists():
    print("Finner ikke en gyldig krypteringsnøkkel.\nKjører førstegangsoppsett...")
    hash_script.hash_aliases_from_excel()  # Runs the hashing script.

from data_processing import load_data
df, SYMPTOM_COLUMNS = load_data()  # Lazy loads the dataframe.

while True:
    print("\nVelg ønsket funksjon:")
    print("—"*23)  # Horizontal seperator

    # Indexes 'input_options' list using the enumerate function, starting at 1 to make the positions 1-based.
    for index, value in enumerate(main_page_choices, start=1):
        print(f"[{index}]  {value}")
    print(f"[{exit_option}]  Avslutt")  # Dynamically set
    print("—"*23 + "\n")  # Horizontal seperator

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
            meta_page.run()
            input("Trykk på Enter-tasten for å returnere til menyen ...")  # A loop pause, preventing menu from automatically popping up

        case _ if user_choice == exit_option:  # After some trial and error I found this works, not sure if it is best practice.
            break
        case _:
            print(f"Ugyldig valg... Vennligst skriv inn et tall mellom 1 og {len(main_page_choices)}.")
