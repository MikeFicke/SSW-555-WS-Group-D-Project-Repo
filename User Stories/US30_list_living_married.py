# Group D - William Bryce
# SSW-555-WS
# User Story: List living married
# List all living married people in a GEDCOM file

def validate_list_living_married(individual_dict):
    living_married = []
    for individual in individual_dict.values():
        if individual["Alive"] and individual["Spouse"] != []:
            living_married.append(individual["ID"])
    if len(living_married) > 0:
        print(f"US30: Living married individuals: ${", ".join(living_married)}")