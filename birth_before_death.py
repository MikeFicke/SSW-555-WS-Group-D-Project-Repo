# TODO make sure to show evidence by logging that the test file that we create passed
# TODO both files -> better error catching

import datetime

def validate_birth_before_death(individuals):
    """
    Verify that an individual's birth date is always before their death date.
    This uses the individuals dictionary from the parse_gedcom() function in pretty_print.py.
    """
    for individual in individuals.values():
        birthday = individual["Birthday"]
        if not birthday or birthday == "NA":
            continue  # skip, nothing to compare
        death_date = individual["Death"]
        if not death_date or death_date == "NA":
            continue  # skip, nothing to compare (not necessarily an error in data quality; this person might not have died yet)
        # convert into datetime dates
        birth_date = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()
        death_date = datetime.datetime.strptime(death_date, "%Y-%m-%d").date()
        if birth_date >= death_date:
            print(f"ERROR: Birth date {birth_date} is after or the same as death date {death_date} for individual {individual['ID']}")
        
