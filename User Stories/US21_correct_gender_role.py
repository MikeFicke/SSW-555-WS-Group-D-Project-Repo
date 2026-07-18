# Group D
# SSW-555-WS
# User Story: Correct gender for role
# Husbands should be male, wives should be female.
# Author: Michael Ficke
# Acknowledgement: IDE Auto-complete was used for certain lines of code

def validate_correct_gender_role(individual_dict, family_dict):
    """
    For every family, check if the husband has a 'M' gender, and the wife
    has a 'F' gender.  An error is printed if either of these rules is broken.
    """
    for family_id in family_dict:
        husband_id = family_dict[family_id]['Husband ID']
        wife_id = family_dict[family_id]['Wife ID']
        
        # Check to see if husband ID is null
        if husband_id != "NA" and husband_id != "" and husband_id != None:
            husband_gender = individual_dict[husband_id]['Gender']
            if husband_gender != 'M':
                print(f"Error: Husband in family {family_id} is not male.")

        # Check to see if wife ID is null
        if wife_id != "NA" and wife_id != "" and wife_id != None:
            wife_gender = individual_dict[wife_id]['Gender']
            if wife_gender != 'F':
                print(f"Error: Wife in family {family_id} is not female.")
