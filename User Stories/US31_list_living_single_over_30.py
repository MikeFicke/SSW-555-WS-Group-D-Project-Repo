# Group D
# SSW-555-WS
# User Story: List living single over 30
# List all living individuals over the age of 30 who have never been married in a GEDCOM file

def validate_list_living_single_over_30(individual_dict):
    living_single = []
    for individual in individual_dict.values():
        if individual["Alive"] and individual["Spouse"] == [] and individual["Age"] != "NA" and individual["Age"] > 30:
            living_single.append(individual["ID"])
    if len(living_single) > 0:
        print(f"US31: Living individuals over 30 who have never been married: {', '.join(living_single)}")
