# Group D - Samantha Bryan
# SSW-555-WS
# User Story: First cousins should not marry one another

def validate_no_marriage_between_first_cousins(family_dict):
    """
    Identify the parent family of each individual (the family in which they are
    listed as a child) and flag any family where the husband and wife are first
    cousins - i.e. a parent of the husband and a parent of the wife are siblings
    (children of the same family).
    """
    parent_family_of = {}
    for family in family_dict.values():
        for child in family["Children"]:
            parent_family_of[child] = family["ID"]

    def are_siblings(person_a, person_b):
        family_a = parent_family_of.get(person_a)
        family_b = parent_family_of.get(person_b)
        return family_a is not None and family_a == family_b

    for family in family_dict.values():
        husband = family["Husband ID"]
        wife = family["Wife ID"]

        husband_parent_family_id = parent_family_of.get(husband)
        wife_parent_family_id = parent_family_of.get(wife)

        if husband_parent_family_id is None or wife_parent_family_id is None:
            continue
        if husband_parent_family_id == wife_parent_family_id:
            continue  # husband and wife are siblings, not cousins - handled by US18

        husband_parent_family = family_dict[husband_parent_family_id]
        wife_parent_family = family_dict[wife_parent_family_id]

        is_first_cousins = any(
            are_siblings(husband_parent, wife_parent)
            for husband_parent in (husband_parent_family["Husband ID"], husband_parent_family["Wife ID"])
            for wife_parent in (wife_parent_family["Husband ID"], wife_parent_family["Wife ID"])
        )

        if is_first_cousins:
            print(f"ERROR: FAMILY: US19: {family['ID']}: Husband ({husband}) and Wife ({wife}) are first cousins")
