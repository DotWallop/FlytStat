# FlytStat

## 🩺 TL;DR
FlytStat is a command-line based ETL application for anonymized triage data from a Norwegian hospital's ER system.
It hashes patient IDs, transforms timestamped records, and graphs patient inflow and symptom distributions.

Built as a final project for the USN PY1010 course.

## 📚 Table of Contents

- [Purpose](#purpose)
- [Feature Summary](#%EF%B8%8F-feature-summary)
- [Installation](#-installation)
- [Key Learning Points](#-key-learning-points)
- [Disclaimer on Scope, Competence and AI](#-scope-competence-and-ai)
- [Project Structure](#-project-structure)
- [License / Usage Disclaimer](#-license--usage-disclaimer)

## ❓Purpose

The tool aims to serve as an [ETL pipeline](https://en.wikipedia.org/wiki/Extract,_transform,_load), extracting a raw datadump from the host software's statistics servers, transform them into a parseable,
structured and dynamically accessible format, then load it into a graphical presentation.

FlytStat is run as a CLI tool, and the current version is an **MVP**, but feature-complete for the scope of the assignment.

## 🏷️ Feature summary:
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
  - Serializing and anonymizing patient data using pickle mapping
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

## 🚀 Installation:
### 1. Clone Repository and 'CD' in
```bash
git clone https://github.com/DotWallop/FlytStat.git
cd FlytStat
```

### 2. Install required packages
```bash
pip install -r requirements.txt
```

### 3. Run `main.py`

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

---
## 🤖 Scope, Competence and AI:

I think it's worth mentioning that I have been honing my Python skills in my free time, expanding from the class scope.

In addition to classes, I have been using [Mimo](https://mimo.org) as well as taking several [Codecademy](https://www.codecademy.com)
courses on Python, Pandas and Matplotlib & NumPy. That is the reason for going slightly outside of scope.

I have utilized ChatGPT and Claude for bugfixing and explanation on specific subjects, including explaining more complex system logic. Nothing has been __built__ purely from AI.


## 📂 Project Structure

```text
├── main.py                     # Entry point CLI menu
├── common.py                  # Global constants and paths
├── data_processing.py         # Data loading and transformation
├── metrics.py                 # Triage and symptom statistics
├── plots.py                   # Visualization logic
├── plot_styling.py            # Centralized plot color styling
├── pages/
│   ├── metadata_page.py       # Dataset overview display
│   └── statistics_page.py     # Submenu for plotting
├── scripts/
│   └── npr_hashing.py         # Patient ID hashing logic
├── data/                      # Contains original and hashed data files
├── requirements.txt
└── readme.md
```
## ⚖️ License / Usage Disclaimer
This project is built as a coursework submission. It is not intended for clinical or production use.
Patient data is handled securely and fully anonymized (only placeholder numbers are included), but the repository only contains test-safe, hashed output and never stores NPR IDs.
