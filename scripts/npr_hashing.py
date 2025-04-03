import pandas as pd
import pickle
from pathlib import Path
import csv

'''
Note: I had some help figuring this logic out from a developer friend of mine.
I researched the pickle-library and figured out the best solution I could come up with for this.
I also came to the conclusion that the most secure thing was to run this script locally and only update the aliased data, in order to never expose the NPR ID's (ref. readme glossary) publicly.
'''


def hash_new_aliases():
    # Read the triage Excel file
    df = pd.read_excel("data/sensitive/vestfoldtriage.xlsx", usecols="A:AT")
    # Uses 'pathlib' method Path to conveniently store boolean response if there already is a mapping table
    vestfoldtriage_hashed_path = Path("../data/vestfoldtriage_data_hashed.pkl")

    # Uses Pathlib to check for hashed file in data dir, and creates an empty dictionary if it doesn't.
    if vestfoldtriage_hashed_path.exists():
        # Opening file in read mode as a binary stream in order to unpickle and read the file (for adding new entries). Built with help from the pickle docs.
        with open(vestfoldtriage_hashed_path, "rb") as triage_data:
            vestfoldtriage_hash = pickle.load(triage_data)  # TODO: explain .load method
    else:
        vestfoldtriage_hash = {}
    # TODO: Burde jeg ha en sjekk for å se om alias_ids er tom (try/except)?
    # Initiating a variable 'alias_ids', which is a set of the 'NPR ID' column in the data source, then subtracts already hashed ID's - making a unique list of unhashed ID's.
    new_alias_ids = set(df['NPR ID']) - vestfoldtriage_hash.keys()
    start_index = len(vestfoldtriage_hash) + 1  # Counter variable in preparation for enumeration below, finding first o

    # Looping through the 'vestfoldtriage_hash' dictionary, replacing the NPR ID with unique alias, using pad formatting (':05')
    for alias, npr_id in enumerate(new_alias_ids, start=start_index):
        vestfoldtriage_hash[npr_id] = f"pasient_{alias:05}"

    # Dumping the now aliased pickle file, opening again in write mode as binary stream. Dump = pickle
    with open(vestfoldtriage_hashed_path, "wb") as triage_data:
        pickle.dump(vestfoldtriage_hash, triage_data)

    # checking for dupe, Initializing new column, applying update to dataframe
    if 'Alias ID' not in df.columns:
        df.insert(0, 'Alias ID', df['NPR ID'].map(vestfoldtriage_hash))
        # Dropping (deleting) original ID column in dataframe to protect identity
    df = df.drop('NPR ID', axis=1)

    # Save as Excel
    df.to_excel("../data/vestfoldtriage_data_hashed.xlsx")
    print(f"Success! Saved {len(new_alias_ids)} ID's.")

hash_new_aliases()