# FlytStat
FlytStat (Flyttavle Statistics) is a dashboard comprised of statistics from the Emergency Room of a norwegian hospital<br>
It serves as the final assignment (prosjektoppgave) for the USN PY1010 course.

## Purpose
TBA
## Background
TBA
## Progress requirements
* [ ] Arrays
* [ ] Vector calculation
* [ ] If / Else comparators
* [ ] For- or While-loops
* [ ] Read and write data to file
* [ ] Plotting
* [ ] Custom functions

## Feature summary:
<details>
  <summary>🔒 Patient data anonymization</summary>
  
  ### Source: _/scripts/npr__hashing.py_
  
  A function that takes a raw data source from the Flyttavle application and hides the marginally identifiable "NPR IDs" with a uniquely indexed alias number.
  This number is unique to the patient, but stays the same if the patient is admitted again. In this way, one can still compute patient-oriented statistics like total number of visits per patient.
  
  File is opened in binary format, and using the built-in Python "pickle" function, it serializes the ID's into a .pkl / "Pickle" file. 
  
  This file, along with the original, un-aliased data source, is excluded from the remote repo through the .gitignore.

  ### Skills used:
  - Custom functions
  - reading data from file
  - plotting data to file
  - if-statements
  - for-loops (counter)
</details>
