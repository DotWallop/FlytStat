"""
Utility function file for common and global variables.
"""
import pandas as pd

from data_processing import df

def get_date_info():
    first_date = df['Ankomst'].min()
    last_date = df['Ankomst'].max()
    return {
        "first_date": first_date,
        "last_date": last_date,
        "date_range": pd.date_range(first_date,last_date, freq='D')
    }


URGENCY_LEVEL = { "NotUrgent": 1,
                  "LessUrgent": 2,
                  "Urgent": 3,
                  "Resuscitation": 4
                 }
