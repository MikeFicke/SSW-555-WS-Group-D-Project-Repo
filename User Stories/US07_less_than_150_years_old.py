# User story 7, an individual should not be older than 150 years old.
# SSW-555-WS Group D
# Pair programming Duo: Michael Ficke & William Bryce
# Acknowledgement: IDE Auto-complete was used for certain lines of code

# Refactoring: Inconsistent guard clause ordering betwen birthday and end date.
# If left alone, the birthday guard can crash with a TypeError if the birthday value is something other than "" or None.
# Also, the docstring in the for loop can be removed,bas it is unconventional.

from dateutil.relativedelta import relativedelta
from datetime import datetime

def validate_age_less_than_150(individuals):
    """
     This function checks every individual's age and outputs error logs if anyone
     is older than 150 years old.

     # args: individuals is the dictionary of all individuals in the family tree
     # returns: nothing, but prints error logs if any individual is older than 150     
    """
    for individual in individuals.values():
        birthday = individual["Birthday"]
        
        # Possible bug caught.  If the date is "NA" and it is converted, it will cause a crash in the application.

        if not birthday or birthday == "NA":  # Use "not" for all falsy values
            # Skip, since the date is not valid and cannot be checked.
            continue

        birthday = datetime.strptime(birthday, "%Y-%m-%d").date()
        end_date = individual["Death"]

        if not end_date or end_date == "NA":
            # bug caught: swap order of methods
            end_date = datetime.today().date()  # not dead, end date is today's date
        else:
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date() # individual is dead, end date is death date
        
        # bug caught: imprecision when handling date calculations, especially with leap years.
        # citation: https://www.google.com/search?q=how+to+calculate+years+in+Python+using+relativedelta+precisely&rlz=1C1CHBF_enUS1023US1023&oq=how+to+calculate+years+in+Python+using+relativedelta+precisely&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigATIHCAIQIRigATIHCAMQIRigATIHCAQQIRigATIHCAUQIRigATIHCAYQIRiPAjIHCAcQIRiPAtIBCDk2NzJqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8
        if relativedelta(end_date, birthday).years >= 150:
            print(f"ERROR: INDIVIDUAL: {individual['ID']}: Age is 150 years or older.")
