"""
This file handles most of the metrics in the application - variable setting and user input functions.
"""
import re

import pandas as pd
from data_processing import df
import numpy as np

# -- GLOBAL VALUES -- #
# Datetime
first_date = df['Ankomst'].min()
last_date = df['Avreise'].max()
date_range = pd.date_range(first_date,last_date, freq='D')

# Urgency / Triage
urgency_level = { "NotUrgent": 1,
                  "LessUrgent": 2,
                  "Urgent": 3,
                  "Resuscitation": 4
                  }

# -- DYNAMIC VALUES -- #
month_input, day_input = month_day_input()
month_input = 0  # Init
day_input = 0  # Init

# def user_datemonth_input_to_datetime(day, month)
#     """Dataset is from 2024-03-10 to 2025-03-09. Year will be calculated accordingly"""
#
#     if month > 03


# def get_triage_stats_per_day(): # TODO: Create tests? Pytest
#     daily_patients_noturgent = df.loc[(df['Resultat av første triage'] == 'NotUrgent') & (df['Ankomst'].dt.date == )]



# -- USER INPUTS -- #

def month_day_input():
    while True:  # Month and day wrapper
        while True:  # Month
            print("Velg  ønsket måned (MM):\nEksempel: '03' for Mars.")
            _user_month_input = input("Måned: ")

            # RegEx match statement. Self-made pattern, passed all my tests, so should be good.
            regex_match = re.search(r"(0[1-9]|1[0-2])",_user_month_input)

            if regex_match is None:
                print("Feil inntasting. Måned må være to siffer, og gyldig måned.\n")
                continue
            month_input = int(regex_match.group())  # Extracts only matched string, converts to INT => Removes leading zeros
            break  # Month

        while True:  # Day
            print("Velg ønsket dato (DD):\nEksempel: '18' for den attende i måneden.")
            _user_day_input = input("Dato: ")

            # No 30-31 validation as I did not find a reasonable way of doing this.
            regex_match = re.search(r"(0[1-9]|[1-2][0-9]|3[0-1])",_user_day_input)

            if regex_match is None:
                print("Feil inntasting. Måned må være to siffer, og en gyldig dato.\n")
                continue
            break  # Day
        day_input = int(regex_match.group()) # Extracts only matched string, converts to INT => Removes leading zeros
        break  # Wrapper

    return month_input, day_input



