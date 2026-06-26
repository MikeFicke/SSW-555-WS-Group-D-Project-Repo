# Michael Ficke
# SSW-555-WS Group D
# User Story: No Bigamy: Marriage should not occur during marriage to another spouse.
# Acknowledgement: Some lines of code were written with IDE auto-complete.

from datetime import datetime

def validate_no_bigamy(individuals, families):
    """
    This function looks at the marriage periods of the spouses that are in families to 
    make sure they are no instances where two marriages are occurring at the same time.
    """

    for individual in individuals.values():
        marriage_information = []
        spouse_list = individual["Spouse"]
        if spouse_list == "NA" or spouse_list is None:
            # Skip, no spouses means there is no chance of bigamy
            continue
        elif len(spouse_list) < 2:
            # cannot have bigamy if there are less than two marriages for an individual
            continue
        
        for family_id in spouse_list:
            family = families[family_id]
            if family == "NA" or family is None:
                # Family not found, skip
                continue
            
            family_id = family["ID"]
            marriage_data = family["Married"]
            if marriage_data == "NA" or marriage_data is None:
                # No marriage date to look at, Skip.
                continue
            
            divorce_date = family["Divorced"]

            # Need to find the death date
            if individual["ID"] == family["Husband ID"]:
                death_id = family["Wife ID"]  # Get the ID of the other spouse
                death_date = individuals.get(death_id, "NA")["Death"]
            elif individual["ID"] == family["Wife ID"]:
                death_id = family["Husband ID"]  # Get the ID of the other spouse
                death_date = individuals.get(death_id, "NA")["Death"]

            if divorce_date != "NA":
                # we will use this as the end date in the analysis
                end_date = divorce_date
            elif death_date != "NA":
                # Use the other spouse's death date as the end date
                end_date = death_date
            else:
                # This marriage is still active
                end_date = None
            
            marriage_date = datetime.strptime(marriage_data, "%Y-%m-%d")

            if end_date is not None:
                end_date = datetime.strptime(end_date, "%Y-%m-%d")

            marriage_information.append((family_id, marriage_date, end_date))
        
        # Date comparison logic
        i = 0
        while i < len(marriage_information):
            j = i + 1
            while j < len(marriage_information):
                family_id_1, start_date_1, end_date_1 = marriage_information[i]
                family_id_2, start_date_2, end_date_2 = marriage_information[j]
                # The logic is that if two date ranges overlap (start1 < end 2 AND start2 < end1), then there is bigamy
                # We check for nulls here in case there are marriages that have not ended yet to address that edge case, which will fail if not considered
                if ((end_date_2 is None) or start_date_1 < end_date_2) and ((end_date_1 is None) or start_date_2 < end_date_1):
                    print(f"ERROR: Bigamy found. Individual {individual['ID']} has two overlapping marriages {family_id_1} and {family_id_2}.")
                j += 1
            i += 1
