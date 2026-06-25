# User story 7, an individual should not be older than 150 years old.
# SSW-555-WS Group D
# Pair programming Duo: Michael Ficke & William Bryce
# Acknowledgement: IDE Auto-complete was used for certain lines of code

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
        # TODO: Implement logic here
        """
        Inside this loop, we need to get the individual's birthday string.
        The birthday needs to be converted into a string so it can be analyzed.
        The "end" date is then needed for each individual.
        If the person is dead, that is their end date.  If they are still alive, their end date is today's date.
        The age in years will be need to be calculated from those dates.
        Finally, check against the 150 year old rule.
        Output error logs if they are >= 150 years old.

        Note: Testing and output logs in main.py will be necessary as well.
        """
        birthday = individual["Birthday"]
        birthday = datetime.strptime(birthday, "%Y-%m-%d").date()
        
        end_date = individual["Death"]
        if not end_date or end_date == "NA":
            end_date = datetime.date.today()  # not dead, end date is today's date
        else:
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date() # individual is dead, end date is death date
        
        if end_date.year - birthday.year >= 150:
            print(f"ERROR: INDIVIDUAL: {individual['ID']}: Age is 150 years or older")
        
