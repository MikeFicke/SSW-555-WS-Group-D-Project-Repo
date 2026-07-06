# Group D - Sam Bryan
# SSW-555-WS
# User Story: Marriage Before Death
# Marriage should occur before death of either spouse

import datetime


def _died_before(death_date_string, reference_date):
    """
    Parses a spouse's death date (if present) and reports whether it falls
    before reference_date. Shared by the husband/wife checks below.
    """
    if death_date_string == "NA":
        return False
    death_date = datetime.datetime.strptime(death_date_string, "%Y-%m-%d")
    return death_date < reference_date


def validate_marriage_before_death(individual_dict, family_dict):
    """
    Function that checks if a family's spouses' marriage occurs before their death.
    Uses data from the `parse_gedcom` function in `pretty_print.py`.
    """
    for family in family_dict.values():
        marriage_date = family["Married"]
        if marriage_date == "NA":
            continue  # there is no data, skip
        marriage_date = datetime.datetime.strptime(marriage_date, "%Y-%m-%d")

        husband_death_date = individual_dict.get(family["Husband ID"], {}).get("Death", "NA")
        wife_death_date = individual_dict.get(family["Wife ID"], {}).get("Death", "NA")

        if _died_before(husband_death_date, marriage_date) or _died_before(wife_death_date, marriage_date):
            print(f"ERROR: Death date in family {family['ID']} is before marriage date {marriage_date}")
