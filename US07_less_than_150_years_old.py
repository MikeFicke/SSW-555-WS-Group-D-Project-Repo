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
        
        # Possible bug caught.  If the date is "NA" and it is converted, it will cause a crash in the application.

        if birthday == "NA" or birthday is None:
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
