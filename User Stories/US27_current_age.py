# Group D - Sam Bryan
# SSW-555-WS
# User Story: Include individual's current age when listing individuals (US27)

from dateutil.relativedelta import relativedelta
from datetime import datetime


def calculate_current_age(birthday, death):
    """
    Calculate a person's age in whole years as of today, or as of their
    death date if they are deceased.

    # args: birthday is the individual's "Birthday" field ("YYYY-MM-DD" or "NA")
    #       death is the individual's "Death" field ("YYYY-MM-DD" or "NA")
    # returns: the person's age in whole years (int), or "NA" if the birthday is unknown
    """
    if not birthday or birthday == "NA":
        # Skip, since the date is not valid and cannot be checked.
        return "NA"

    birthday = datetime.strptime(birthday, "%Y-%m-%d").date()

    if not death or death == "NA":
        end_date = datetime.today().date()  # not dead, end date is today's date
    else:
        end_date = datetime.strptime(death, "%Y-%m-%d").date()  # individual is dead, end date is death date

    # Use relativedelta for precise age calculation, matching US07's approach.
    return relativedelta(end_date, birthday).years
