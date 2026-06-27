# Sam Bryan - Group D, pair programmed with Michael Ficke
# Child should be born before death of mother and before 9 months after death of father
# Acknowledgement: Certain lines of code were written using IDE auto-complete

import datetime

def validate_birth_before_death(individual_dict, families_dict):  # Note: need to add families dictionary as well
    """
    Function that checks if a child is born before the death of their mother and before 9 months after the death of their father.
    Uses data from the `parse_gedcom` function in `pretty_print.py`.
    """
    # Note: Adjusting for loop logic

    # for individual in individual_dict.values():
    #     birth_date = individual.get("Birthday", "NA")
    #     if birth_date == "NA":
    #         continue
    #     birth_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d")
    #     mother_death_date = individual.get("Mother Death", "NA")
    #     father_death_date = individual.get("Father Death", "NA")
    #     father_death_date_normalized = father_death_date + datetime.timedelta(months=9) if father_death_date != "NA" else "NA"

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

        mother_death_date = individual_dict.get(wife_id, {}).get("Death", "NA")
        father_death_date = individual_dict.get(husband_id, {}).get("Death", "NA")

        if mother_death_date == "NA" and father_death_date == "NA":
            # skip; nothing to check
            continue

        for child in children:
            """
            We need to get the child's birth date, perform a data quality pre-check, parse the date, 
            and then do if comparisons and error reporting.
            """
            # TODO
            continue

    # TODO: Need to also call the function in main.py and test with test data.
