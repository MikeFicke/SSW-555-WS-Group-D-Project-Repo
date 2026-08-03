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

        if birthday != "NA":
            individual["Birthday"] = parse_date(birthday)

        if death != "NA":
            individual["Death"] = parse_date(death)

        print(f"US41: INDIVIDUAL ({individual['ID']}): Birthday = {individual['Birthday']}, Death = {individual['Death']}")


    for family in family_dict.values():
        married = family["Married"]
        divorced = family["Divorced"]

        if married != "NA":
            family["Married"] = parse_date(married)

        if divorced != "NA":
            family["Divorced"] = parse_date(divorced)

        print(f"US41: FAMILY ({family['ID']}): Married = {family['Married']}, Divorced = {family['Divorced']}")