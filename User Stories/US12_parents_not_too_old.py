# Group D - William Bryce
# SSW-555-WS
# User Story: Parents not too old
# Mother should be less than 60 years older than her children and father should be less than 80 years older than his children

import datetime
from dateutil.relativedelta import relativedelta

def validate_parents_not_too_old(individual_dict, family_dict):
    for family in family_dict.values():
        father = family["Husband ID"]
        mother = family["Wife ID"]
        children = family["Children"]

        if children == []:
            continue

        father_birth = individual_dict[father]["Birthday"]
        mother_birth = individual_dict[mother]["Birthday"]

        if father_birth == "NA":
            continue
        if mother_birth == "NA":
            continue

        father_birth = datetime.datetime.strptime(father_birth, "%Y-%m-%d").date()
        mother_birth = datetime.datetime.strptime(mother_birth, "%Y-%m-%d").date()

        for child in children:
            child_birth = individual_dict[child]["Birthday"]

            if child_birth == "NA":
                continue

            child_birth = datetime.datetime.strptime(child_birth, "%Y-%m-%d").date()

            father_diff = relativedelta(child_birth, father_birth)

            if father_diff.years >= 80:
                print(f"ERROR: US12: Father ({father}) is 80 or more years older than child ({child})")

            mother_diff = relativedelta(child_birth, mother_birth)

            if mother_diff.years >= 60:
                print(f"ERROR: US12: Mother ({mother}) is 60 or more years older than child ({child})")