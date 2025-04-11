from common import HOUR_LABELS
from metrics import get_triage_stats_per_unit, user_date_prompt_to_timestamp, get_relative_symptom_counts
from plot_styling import triage_style
from data_processing import load_data

import matplotlib.pyplot as plt
import numpy as np

df = load_data()
plt.style.use('ggplot')

# Stacked bar chart per day TODO: Decide if the data definition belongs here, or in data_processing

def build_stacked_bar_triage_for_day():
    """
    Prompts user for date input, then builds stacked bar chart for no. of patients admitted per hour for selected day.
    Built with help from matplotlib documentation
    """
    selected_date = user_date_prompt_to_timestamp()
    patient_triage_dict = get_triage_stats_per_unit(df,selected_date, 'hour')  # TODO: Make hour inherit from user input?

    triage_counts = {
        "NotUrgent Patients": np.array([patient_triage_dict[hour]['NotUrgent'] for hour in range(24)]),
        "LessUrgent Patients": np.array([patient_triage_dict[hour]['LessUrgent'] for hour in range(24)]),
        "Urgent Patients": np.array([patient_triage_dict[hour]['Urgent'] for hour in range(24)]),
        "Resuscitation Patients": np.array([patient_triage_dict[hour]['Resuscitation'] for hour in range(24)])
    }  #  TODO: Replace placeholder labels with norwegian equivalent

    width = 0.6

    fix, ax = plt.subplots(figsize=(14,7))
    bottom = np.zeros(24)  # Initializes an array of 24 zeros. Will be the bottom of the bar chart.
    for label, count in triage_counts.items():
        p = ax.bar(HOUR_LABELS, count, width, label=label, bottom=bottom, color=triage_style[label])
        bottom += count
    ax.set_title(f"Antall pasienter ankommet akuttsenteret\n{selected_date.strftime("%d. %B %Y")}", fontsize=22, weight='bold')
    ax.set_xlabel("Tid på døgnet", fontsize=12)
    ax.set_ylabel("Antall pasienter", fontsize=12)
    ax.legend(loc="upper right")
    ax.grid(True, axis='y', linestyle='-', alpha=0.6)
    ax.tick_params(axis='x', labelrotation=30)

    plt.show()
    return f"Generating plot for {selected_date.strftime("%d. %B %Y")} ..."


# bar_chart = build_stacked_bar_triage_for_day()  # Run

def build_symptom_pie_chart(threshold=0.05):  # Default threshold of 5%, used in grouping
    selected_date = user_date_prompt_to_timestamp()
    relative_count_dict = get_relative_symptom_counts(df, selected_date)
    # Grouping
    symptom_labels = []
    symptom_values = []
    other_total = 0.0

    for label, value in relative_count_dict.items():
        if value >= threshold:
            symptom_labels.append(label)
            symptom_values.append(value)
        else:
            other_total += value

    if other_total > 0:
        symptom_labels.append("Andre")
        symptom_values.append(other_total)

    fig, ax = plt.subplots()

    ax.pie(symptom_values, labels=symptom_labels, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')  # Aspect ratio
    ax.set_title(f"Fordeling av symptomer i akuttsenter\n{selected_date.strftime('%d. %B %Y')}")
    plt.tight_layout()

    plt.show()
    return f"Generating plot for {selected_date.strftime('%d. %B %Y')} ..."


# pie_chart = build_symptom_pie_chart()