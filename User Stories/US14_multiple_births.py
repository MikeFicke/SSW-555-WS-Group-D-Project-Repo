# Group D - Michael Ficke
# SSW-555-WS
# User Story: No more than five siblings should be born at the same time.

# Acknowledgement: IDE auto-complete was used for certain lines of code

def validate_multiple_births(individual_dict, family_dict):
    """
    Check to make sure that no more than five siblings are born at the same time.
    """
    for family in family_dict:
        children_ids = family_dict[family].get("Children")

        if children_ids == [] or children_ids == None:
            # skip, as there are no children to check for
            continue
        
        children_birthdays = {}
        for child in children_ids:
            child_birthday = individual_dict[child].get("Birthday")
            if child_birthday == "NA" or child_birthday == None:
                # skip, there is no birthday to look at
                continue
            if child_birthday in children_birthdays:
                children_birthdays[child_birthday].append(child)
            else:
                children_birthdays[child_birthday] = [child]

        for birthday, children in children_birthdays.items():
            if len(children) > 5:
                print(f"ERROR: US14: Family {family} has more than 5 children born on the same day ({birthday})")
