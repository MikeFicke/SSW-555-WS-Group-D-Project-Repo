# Sam Bryan - Group D
# Children should be born after marriage of parents (and not more than 9 months after their divorce)

import datetime
from dateutil.relativedelta import relativedelta  # imported and used for easier date checks

def validate_birth_after_marriage(individual_dict, families_dict):
    """
    Function that checks if children should be born after marriage of parents (and not more than 9 months after their divorce).
    Uses data from the `parse_gedcom` function in `pretty_print.py`.
    """
    for family in families_dict.values():
        children = family.get("Children", [])
        if children == []:
            # skip, as there is nothing to check
            continue

        wife_id = family.get("Wife ID", "NA")
        husband_id = family.get("Husband ID", "NA")

        if wife_id == "NA":
            # skip; nothing to check
            continue
        if husband_id == "NA":
            continue

        marriage_date = family.get("Married", "NA")
        divorce_date = family.get("Divorced", "NA")

        if marriage_date == "NA":
            # skip; nothing to check
            continue

        marriage_date_parsed = datetime.datetime.strptime(marriage_date, "%Y-%m-%d")
        divorce_date_parsed = datetime.datetime.strptime(divorce_date, "%Y-%m-%d") if divorce_date != "NA" else None

        for child in children:
            birth_date = individual_dict.get(child, {}).get("Birthday", "NA")
            if birth_date == "NA":
                continue

            birth_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d")

            if birth_date < marriage_date_parsed:
                print(f"ERROR: Child {child} was born before the marriage of their parents in family {family['ID']}")

            if divorce_date_parsed is not None and birth_date > divorce_date_parsed + relativedelta(months=9):
                print(f"ERROR: Child {child} was born more than 9 months after the divorce of their parents in family {family['ID']}")

    # Note: called the function in main.py to test with test data.
