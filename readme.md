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
* [x] If / Else comparators
* [x] For- or While-loops
* [x] Read and write data to file
* [ ] Plotting
* [x] Custom functions

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
<details>
  <summary>📝 CSV vs. Xlsx</summary>
  
  The data source was retrieved from a CSV file. The CSV file alone is around 5 Mb comprised of over 30,000 lines, all in which have over 40 values to them.
  I quickly found out that parsing a file this big brought many problems; file integrity, parsing, binary stream issues due to memory constraints etc.

  In reality, I would likely been able to get around this with research and just a touch of AI assistance (though, the results I tried using both OpenAI and Claude only rendered useless responses despite good prompting),
  but I made a decision to rather convert this to an .xlsx file - in order to keep the scope of the project within confines.
  
  For a file this large, I would for a production project always have gone with a CSV file (or in reality, a database, even a lightweight one like SQLite) to give better options.
  I have some experience with SQLite, but as that is outside the scope of PY1010, I chose not to include it.

</details>

