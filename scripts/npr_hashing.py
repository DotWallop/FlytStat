"""
Note: I had some help figuring this logic out from a developer friend of mine.
I researched the pickle-library and figured out the best solution I could come up with for this.
I also came to the conclusion that the most secure thing was to run this script locally and only update the aliased data, in order to never expose the NPR ID's (ref. readme glossary) publicly.
"""
from common import ORIGINAL_SHEET_PATH, ROOT_DIR, HASHED_SHEET_PATH
import pickle
from pathlib import Path

import pandas as pd

def hash_aliases_from_excel():
    file_path = ORIGINAL_SHEET_PATH # Get file path

    try:
        df = pd.read_excel(file_path, usecols="A:AQ") # Read the triage Excel file
        print(f"{file_path.name} er lastet inn!")
    except FileNotFoundError:
        print(f"Kan ikke finne fil {file_path.name} i mappe: {file_path.parent}!")
        return
    except PermissionError:
        print(f"Ingen tilgang til {file_path}! Har du filen åpen?")
        return
    except ValueError as e:
        print(f"Ånei! Noe gikk galt: \n{e}")
        return


    # Uses 'pathlib' method Path to conveniently store boolean response if there already is a mapping table
    vestfoldtriage_hash_table_path = ROOT_DIR / "data" / "vestfoldtriage_data_hashed.pkl"

    # Uses Pathlib to check for hashed file in data dir, and creates an empty dictionary if it doesn't.
    if vestfoldtriage_hash_table_path.exists():
        # Opening file in read mode as a binary stream in order to unpickle and read the file (for adding new entries). Built with help from the pickle docs.
        with open(vestfoldtriage_hash_table_path, "rb") as triage_data:
            vestfoldtriage_hash = pickle.load(triage_data)
    else:
        vestfoldtriage_hash = {}
    # TODO: Burde jeg ha en sjekk for å se om alias_ids er tom (try/except)?
    # Initiating a variable 'alias_ids', which is a set of the 'NPR ID' column in the data source, then subtracts already hashed ID's - making a unique list of unhashed ID's.
    new_alias_ids = set(df['NPR ID']) - vestfoldtriage_hash.keys()
    start_index = len(vestfoldtriage_hash) + 1  # Counter variable in preparation for enumeration below, returning first unhashed index.

    # Looping through the 'vestfoldtriage_hash' dictionary, replacing the NPR ID with unique alias, using pad formatting (':05')
    for alias, npr_id in enumerate(new_alias_ids, start=start_index):
        vestfoldtriage_hash[npr_id] = f"pasient_{alias:05}"

    # Dumping the now aliased pickle file, opening again in write mode as binary stream. Dump = pickle
    with open(vestfoldtriage_hash_table_path, "wb") as triage_data:
        pickle.dump(vestfoldtriage_hash, triage_data)

    # checking for dupe, Initializing new column, applying update to dataframe
    if 'Alias ID' not in df.columns:
        df.insert(0, 'Alias ID', df['NPR ID'].map(vestfoldtriage_hash))
        # Dropping (deleting) original ID column in dataframe to protect identity
    df = df.drop('NPR ID', axis=1)

    # Save as Excel
    print("Lagrer ID-nummer. Dette kan ta litt tid ...")
    df.to_excel(HASHED_SHEET_PATH, index=False)
    print(f"Suksess! Lagret {len(new_alias_ids)} ID-nummer.")

# Main guard - A trick my developer friend taught me.. :)
if __name__ == "__main__":
    hash_aliases_from_excel()
    print("Prosess fullført!")
