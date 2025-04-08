# DateTime variable setting:
import pandas as pd
from data_processing import df
import numpy as np

# -- GLOBAL VALUES -- #
# Datetime
first_date = df['Ankomst'].min()
last_date = df['Avreise'].max()
date_range = pd.date_range(first_date,last_date, freq='D')

