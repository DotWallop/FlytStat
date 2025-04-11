"""
This file handles most of the metrics in the application - variable setting and user input functions.
"""
from common import URGENCY_LEVELS
import re
import pandas as pd

def user_date_prompt_to_timestamp() -> pd.Timestamp:
    """
    A top-level, nested function that prompts the user to input a month and date for data visualization.
    get_valid_month_day() -- Runs the input flow and validates it with simple RegEx, outputs month_input, day_input
    get_year_from_month_and_day() -- Calculates the year based on month and day input
    :returns: pd.Timestamp object from user prompt
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
    print(f"Dato valgt:  {timestamp.strftime('%d. %B %Y')}")  # Console confirmation output
    return timestamp


def get_triage_stats_per_unit(df, date, datetime_prop='date') -> dict:  # TODO: Create tests? Pytest
    triage_count_stats = {}

    if datetime_prop == 'hour': # TODO: Refactor, should be day?
        for hour in range(24):
            hourly_stats = {}
            for level in URGENCY_LEVELS:
                counter = df.loc[
                    (df['Resultat av første triage'] == level)
                    & (df['Ankomst'].dt.date == date.date())
                    & (df['Ankomst'].dt.hour == hour)
                ]
                hourly_stats[level] = len(counter)
            triage_count_stats[hour] = hourly_stats
        return triage_count_stats

    else:
        for level in URGENCY_LEVELS:
            counter = df.loc[
                (df['Resultat av første triage'] == level)
                & (df['Ankomst'].dt.date == date.date())
            ]
            triage_count_stats[level] = len(counter)
        return triage_count_stats

def get_symptom_stats_by_date(df, symptom_columns, date) -> dict:
    symptom_count = {}
    for symptom in symptom_columns:
        patients_per_day = df.loc[(df[symptom] == 'X') & (df['Ankomst'].dt.date == date.date())]
        symptom_count[symptom] = len(patients_per_day)
    sorted_symptom_count = dict(sorted(symptom_count.items(), key=lambda item: item[1], reverse=True))  # Helped build by plt docs
    return sorted_symptom_count

def convert_counts_to_relative_size(sorted_symptom_count: dict):
    total_patients = sum(sorted_symptom_count.values())
    if total_patients == 0:  # Prevents dividing by zero.. ;-)
        return {symptom: 0 for symptom in sorted_symptom_count}
    relative_number_of_patients = {symptom: count / total_patients for symptom, count in sorted_symptom_count.items()}
    return relative_number_of_patients

def get_relative_symptom_counts(df, symptom_colums, date):
    sorted_counts = get_symptom_stats_by_date(df, symptom_colums, date)
    return convert_counts_to_relative_size(sorted_counts)





