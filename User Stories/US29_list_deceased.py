# Group D - William Bryce
# SSW-555-WS
# User Story: List deceased
# List all deceased individuals in a GEDCOM file

def validate_list_deceased(individual_dict):
    deceased = []
    for individual in individual_dict.values():
        if individual["Alive"] == False:
           deceased.append(individual["ID"])
    if len(deceased) > 0:
        print(f"US29: Deceased Individuals: ${", ".join(deceased)}")