import matplotlib.pyplot as plt
import numpy as np
from data_processing import urgency_level, date_range

# Stacked bar chart per day TODO: Decide if the data definition belongs here, or in data_processing
hours_in_day = np.array([f"{hour:02d}" for hour in range(24)])

width = 0.5

fix, ax = plt.subplots()
bottom = np.zeros(len(hours_in_day))



# Pie charts - quantity of the most prevalent diagnoses that day? Input date?
# - Maybe add an attribute if you want to see day, month or year - and inform the user through input() statements pre-call


# Bar chart - Triage per day

# Line plot or similar - patients per hour per triage category (input: date)

# Test out matplotlib's subplot feature to make multiple plots!