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

def get_triage_stats_per_day():




# -- USER INPUTS -- #
month_input = 0
day_input = 0
def month_date_input():

    while True:  # Month and date wrapper
        while True:  # Month
            print("Velg  ønsket måned (MM):\nEksempel: '03' for Mars.")
            _user_month_input = input("Måned: ")

            # RegEx match statement. Self-made pattern, passed all my tests, so should be good.
            _user_month_input = re.search(r"(0[1-9]|1[0-2])",_user_month_input)

            if _user_month_input is None:
                print("Feil inntasting. Måned må være to siffer, og gyldig måned.\n")
                continue
            break  # Month

        while True:  # Day
            print("Velg ønsket dato (DD):\nEksempel: '18' for den attende i måneden.")
            _user_date_input = input("Dato: ")

            # No 30-31 validation as I did not find a reasonable way of doing this.
            _user_date_input = re.search(r"(0[1-9]|[1-2][0-9]|3[0-1])",_user_date_input)

            if _user_date_input is None:
                print("Feil inntasting. Måned må være to siffer, og en gyldig dato.\n")
                continue
            break  # Day
        break  # Wrapper
    month_input = int(_user_month_input)
    date_input = int(_user_date_input)

