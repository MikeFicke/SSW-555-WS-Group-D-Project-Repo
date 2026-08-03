# Group D - William Bryce
# SSW-555-WS
# User Story: List orphans
# List all orphaned children (both parents dead and child < 18 years old) in a GEDCOM file

import datetime
from dateutil.relativedelta import relativedelta

def validate_list_orphans(individual_dict, family_dict):
    orphans = []
    for family in family_dict.values():
        husband = family["Husband ID"]
        wife = family["Wife ID"]

        if individual_dict[husband]["Death"] == "NA" or individual_dict[wife]["Death"] == "NA":
            continue    # at least one parent living, skip

        children = family["Children"]
        if children == []:
            continue

        for child in children:
            if "Death" not in individual_dict[child] or individual_dict[child]["Death"] != "NA":
                continue

            birthday = individual_dict[child]["Birthday"]
            birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()

            age = relativedelta(datetime.date.today(), birthday)

            if age.years < 18:
                orphans.append(child)
            
    if orphans != []:
        print(f"US33: Orphans: {', '.join(orphans)}")