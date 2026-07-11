# Group D - William Bryce
# SSW-555-WS
# User Story: No marriages to descendants
# Parents should not marry any of their descendants

def get_descendants(indi, all_children):
    # get the descendants of given individual
    descendants = set()
    queue = all_children.get(indi, []).copy()

    while queue:
        current = queue.pop(0)

        if current not in descendants:
            descendants.add(current)
            queue.extend(all_children.get(current, []))

    return descendants

def validate_no_marriages_to_descendants(family_dict):
    # get all parent-children relations
    all_children = {}
    for family in family_dict.values():
        husband = family["Husband ID"]
        wife = family["Wife ID"]
        children = family["Children"]

        if not children or children == []:
            # no descendants
            continue
        
        for parent in (husband, wife):
            if parent not in all_children:
                all_children[parent] = children.copy()
            else:
                all_children[parent].extend(children)
            
    for family in family_dict.values():
        husband = family["Husband ID"]
        wife = family["Wife ID"]

        husband_descendants = get_descendants(husband, all_children)
        if wife in husband_descendants:
            print(f"ERROR: FAMILY: US17: {family['ID']}: Husband ({husband}) married to descendant ({wife})")

        wife_descendants = get_descendants(wife, all_children)
        if husband in wife_descendants:
            print(f"ERROR: FAMILY: US17: {family['ID']}: Wife ({wife}) married to descendant ({husband})")
