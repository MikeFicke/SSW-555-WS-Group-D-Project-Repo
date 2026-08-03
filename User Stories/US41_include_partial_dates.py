# Group D - William Bryce
# SSW-555-WS
# User Story: Include partial dates
# Accept and use dates without days or without days and months

import datetime

def parse_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except  ValueError:
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m").date()
        except  ValueError:
            try:
                return datetime.datetime.strptime(date_str, "%Y").date()
            except  ValueError:
                return "NA"


def validate_include_partial_dates(individual_dict, family_dict):
    for individual in individual_dict.values():
        birthday = individual["Birthday"]
        death = individual["Death"]

        # Parse dates for display only — do NOT mutate the shared dict
        parsed_birthday = parse_date(birthday) if birthday != "NA" else "NA"
        parsed_death = parse_date(death) if death != "NA" else "NA"

        print(f"US41: INDIVIDUAL ({individual['ID']}): Birthday = {parsed_birthday}, Death = {parsed_death}")


    for family in family_dict.values():
        married = family["Married"]
        divorced = family["Divorced"]

        # Parse dates for display only — do NOT mutate the shared dict
        parsed_married = parse_date(married) if married != "NA" else "NA"
        parsed_divorced = parse_date(divorced) if divorced != "NA" else "NA"

        print(f"US41: FAMILY ({family['ID']}): Married = {parsed_married}, Divorced = {parsed_divorced}")