# Group D - William Bryce
# SSW-555-WS
# User Story: Siblings spacing
# Birth dates of siblings should be more than 8 months apart or less than 2 days apart (twins may be born one day apart, e.g. 11:59 PM and 12:02 AM the following calendar day)

import datetime
from dateutil.relativedelta import relativedelta
from itertools import combinations

def validate_siblings_spacing(individual_dict, family_dict):
    for family in family_dict.values():
        children = family["Children"]

        if len(children) <= 1:
            # no children or only one child, no siblings to check
            continue

        for sibling1, sibling2 in combinations(children, 2):
            # comparing every sibling to each other
            sib1_birthday = individual_dict[sibling1]["Birthday"]
            sib2_birthday = individual_dict[sibling2]["Birthday"]

            if sib1_birthday == "NA":
                continue
            if sib2_birthday == "NA":
                continue

            sib1_birthday = datetime.datetime.strptime(sib1_birthday, "%Y-%m-%d").date()
            sib2_birthday = datetime.datetime.strptime(sib2_birthday, "%Y-%m-%d").date()

            sibling_diff = relativedelta(max(sib1_birthday, sib2_birthday), min(sib1_birthday, sib2_birthday))
            months_diff = (sibling_diff.years * 12) + sibling_diff.months
            days_diff = (max(sib1_birthday, sib2_birthday) - min(sib1_birthday, sib2_birthday)).days

            if (months_diff < 8 or (months_diff == 8 and sibling_diff.days == 0)) and (days_diff >= 2):
                # sibling birthdays are 2 days to 8 months apart
                print(f"ERROR: FAMILY: US13: {family['ID']}: Siblings ({sibling1} and {sibling2}) have birthdays 2 days to 8 months apart")