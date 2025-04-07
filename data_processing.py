import pandas as pd
import numpy as np
from pathlib import Path
# Possible classes OOP style: patient-oriented, hospital/system-oriented

sheet_path = Path('data/vestfoldtriage_data_hashed.xlsx')

# Check if spreadsheet exists, if so, load it into a Pandas dataframe
if not sheet_path.exists():
    raise FileNotFoundError(f"Kan ikke finne angitt fil: {sheet_path.resolve()}!\nHar du kjørt 'npr_hashing.py'?")
else:
    df = pd.read_excel(sheet_path.name)

# Convert "urgency/triage" columns into a number format for comparison
urgency_level = {
    "NotUrgent": 1,
    "LessUrgent": 2,
    "Urgent": 3,
    "Resuscitation": 4
}

# TODO: Make new column in df with above data?


class PatientData:
    def __init__(self, patient_alias):
        self.patient_alias = patient_alias
