import pandas as pd
import numpy as np
from pathlib import Path
# Possible classes OOP style: patient-oriented, hospital/system-oriented

sheet_path = Path('data/vestfoldtriage_data_hashed.xlsx')

if not sheet_path.exists():
    raise ValueError



class PatientData:
    def __init__(self, patient_alias):
        self.patient_alias = patient_alias

