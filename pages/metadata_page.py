""" This page displays relevant info about the dataset in question."""
from data_processing import get_metadata

def run():
    source_metadata = get_metadata()
    print("\n== Informasjon om datasett ==\n")
    print(f"Datoområde: {source_metadata["first_date"].date()} - {source_metadata["last_date"].date()}\n")
    print(f"Antall pasienter: {source_metadata["total_patient_count"]}")
    print()