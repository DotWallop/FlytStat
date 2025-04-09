from common import HOUR_LABELS
from metrics import get_triage_stats_per_unit, user_date_prompt_to_timestamp
from data_processing import df

import matplotlib.pyplot as plt
import numpy as np

# Stacked bar chart per day TODO: Decide if the data definition belongs here, or in data_processing

def build_stacked_bar_triage_for_day():
    """
    Prompts user for date input, then builds stacked bar chart for no. of patients admitted per hour for selected day.
    Built with help from matplotlib documentation
    """
    selected_date = user_date_prompt_to_timestamp()
    patient_triage_dict = get_triage_stats_per_unit(selected_date, 'hour')  # TODO: Make hour inherit from user input?

    triage_counts = {
        "NotUrgent Patients": np.array([patient_triage_dict[hour]['NotUrgent'] for hour in range(24)]),
        "LessUrgent Patients": np.array([patient_triage_dict[hour]['LessUrgent'] for hour in range(24)]),
        "Urgent Patients": np.array([patient_triage_dict[hour]['Urgent'] for hour in range(24)]),
        "Resuscitation Patients": np.array([patient_triage_dict[hour]['Resuscitation'] for hour in range(24)])
    }  #  TODO: Replace placeholder labels with norwegian equivalent



    width = 0.5

    fix, ax = plt.subplots()
    bottom = np.zeros(24)  # Initializes an array of 24 zeros. Will be the bottom of the bar chart.
    for label, count in triage_counts.items():
        p = ax.bar(HOUR_LABELS, count, width, label=label, bottom=bottom)
        bottom += count
    ax.set_title(f"Antall pasienter ankommet akuttsenteret\n{selected_date.strftime("%d. %B %Y")}")
    ax.legend(loc="upper right")

    plt.show()

bar_chart = build_stacked_bar_triage_for_day()

# Pie charts - quantity of the most prevalent diagnoses that day? Input date?
# - Maybe add an attribute if you want to see day, month or year - and inform the user through input() statements pre-call


# Bar chart - Triage per day

# Line plot or similar - patients per hour per triage category (input: date)

# Test out matplotlib's subplot feature to make multiple plots!