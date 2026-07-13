# SSW-555-WS-Group-D-Project-Repo

Group D's project repo for SSW-555-WS.

## Overview

A command-line Python program that parses GEDCOM genealogy files, pretty-prints summaries of individuals and families, and detects errors and anomalies based on user story validation rules.

## Setup

```bash
# Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\activate        # Windows
source .venv/bin/activate       # macOS/Linux

# Install dependencies
pip install prettytable python-dateutil
```

## Usage

```bash
python main.py <path_to_gedcom_file>
```

Example:

```bash
python main.py GEDCOMs/GEDCOM-test-data.ged
```

Output is printed to the terminal and also saved to `output.txt`.

## Project Structure

```
.
├── main.py                  # Entry point — parses GEDCOM, runs all validations
├── pretty_print.py          # GEDCOM parser and table printer
├── GEDCOMs/                 # Test GEDCOM data files
│   ├── GEDCOM-test-data.ged
│   ├── US07-stress-test.ged
│   ├── US08-stress-test.ged
│   ├── US09-stress-test.ged
│   ├── US10-stress-test.ged
│   ├── US11-stress-test.ged
│   ├── US12-stress-test.ged
│   ├── US15-stress-test.ged
│   └── ...
├── User Stories/            # Validation logic (one file per user story)
│   ├── US01_dates_before_current_date.py
│   ├── US02_birth_before_marriage.py
│   ├── US03_birth_before_death.py
│   ├── US04_marriage_before_divorce.py
│   ├── US05_marriage_before_death.py
│   ├── US06_divorce_before_death.py
│   ├── US07_less_than_150_years_old.py
│   ├── US08_birth_after_marriage.py
│   ├── US09_birth_before_parent_death.py
│   ├── US10_marriage_after_14.py
│   ├── US11_no_bigamy.py
│   ├── US12_parents_not_too_old.py
│   └── US15_fewer_than_15_siblings.py
└── User Story Tests/        # Unit tests per user story
```

## Implemented User Stories

| ID   | Description                                                           |
| ---- | --------------------------------------------------------------------- |
| US01 | Dates before current date                                             |
| US02 | Birth before marriage                                                 |
| US03 | Birth before death                                                    |
| US04 | Marriage before divorce                                               |
| US05 | Marriage before death of spouse                                       |
| US06 | Divorce before death of spouse                                        |
| US07 | Age less than 150 years                                               |
| US08 | Birth after marriage of parents (and within 9 months of divorce)      |
| US09 | Birth before death of parents (and within 9 months of father's death) |
| US10 | Marriage after age 14                                                 |
| US11 | No bigamy                                                             |
| US12 | Parents not too old                                                   |
| US15 | Fewer than 15 siblings                                                |
| US18 | Siblings should not marry one another                                |

## Team

- Group D — 3 members
- Branching: feature branches off `main`, merged via PRs only
