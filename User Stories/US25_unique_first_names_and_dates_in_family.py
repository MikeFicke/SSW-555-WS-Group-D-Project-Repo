# Group D
# SSW-555-WS
# User Story: Unique names and dates in each family
# Author: Michael Ficke
# Acknowledgement: IDE Auto-complete was used for certain lines of code

"""
No two children can have the same first name and be born on the same date.
"""

def validate_unique_first_names_in_families(individuals, families):
    """
    Function that parses through the individuals and families dictionaries
    and uses a tracker to group children by their birthdays and names, performs a comparison, and 
    prints an error if there are duplicates found.
    """
    for family in families.values():
        # dictionary for children that we parsed with a KV-pair of (name, birthday) to ID
        children = {}
        # iterate through each child in the family
        for child_id in family["Children"]:
            # Look up the name and birthday of the child
            name = individuals[child_id]["Name"]
            birthday = individuals[child_id]["Birthday"]
            
            # Collect duplicates
            if (name, birthday) in children:
                children[(name, birthday)].append(child_id)
            else:
                children[(name, birthday)] = [child_id]

        # Identify duplicates and print errors accordingly
        for (name, birthday), ids in children.items():
            if len(ids) >= 2:  # Duplicates found
                id_list = ', '.join(ids)  # Format the list of duplicate IDs for the error message
                print(f"ERROR: US25: FAMILY ({family['ID']}): Children ({id_list}) share the same name ({name}) and birth date ({birthday}).")
