import pandas as pd
import pickle
from pathlib import Path

'''
Note: I had some help figuring this logic out from a developer friend of mine.
I researched the pickle-library and figured out the best solution I could come up with for this.
I also came to the conclusion that the most secure thing was to run this script locally and only update the aliased data, in order to never expose the NPR ID's (ref. readme glossary) publicly.
'''
# Read the triage CSV file
df = pd.read_excel("../data/sensitive/vestfoldtriage.csv")

# Uses 'pathlib' method Path to conveniently store boolean response if there already is a mapping table
vestfoldtriage_hashed_path = Path("../data/vestfoldtriage_data_hashed.pkl")
if vestfoldtriage_hashed_path.exists():
    with open(vestfoldtriage_hashed_path) as triage_data:
        vestfoldtriage_hash = pickle.load(triage_data) # TODO: explain .load met

else:
    vestfoldtriage_hash = {}