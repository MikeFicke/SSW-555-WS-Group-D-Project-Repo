# Group D
# SSW-555-WS
# User Story: Marriage after 14
# Marriage should be at least 14 years after birth of both spouses (parents must be at least 14 years old)

import datetime

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
        # spouses birthdates in datetime
        husband_birth = datetime.datetime.strptime(husband_birth, "%Y-%m-%d").date()
        wife_birth = datetime.datetime.strptime(wife_birth, "%Y-%m-%d").date()
        
        # comparison of marriage_date to both spouses, checking at least 14 years old
        # if not: print(f"ERROR: FAMILY: US10: {family['ID']}: Marriage occurs before both spouses are at least 14 years old")
        