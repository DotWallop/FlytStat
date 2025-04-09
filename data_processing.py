"""
This file handles the data processing necessary for the plots to function.
It expects a hashed xlsx file, so run npr_hashing.py first.
"""
from common import URGENCY_LEVELS
from pathlib import Path

import pandas as pd

sheet_path = Path('data/vestfoldtriage_data_hashed.xlsx')

# Check if spreadsheet exists, if so, load it into a Pandas dataframe
if not sheet_path.exists():
    raise FileNotFoundError(f"Kan ikke finne angitt fil: {sheet_path.resolve()}!\nHar du kjørt 'npr_hashing.py'?")
df = pd.read_excel(sheet_path)

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
    # Mapping old_col string values to URGENCY_LEVELS int counterpart, inserts col right of old original col
    new_col_index = df.columns.get_loc(old_col) + 1  # TODO: Test get_loc
    mapped_urgency_values = df[old_col].map(URGENCY_LEVELS)
    df.insert(new_col_index, new_col_name, mapped_urgency_values)

    print(f"Mapping complete: {mapped_urgency_values.count()} values mapped!") # Console print

def df_value_filter(col_name, filter_value):
    return df

# Initialize date info
def get_date_info():
    first_date = df['Ankomst'].min()
    last_date = df['Ankomst'].max()
    return {
        "first_date": first_date,
        "last_date": last_date,
        "date_range": pd.date_range(first_date,last_date, freq='D')
    }

if __name__ == "__main__":
    # Mapping string keys to their respective int value to enable comparison
    TRIAGE_COLUMNS = ['Resultat av første pretriage', 'Resultat av første legerespons', 'Resultat av første triage', 'Klinisk bekymring i første triage']
    for column in TRIAGE_COLUMNS:
        insert_triage_col(column)

    # Applying Pandas' .to_datetime function to all datetime-columns
    DATETIME_COLUMNS = ['Ankomst', "Avreise", "Tidspunkt for første pretriage", "Tidspunkt for første legerespons", "Tidspunkt for første triage"]
    df[DATETIME_COLUMNS] = df[DATETIME_COLUMNS].apply(pd.to_datetime, errors='coerce') # Coerce = error fields => NaT

    GLOBAL_DATE_INFO = get_date_info()

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
