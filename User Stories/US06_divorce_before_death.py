# Group D - William Bryce
# SSW-555-WS
# User Story: Divorce before death
# Divorce can only occur before death of both spouses

import datetime

def validate_divorce_before_death(individual_dict, family_dict):
    for family in family_dict.values():
        divorce_date = family["Divorced"]
        if not divorce_date or divorce_date == "NA":
            continue
        divorce_date = datetime.datetime.strptime(divorce_date, "%Y-%m-%d").date()
        husband = family["Husband ID"]
        wife = family["Wife ID"]
        husband_death = individual_dict[husband]["Death"]
        wife_death = individual_dict[wife]["Death"]
        if husband_death and husband_death != "NA":
            husband_death = datetime.datetime.strptime(husband_death, "%Y-%m-%d").date()
            if husband_death < divorce_date:
                print(f"ERROR: FAMILY: US06: {family['ID']}: Divorced {divorce_date} after husband's ({husband}) death on {husband_death}")
        if wife_death and wife_death != "NA":
            wife_death = datetime.datetime.strptime(wife_death, "%Y-%m-%d").date()
            if wife_death < divorce_date:
                print(f"ERROR: FAMILY: US06: {family['ID']}: Divorced {divorce_date} after wife's ({wife}) death on {wife_death}")
        