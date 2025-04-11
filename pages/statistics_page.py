

def run():
    while True:
        stats_page_choices = ("Stablet stolpediagram -- Pasienter innlagt per time",  # TODO: Func name as comment
                              "Sektordiagram -- Andel av symptomtype per døgn"
                              )
        exit_option = len(stats_page_choices) + 1

        print("==  Tilgjengelig statistikk:  ==\n")
        print("—" * 56)  # Horizontal seperator
        for index, value in enumerate(stats_page_choices, start=1):
            print(f"[{index}]  {value}")
        print(f"[{exit_option}]  Tilbake til hovedmeny")  # Dynamic return option
        print("—" * 56)  # Horizontal seperator
        try:  # Gentle error handling for invalid inputs
            user_choice = int(input("Valg: "))
        except ValueError:
            print(f"Ugyldig valg... Vennligst skriv inn et tall mellom 1 og {len(stats_page_choices)}.")

        match user_choice:
            case 1:
                pass
                input("Trykk på Enter-tasten for å returnere til menyen ...")  # A loop pause, preventing menu from automatically popping up

            case 2:
                pass
                input("Trykk på Enter-tasten for å returnere til menyen ...")  # A loop pause, preventing menu from automatically popping up

            case _ if user_choice == exit_option:
                break
            case _:
                raise KeyError(f"Ugyldig valg... Vennligst skriv inn et tall mellom 1 og {len(stats_page_choices)}.")

if __name__ == "__main__":  # Main guard, enables to run functions if it's ran from file
    run()