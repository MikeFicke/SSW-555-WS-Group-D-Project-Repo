# Group D - William Bryce
# SSW-555-WS
# User Story: Unique name and birth date
# No more than one individual with the same name and birth date should appear in a GEDCOM file

def validate_unique_name_and_birth_date(individual_dict):
    unique_name_birth = {}
    for individual in individual_dict.values():
        name = individual["Name"]
        birthday = individual["Birthday"]

        if (name, birthday) in unique_name_birth:
            unique_name_birth[(name, birthday)].append(individual["ID"])
        else:
            unique_name_birth[(name, birthday)] = [individual["ID"]]

    for name_birth in unique_name_birth:
        if len(unique_name_birth[name_birth]) >= 2:
            ids = ', '.join(unique_name_birth[name_birth])
            print(f"ERROR: US23: INDIVIDUALS ({ids}): More than one individual with name ({name_birth[0]}) and birth date ({name_birth[1]}).")
