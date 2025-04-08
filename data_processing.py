"""
This file handles the data processing necessary for the plots to function.
It expects a hashed xlsx file, so run npr_hashing.py first.
"""
import pandas as pd
from pathlib import Path


sheet_path = Path('data/vestfoldtriage_data_hashed.xlsx')

def insert_triage_col(old_col):
    """Creates and inserts parsed triage column to the right of the original column"""

    new_col_name = f"converted_{old_col[0:20].replace(" ", "_")}"  # Generates shortened, code-friendly name

    # Handling most common errors
    if df is None or df.empty:
        raise ValueError('Pandas DataFrame not found.')
    elif not old_col in df.columns:
        raise ValueError(f"'{old_col}' not found in DataFrame.")
    elif new_col_name in df.columns:
        print(f"Existing column: '{new_col_name}' found. Skipping column.")
        return False

    print(f"Mapping '{old_col}'.\n This might take some time ...")  # Console print
    # Mapping old_col string values to urgency_level int counterpart, inserts col right of old original col
    new_col_index = df.columns.get_loc(old_col) + 1  # TODO: Test get_loc
    mapped_urgency_values = df[old_col].map(urgency_level)
    df.insert(new_col_index, new_col_name, mapped_urgency_values)

    print(f"Mapping complete: {mapped_urgency_values.count()} values mapped!") # Console print


# Check if spreadsheet exists, if so, load it into a Pandas dataframe
if not sheet_path.exists():
    raise FileNotFoundError(f"Kan ikke finne angitt fil: {sheet_path.resolve()}!\nHar du kjørt 'npr_hashing.py'?")
else:
    df = pd.read_excel(sheet_path)

urgency_level = { "NotUrgent": 1,
                  "LessUrgent": 2,
                  "Urgent": 3,
                  "Resuscitation": 4
                  }

# Mapping string keys to their respective int value to enable comparison
insert_triage_col('Resultat av første pretriage')
insert_triage_col('Resultat av første legerespons')
insert_triage_col('Resultat av første triage')
insert_triage_col('Klinisk bekymring i første triage')

# Applying Pandas' .to_datetime function to all datetime-columns
datetime_columns = ['Ankomst', "Avreise", "Tidspunkt for første pretriage", "Tidspunkt for første legerespons", "Tidspunkt for første triage"]
df[datetime_columns] = df[datetime_columns].apply(pd.to_datetime, errors='coerce') # Coerce = error fields => NaT


# Outputs modified file to the excel file
try:
    df.to_excel(sheet_path, index=False)
except ValueError:
    print(f"{sheet_path.name} not found. Please run 'scripts/npr_hashing.py' again to regenerate.")
except PermissionError:
    print(f"Could not write to file: permission denied. Do you have {sheet_path.name} open?")
except Exception as e:
    print(f"Unexpected error!\n{e}")
else:
    print("Successfully edited file.")
