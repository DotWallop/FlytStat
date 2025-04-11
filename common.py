"""
Utility function file for common and global variables.
"""
from pathlib import Path

ROOT_DIR = Path.cwd() if __name__ == "__main__" else Path(__file__).resolve().parent # Gets working dir if ran from IDE, else full base path
ORIGINAL_SHEET_PATH = ROOT_DIR / "data" / "sensitive" / "vestfoldtriage.xlsx"
HASHED_SHEET_DIR = ROOT_DIR / "data"
HASHED_SHEET_PATH = ROOT_DIR / "data" / "vestfoldtriage_data_hashed.xlsx"

URGENCY_LEVELS = {"NotUrgent": 1,
                  "LessUrgent": 2,
                  "Urgent": 3,
                  "Resuscitation": 4
                  }

HOUR_LABELS = [f"{hour:02d}:00" for hour in range(24)]