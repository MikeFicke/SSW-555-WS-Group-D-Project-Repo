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
    marriage_information = tuple()
    for individual in individuals.values():
        spouse_list = []  # TODO: how to parse the data to get the list of spouses for the first if check
        if len(spouse_list) < 2:
            # cannot have bigamy if there are less than two marriages for an individual
            continue
        
        for family in families:
            if family == "NA" or family is None:
                # Family not found, skip
                continue
            
            family_id = family["ID"]
            marriage_data = family["Marriage"]
            if marriage_data == "NA" or marriage_data is None:
                # No marriage date to look at, Skip.
                continue
            
            divorce_date = family["Divorce"]["End Date"]
            death_date = family["Death"]

            if divorce_date != "NA" or divorce_date is not None:
                # we will use this as the end date in the analysis
                end_date = None
            elif death_date != "NA" or death_date is not None:
                # Use the other spouse's death date as the end date
                end_date = None
            else:
                # This marriage is still active
                end_date = None
            
            marriage_date = datetime.strptime(marriage_data, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
            marriage_dates = marriage_information.append((family_id, marriage_date, end_date))
        
    # Date comparison logic
    for dates in marriage_dates:
        if dates[1] < dates[2] and dates[2] < dates[1]:
            print(f"ERROR: individual {individual['ID']} has overlapping marriages (bigamy) for {dates[0]}, {dates[1]}, {dates[2]}")
