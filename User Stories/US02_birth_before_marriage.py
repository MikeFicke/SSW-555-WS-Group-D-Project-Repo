# Group D - Michael Ficke
# SSW-555-WS
# User Story: Birth before marriage
# Birth should occur before marriage of an individual

# Refactoring: Husband check and wife check contain nearly identical code.  Logic can be cleaned up to reduce the file size and make it more efficient.

# Acknowledgement: IDE auto-complete was used for certain lines of code

import datetime

def check_spouse_birth_helper(individual_dict, spouse_id, marriage_date, family_id, role):
    """
    Helper function that checks if a spouse's birthday is before the marriage date.
    """
    if not spouse_id or spouse_id == "NA" or spouse_id not in individual_dict:
        return  # Nothing to check, so skip

    birthday = individual_dict[spouse_id]["Birthday"]
    if not birthday or birthday == "NA":
        return  # Nothing to check

    # Convert to datetime
    birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d")

    if birthday >= marriage_date:
        print(f"ERROR: {role}'s birthday in family {family_id} is after marriage date {marriage_date}")

def validate_birth_before_marriage(individual_dict, family_dict):
    """
    Function that checks if a family's spouses' birthdates occur before their marriage.
    Uses data from the `parse_gedcom` function in `pretty_print.py`.
    """
    for family in family_dict.values():
        marriage_date = family["Married"]
        if marriage_date == "NA":
            continue  # there is no data, skip
        # citation: https://www.google.com/search?q=python+how+to+convert+a+sring+date+to+a+yyyy-mm-dd+format%3F&rlz=1C1CHBF_enUS1023US1023&oq=python+how+to+convert+a+sring+date+to+a+yyyy-mm-dd+format%3F&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQIRgKGKABMgkIAhAhGAoYqwIyCQgDECEYChirAjIHCAQQIRiPAjIHCAUQIRiPAtIBCDkzMDRqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8
        marriage_date = datetime.datetime.strptime(marriage_date, "%Y-%m-%d")
        husband_id = family["Husband ID"]
        wife_id = family["Wife ID"]
        check_spouse_birth_helper(individual_dict, husband_id, marriage_date, family['ID'], 'Husband')
        check_spouse_birth_helper(individual_dict, wife_id, marriage_date, family['ID'], 'Wife')
