# Group D - William Bryce
# SSW-555-WS
# User Story: Dates before current date
# Dates (birth, marriage, divorce, death) should not be after the current date

import datetime

def validate_dates_before_current_date(individual_dict, family_dict):
    current_date = datetime.date.today()
    for individual in individual_dict.values():
        birth_date = individual["Birthday"]
        death_date = individual["Death"]
        if birth_date and birth_date != "NA":
            birth_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d").date()
            if birth_date > current_date:
                print(f"ERROR: INDIVIDUAL: US01: {individual['ID']}: Birthday {birth_date} occurs in the future")
        if death_date and death_date != "NA":
            death_date = datetime.datetime.strptime(death_date, "%Y-%m-%d").date()
            if death_date > current_date:
                print(f"ERROR: INDIVIDUAL: US01: {individual['ID']}: Death {death_date} occurs in the future")
    for family in family_dict.values():
        marriage_date = family["Married"]
        divorce_date = family["Divorced"]
        if marriage_date and marriage_date != "NA":
            marriage_date = datetime.datetime.strptime(marriage_date, "%Y-%m-%d").date()
            if marriage_date > current_date:
                print(f"ERROR: FAMILY: US01: {family['ID']}: Marriage date {marriage_date} occurs in the future")
        if divorce_date and divorce_date != "NA":
            divorce_date = datetime.datetime.strptime(divorce_date, "%Y-%m-%d").date()
            if divorce_date > current_date:
                print(f"ERROR: FAMILY: US01: {family['ID']}: Divorce date {divorce_date} occurs in the future")
                
