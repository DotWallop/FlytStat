# FlytStat

FlytStat (Flyttavle Statistics) is a lightweight tool comprised of statistics from the Emergency Room of a norwegian hospital<br>
It serves as the final assignment (prosjektoppgave) for the USN PY1010 course.

## Purpose

The tool aims to serve as an [ETL pipeline](https://en.wikipedia.org/wiki/Extract,_transform,_load), extracting a raw datadump from the host software's statistics servers, transform them into a parseable,
structured and dynamically accessible format, then load it into a graphical presentation.

FlytStat is run as a CLI tool, and the current version is an **MVP**, but feature-complete for the scope of the assignment.

## Installation:
### 1. Clone Repository and 'CD' in
```py
git clone https://github.com/DotWallop/FlytStat.git
cd FlytStat
```

### 2. Install required packages
```py
pip install -r requirements.txt
```

### 3. Run `main.py`


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
---

## TBD: Explain reasons for going outside scope
  - Codecademy kurs Pandas, numpy+matplotlib
  - Mimo + Codecademy Python
  - 
---
## ⭐ Key Learning Points
I learned a lot of things throughout this project. I have summarized them for myself, and for whomever is reading this.
<details>
  <summary>Follow established best practice!</summary>

  Stick to best practice. Proactively using DRY, YAGNI and others that I've probably not heard about yet goes a long way.
</details>

<details>
  <summary>Think out an OOP structure from the get-go</summary>

  I started out using a functional structure. As the project grew, I realized how cluttered it had become.

  At that point, I did not have time to refactor everything. Depending on when you are grading it, and if I want to take on the task, I might have a separate OOP-branch.
</details>

<details>
  <summary>Narrow file scope</summary>

  Circular import issues, not being able to find the function you want etc... Keep global settings to a global file, import only what you need, where you need it.
</details>

<details>
  <summary>Function before looks!</summary>

  It's **super** easy to get carried away exploring how to make the program prettier. I spent a bit too much time fiddling around with
  visual libraries and originally implemented the Rich library with Loguru for pretty-print and rich console output. However this added complexity,
  And gave errors I did not know how to fix. Thus, I made the decision to remove them. Rookie mistake!
</details>

<details>
  <summary>Main guarding is a lifesaver!!</summary>

  A developer friend of mine taught me about the `if __name__ == "__main__"` - also called main guarding - function.
  This is absolutely crucial for making sure you don't load the whole files from import. Amongst other things I use it to not load the dataframe more than once.
</details>

<details>
  <summary>(Hot take) - PEP8 is a cult manual</summary>

  Ok, maybe not __THAT__ bad 😁, but ...
  After taking the time to read through the entirety of PEP8, I realize that a lot of it resembles OCD-fueled rambling.
  Don't get me wrong, PEP8 is very useful, but it is quite a fun read!
  __"Know the rules, and know when to break them"__.
</details>