"""
This file handles most of the metrics in the application - variable setting and user input functions.
"""
from common import get_date_info, URGENCY_LEVELS
import re
import pandas as pd
import numpy as np

# -- DYNAMIC VALUES -- #

def get_triage_stats_per_day(date) -> dict:  # TODO: Create tests? Pytest
    patient_stats = {}

    for level in URGENCY_LEVELS:
        counter = df.loc[
            (df['Resultat av første triage'] == level)
            & (df['Ankomst'].dt.date == date.date())
        ]
        patient_stats[level] = len(counter)
    return patient_stats

def dict_to_np_array(dict):
    for key in dict:
        key

def triage_stats_per_hour(date) -> dict:
    pass


# -- USER INPUTS -- #

def user_date_prompt_to_timestamp() -> pd.Timestamp:
    """
    A top-level, nested function that prompts the user to input a month and date for data visualization.
    get_valid_month_day() -- Runs the input flow and validates it with simple RegEx, outputs month_input, day_input
    get_year_from_month_and_day() -- Calculates the year based on month and day input
    """
    def get_valid_month_day() -> tuple[int, int]:
        """ Runs user prompt and validates to regex pattern """
        while True:  # Month and day wrapper
            while True:  # Month
                print("Velg ønsket måned - to siffer (MM):\nEksempel: '03' for Mars.")
                _user_month_input = input("Måned: ")

                # RegEx match statement. Self-made pattern, passed all my tests, so should be good.
                regex_match_month = re.search(r"^(0[1-9]|1[0-2])$",_user_month_input)

                if regex_match_month is None:
                    print("Feil inntasting. Måned må være to siffer, og gyldig måned.\n")
                    continue
                month_input = int(regex_match_month.group())  # Extracts only matched string, converts to INT => Removes leading zeros
                break  # Month

            while True:  # Day
                print("Velg ønsket dato - to siffer (DD):\nEksempel: '18' for den attende i måneden.")
                _user_day_input = input("Dato: ")

                # No 30-31 validation as I did not find a reasonable way of doing this.
                regex_match_day = re.search(r"^(0[1-9]|[1-2][0-9]|3[0-1])$",_user_day_input)

                if regex_match_day is None:
                    print("Feil inntasting. Dato må være to siffer, og en gyldig dato.\n")
                    continue
                break  # Day
            day_input = int(regex_match_day.group()) # Extracts only matched string, converts to INT => Removes leading zeros
            break  # Wrapper
        return month_input, day_input

    def get_year_from_month_and_day(month_input, day_input) -> int:
        """Dataset is from 2024-03-10 to 2025-03-09. Year will be calculated accordingly"""

        if month_input > 3:
            calculated_year = 2024
        elif month_input < 3:
            calculated_year = 2025
        elif month_input == 3:
            calculated_year = 2025 if day_input <= 9 else 2024

        return calculated_year

    month, day = get_valid_month_day()
    year = get_year_from_month_and_day(month, day)

    timestamp = pd.Timestamp(f"{year}-{month}-{day}")
    return timestamp

