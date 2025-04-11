

def run():
    stats_page_choices = (
        "Stablet stolpediagram -- Pasienter innlagt per time",  # TODO: Func name as comment
        "Sektordiagram -- Andel av symptomtype per døgn"
    )

    print("==  Tilgjengelig statistikk:  ==")

    for index, value in enumerate(stats_page_choices, start=1):
        print(f"[{index}]  {value}")

    print(f"[{len(stats_page_choices)+1}]  tilbake til hovedmeny ...")  # Dynamic return option


if __name__ == "__main__":  # Main guard, enables to run functions if it's ran from file
    run()