# Group D - Michael Ficke
# SSW-555-WS
# User Story: All male children have the same last name

# Acknowledgement: IDE auto-complete was used for certain lines of code

import re

def get_last_name_helper(full_name):
    """
    This is a helper function that attempts to extract the last name from a 
    person's full name using regex.
    """

    if full_name == "NA" or full_name == "" or full_name == None:
        # nothing to check, return none to skip
        return None

    
    # Look for '/' characters to split the names since surnames are stored as "<first name> '/'<last name>/"
    if '/' in full_name:
        extracted_name = re.search(r"/(.+)/", full_name)
        return extracted_name.group(1)
    else:
        # split by spaces as fallback
        extracted_name = full_name.split(" ")
        if extracted_name is not None and extracted_name != "":
            return extracted_name[-1]  # the last index should be the last name
    


def validate_male_last_names(individual_dict, family_dict):
    """
    Function to check that all males in a family share the same last name.
    The husband ID needs to be retrieved first so we can get the proper last name.
    Then we need to get the children IDs and do a last name check on the males only.
    """
    for family in family_dict:
        # Get the husband's ID to perform a lookup
        husband_id = family_dict[family]['Husband ID']
        if husband_id == "" or husband_id == "NA" or husband_id is None:
            # skip, we cannot check
            continue

        # Get the husband's name next
        husband_name = individual_dict[husband_id]['Name']
        if husband_name == "NA" or husband_name == "" or husband_name is None:
            # skip, we cannot check
            continue

        # Get the expected last name
        husband_last_name = get_last_name_helper(husband_name)
        
        # Get the children IDs next to perform lookups
        children_ids = family_dict[family]['Children']
        if children_ids is None or children_ids == []:
            # skip, we cannot check
            continue

        # Iterate over the children, identify the males, and then compare their last names to the father's last name
        for child in children_ids:
            child_gender = individual_dict[child]['Gender']
            if child_gender == "NA" or child_gender == "" or child_gender is None or child_gender == "F":
                # skip, we cannot check
                continue

            child_name = individual_dict[child]['Name']
            if child_name == "NA" or child_name == "" or child_name is None:
                # skip, we cannot check
                continue
            
            # at this point we should only have males left
            child_last_name = get_last_name_helper(child_name)
            if child_last_name == "NA" or child_last_name == "" or child_last_name is None:
                # skip, we cannot check
                continue
            
            if child_last_name != husband_last_name:
                print(f"ERROR: US16: {child_name}'s last name '{child_last_name}' does not match the husband's last name '{husband_last_name}'")
            