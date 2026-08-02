# Group D - Sam Bryan
# SSW-555-WS
# User Story: List large age gap married couples
# List all couples who were married when the older spouse was more than twice as old as the younger spouse

import datetime
from dateutil.relativedelta import relativedelta


def validate_large_age_gap_married_couples(individual_dict, family_dict):
    large_age_gap_families = []
    for family in family_dict.values():
        marriage_date = family["Married"]
        if marriage_date == "NA":
            continue
        marriage_date = datetime.datetime.strptime(marriage_date, "%Y-%m-%d").date()

        husband = family["Husband ID"]
        wife = family["Wife ID"]

        if husband not in individual_dict or wife not in individual_dict:
            continue

        husband_birth = individual_dict[husband]["Birthday"]
        wife_birth = individual_dict[wife]["Birthday"]

        if husband_birth == "NA" or wife_birth == "NA":
            continue

        husband_birth = datetime.datetime.strptime(husband_birth, "%Y-%m-%d").date()
        wife_birth = datetime.datetime.strptime(wife_birth, "%Y-%m-%d").date()

        husband_age_at_marriage = relativedelta(marriage_date, husband_birth).years
        wife_age_at_marriage = relativedelta(marriage_date, wife_birth).years

        older_age = max(husband_age_at_marriage, wife_age_at_marriage)
        younger_age = min(husband_age_at_marriage, wife_age_at_marriage)

        # A younger spouse aged 0 or less makes the "twice as old" ratio undefined; skip.
        if younger_age <= 0:
            continue

        if older_age > 2 * younger_age:
            large_age_gap_families.append(family["ID"])

    if len(large_age_gap_families) > 0:
        print(f"US34: Families where the older spouse was more than twice the younger spouse's age at marriage: {', '.join(large_age_gap_families)}")
