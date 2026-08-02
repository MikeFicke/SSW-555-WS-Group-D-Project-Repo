# Group D - Samantha Bryan
# SSW-555-WS
# User Story: Aunts and uncles should not marry their nieces or nephews

def validate_no_marriage_between_aunt_uncle_and_niece_nephew(family_dict):
    """
    Identify the parent family of each individual (the family in which they are
    listed as a child) and flag any family where one spouse is a sibling of the
    other spouse's parent - i.e. one spouse is the aunt/uncle and the other is
    the niece/nephew.
    """
    parent_family_of = {}
    for family in family_dict.values():
        for child in family["Children"]:
            parent_family_of[child] = family["ID"]

    def are_siblings(person_a, person_b):
        family_a = parent_family_of.get(person_a)
        family_b = parent_family_of.get(person_b)
        return family_a is not None and family_a == family_b

    def is_aunt_or_uncle_of(person, potential_niece_or_nephew):
        parent_family_id = parent_family_of.get(potential_niece_or_nephew)
        if parent_family_id is None:
            return False
        parent_family = family_dict[parent_family_id]
        return (
            are_siblings(person, parent_family["Husband ID"])
            or are_siblings(person, parent_family["Wife ID"])
        )

    for family in family_dict.values():
        husband = family["Husband ID"]
        wife = family["Wife ID"]

        if is_aunt_or_uncle_of(husband, wife) or is_aunt_or_uncle_of(wife, husband):
            print(f"ERROR: FAMILY: US20: {family['ID']}: Husband ({husband}) and Wife ({wife}) are aunt/uncle and niece/nephew")
