""" This page displays relevant info about the dataset in question."""
from data_processing import get_metadata
from pathlib import Path

source_metadata = get_metadata()

print("== Informasjon om datasett ==")
print(f"Datoområde: {source_metadata["first_date"].dt.date} - {source_metadata["last_date"].dt.date}")