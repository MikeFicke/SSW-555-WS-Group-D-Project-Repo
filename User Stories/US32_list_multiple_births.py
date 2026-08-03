# Group D - William Bryce
# SSW-555-WS
# User Story: List multiple births
# List all multiple births in a GEDCOM file

import datetime
from dateutil.relativedelta import relativedelta

def validate_list_multiple_births(individual_dict, family_dict):
    for family in family_dict.values():
        children = family["Children"]

        if len(children) <= 1:
            continue

        birth_dates = {}
        for child in children:
            birthday = individual_dict[child]["Birthday"]
            birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()

            birth_dates[child] = birthday

        birth_dates = dict(sorted(birth_dates.items(), key=lambda item: item[1]))
        multiple_births = []
        current_group = []
        current_id = None
        current_birth = None
        for id, birth in birth_dates.items():
            if current_id is None and current_birth is None:
                current_id = id
                current_birth = birth
                current_group = [id]
            else:
                if birth < (current_birth + relativedelta(days=2)):
                    current_group.append(id)
                else:
                    if len(current_group) > 1:
                        multiple_births.append(current_group)
                    current_group = [id]

            current_id = id
            current_birth = birth

        if len(current_group) > 1:
            multiple_births.append(current_group)

        for group in multiple_births:
            print(f"US32: {family['ID']}: Multiple births: {', '.join(group)}")
            
