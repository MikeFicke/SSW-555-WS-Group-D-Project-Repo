# Sam Bryan - Group D
# Child should be born before death of mother and before 9 months after death of father

import datetime

def validate_birth_before_death(individual_dict):
    """
    Function that checks if a child is born before the death of their mother and before 9 months after the death of their father.
    Uses data from the `parse_gedcom` function in `pretty_print.py`.
    """
    for individual in individual_dict.values():
        birth_date = individual.get("Birthday", "NA")
        if birth_date == "NA":
            continue
        birth_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d")
        mother_death_date = individual.get("Mother Death", "NA")
        father_death_date = individual.get("Father Death", "NA")
        father_death_date_normalized = father_death_date + datetime.timedelta(months=9) if father_death_date != "NA" else "NA"