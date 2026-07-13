# Group D - Sam Bryan
# SSW-555-WS
# User Story: Fewer than 15 siblings
# There should be fewer than 15 siblings in a family

def validate_fewer_than_15_siblings(family_dict):
    """
    Identify the siblings in each family (the children listed on that family)
    and flag any family with 15 or more siblings.
    """
    for family in family_dict.values():
        siblings = family["Children"]

        if len(siblings) >= 15:
            print(f"ERROR: US15: Family ({family['ID']}) has {len(siblings)} siblings, which is 15 or more")
