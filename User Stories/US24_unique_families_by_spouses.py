# Group D - William Bryce
# SSW-555-WS
# User Story: Unique families by spouses
# No more than one family with the same spouses by name and the same marriage date should appear in a GEDCOM file

def validate_unique_families_by_spouses(individual_dict, family_dict):
    unique_spouse_marriages = {}
    for family in family_dict.values():
        husband = individual_dict[family["Husband ID"]]["Name"]
        wife = individual_dict[family["Wife ID"]]["Name"]

        marriage_date = family["Married"]

        if (husband, wife, marriage_date) in unique_spouse_marriages:
            unique_spouse_marriages[(husband, wife, marriage_date)].append(family["ID"])
        else:
            unique_spouse_marriages[(husband, wife, marriage_date)] = [family["ID"]]

    for spouses_marriage in unique_spouse_marriages:
        if len(unique_spouse_marriages[spouses_marriage]) >= 2:
            fam_ids = ', '.join(unique_spouse_marriages[spouses_marriage])
            print(f"ERROR: US23: FAMILIES ({fam_ids}): More than one family with the same husband ({spouses_marriage[0]}), wife ({spouses_marriage[1]}), and marriage date ({spouses_marriage[2]}).")
