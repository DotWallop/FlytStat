"""
Utility function file for common and global variables.
"""
import pandas as pd
import numpy as np

URGENCY_LEVELS = {"NotUrgent": 1,
                  "LessUrgent": 2,
                  "Urgent": 3,
                  "Resuscitation": 4
                  }

HOUR_LABELS = [f"{hour:02d}:00" for hour in range(24)]
