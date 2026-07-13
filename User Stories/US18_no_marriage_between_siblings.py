# Group D - Samantha Bryan
# SSW-555-WS
# User Story: Siblings should not marry one another

def validate_no_marriage_between_siblings(family_dict):
    """
    Identify the siblings in each family (the children listed on that family)
    and flag any family where the husband and wife are siblings.
    """
    siblings_by_family = {}
    for family in family_dict.values():
        siblings_by_family[family["ID"]] = set(family["Children"])

    for family in family_dict.values():
        husband = family["Husband ID"]
        wife = family["Wife ID"]

        for sibling_family_id, siblings in siblings_by_family.items():
            if husband in siblings and wife in siblings:
                print(f"ERROR: FAMILY: US18: {family['ID']}: Husband ({husband}) and Wife ({wife}) are siblings from family ({sibling_family_id})")
