# Group D
# SSW-555-WS
# User Story: Marriage after 14
# Marriage should be at least 14 years after birth of both spouses (parents must be at least 14 years old)
# Pair programming Duo: William Bryce and Michael Ficke
# Acknowledgement: IDE Auto-complete was used for certain lines of code


import datetime
from dateutil.relativedelta import relativedelta  # Need this for date comparisons

def validate_marriage_after_14(individual_dict, family_dict):
    for family in family_dict.values():
        marriage_date = family["Married"]
        if marriage_date == "NA":
            continue
        marriage_date = datetime.datetime.strptime(marriage_date, "%Y-%m-%d").date()

        husband = family["Husband ID"]
        wife = family["Wife ID"]

        husband_birth = individual_dict[husband]["Birthday"]
        wife_birth = individual_dict[wife]["Birthday"]

        # Possible bug found: Need to check if the dates are 'NA' before doing conversions and calculations, otherwise there will be a risk of a crash

        if husband_birth == "NA":
            # If there is no birthdate, we need to skip.
            continue
        if wife_birth == "NA":
            continue

        # spouses birthdates in datetime
        husband_birth = datetime.datetime.strptime(husband_birth, "%Y-%m-%d").date()
        wife_birth = datetime.datetime.strptime(wife_birth, "%Y-%m-%d").date()
        
        husband_age_diff = relativedelta(marriage_date, husband_birth)  # This value is a positive number if marriage is after birth, and negative if before
        husband_marriage_age = husband_age_diff.years
        
        wife_age_diff = relativedelta(marriage_date, wife_birth)  # This value is a positive number if marriage is after birth, and negative if before
        wife_marriage_age = wife_age_diff.years

        if husband_marriage_age < 14:
            print(f"ERROR: FAMILY: US10: {family['ID']}: Individual {individual_dict[husband]['Name']} was married before age 14.")

        if wife_marriage_age < 14:
            print(f"ERROR: FAMILY: US10: {family['ID']}: Individual {individual_dict[wife]['Name']} was married before age 14.")

        # TODO: also need main.py imports and unit tests as evidence that it works.
