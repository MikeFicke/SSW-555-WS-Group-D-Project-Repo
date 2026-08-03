# Group D - William Bryce
# SSW-555-WS
# User Story: Reject illegitimate dates
# All dates should be legitimate dates for the months

import datetime

def illegitimate_date(date_str):
    # If US41 has already parsed the date string into a datetime.date object,
    # it is by definition a legitimate date — skip strptime.
    if isinstance(date_str, (datetime.date, datetime.datetime)):
        return False
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        return False
    except  ValueError:
        return True

def validate_reject_illegitimate_dates(individual_dict, family_dict):
    for individual in individual_dict.values():
        birthday = individual["Birthday"]
        death = individual["Death"]

        if birthday != "NA" and illegitimate_date(birthday):
            print(f"ERROR: US42: INDIVIDUAL ({individual['ID']}): Invalid date for birthday, {birthday}")

        if death != "NA" and illegitimate_date(death):
            print(f"ERROR: US42: INDIVIDUAL ({individual['ID']}): Invalid date for death, {death}")

    for family in family_dict.values():
        married = family["Married"]
        divorced = family["Divorced"]

        if married != "NA" and illegitimate_date(married):
            print(f"ERROR: US42: FAMILY ({family['ID']}): Invalid date for marriage, {married}")

        if divorced != "NA" and illegitimate_date(divorced):
            print(f"ERROR: US42: FAMILY ({family['ID']}): Invalid date for divorce, {divorced}")

        