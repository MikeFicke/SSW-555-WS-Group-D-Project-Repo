# Group D
# SSW-555-WS
# User Story: Corresponding entries (US26)
# Author: Michael Ficke
# Acknowledgement: IDE Auto-complete was used for certain lines of code

"""
This user story checks tha all family roles in the individual record should be
in the family record as well, and vice-versa.

The logic is as follows via cross-reference checks:

- If an individual says Child = @F1@, then family @F1@ must list that individual in its Children list.
- If an individual says Spouse = [@F2@], then family @F2@ must list that individual as Husband ID or Wife ID.
- If a family says Husband ID = @I1@ or Wife ID = @I2@, then that individual must list the family in their Spouse list.
- If a family says Children = [@I3@, @I4@], then each of those individuals must have Child = that family ID.
"""

def validate_corresponding_entries(individuals, families):
    """
    Iterate through all individuals and check for child/spouse consistency with their families.
    Iterate through all families and check for husband/wife/child consistency with their individuals.
    """
    for individual in individuals.values():
        individual_id = individual["ID"]

        # Check 1: Individual is a child in a family
        child_family_id = individual["Child"]
        if child_family_id != "NA":
            # We first checked to make sure that the value existed.  Now, we check to make sure that it matches
            if child_family_id not in families:
                print(f"ERROR: US26: Family ({child_family_id}) referenced by individual ({individual_id}) does not exist.")
            else:
                # Check the ID with the list of children
                if individual_id not in families[child_family_id]["Children"]:
                    print(f"ERROR: US26: Individual ({individual_id}) says they are a child of family ({child_family_id}), but that family does not list them.")
        
        # Check 2: Individual is a spouse in a certain family
        for spouse_family_id in individual["Spouse"]:
            if spouse_family_id not in families:
                print(f"ERROR: US26: Family ({spouse_family_id}) referenced by individual ({individual_id}) does not exist.")
            else:
                # Check the ID with the spouse fields
                if individual_id != families[spouse_family_id]["Husband ID"] and individual_id != families[spouse_family_id]["Wife ID"]:
                    print(f"ERROR: US26: Individual ({individual_id}) says they are a spouse in family ({spouse_family_id}), but that family does not list them as husband or wife.")
        
    # Now we are looking a the family instead of the individual
    for family in families.values():
        family_id = family["ID"]

        # Check 3: Husband check
        husband_id = family["Husband ID"]
        if husband_id != "NA":
            if husband_id not in individuals:
                print(f"ERROR: US26: Individual ({husband_id}) referenced as husband in family ({family_id}) does not exist.")
            else:
                # Check the individual's Spouse list references this family
                if family_id not in individuals[husband_id]["Spouse"]:
                    print(f"ERROR: US26: Family ({family_id}) lists ({husband_id}) as husband, but that individual does not list this family as a spouse.")

        # Check 4: Wife check
        wife_id = family["Wife ID"]
        if wife_id != "NA":
            if wife_id not in individuals:
                print(f"ERROR: US26: Individual ({wife_id}) referenced as wife in family ({family_id}) does not exist.")
            else:
                # Check the individual's Spouse list references this family
                if family_id not in individuals[wife_id]["Spouse"]:
                    print(f"ERROR: US26: Family ({family_id}) lists ({wife_id}) as wife, but that individual does not list this family as a spouse.")

        # Check 5: Children check
        for child_id in family["Children"]:
            if child_id not in individuals:
                print(f"ERROR: US26: Individual ({child_id}) referenced as child in family ({family_id}) does not exist.")
            else:
                # Check the individual's Child field references this family
                if individuals[child_id]["Child"] != family_id:
                    print(f"ERROR: US26: Family ({family_id}) lists ({child_id}) as a child, but that individual does not list this family as their child.")
