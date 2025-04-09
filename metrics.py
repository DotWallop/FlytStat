"""
This file handles most of the metrics in the application - variable setting and user input functions.
"""
import pandas as pd

from common import get_date_info

import re

# -- DYNAMIC VALUES -- #
# month_input, day_input = month_day_input()

def user_datemonth_input_to_datetime(day, month)
    """Dataset is from 2024-03-10 to 2025-03-09. Year will be calculated accordingly"""

    if month > 3


def get_triage_stats_per_day(): # TODO: Create tests? Pytest
    daily_patients_noturgent = df.loc[(df['Resultat av første triage'] == 'NotUrgent') & (df['Ankomst'].dt.date == )] # TODO: UNFINISHED



# -- USER INPUTS -- #

def month_day_input_to_datetime() -> pd.Timestamp:
    """
    A top-level, nested function that prompts the user to input a month and date for data visualization.
    get_valid_month_day() -- Runs the input flow and validates it with simple RegEx, outputs month_input, day_input
    get_year_from_month_and_day() -- Calculates the year based on month and day input
    """
    def get_valid_month_day():
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

    def get_year_from_month_and_day(month_input, day_input):
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



