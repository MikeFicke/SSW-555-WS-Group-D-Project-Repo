# Group D
# SSW-555-WS
# User Story: List Upcoming Birthdays (US38)
# Author: Michael Ficke
# Acknowledgement: IDE Auto-complete was used for certain lines of code

"""
This user story lists all of the individuals that have birthdays within the next 30 days.
The logic in this code will be very similar to US35 and US36.
"""

from datetime import datetime, timedelta

def validate_forthcoming_birthdays(individuals):
    today = datetime.today()
    thirty_day_future = today + timedelta(days=30)
    forthcoming_birthdays = []

    for individual in individuals.values():
        if not individual["Alive"] or individual["Birthday"] == "NA" or individual["Birthday"] == None:
            # Skip; nothing to check
            continue

        birthday = datetime.strptime(individual["Birthday"], "%Y-%m-%d")

        # Check if birthday is within the next 30 days
        birthday_in_future = birthday >= today and birthday <= thirty_day_future

        if birthday_in_future:
            forthcoming_birthdays.append((individual["Name"], individual["Birthday"]))

    # Print the results
    print("Forthcoming Birthdays (Next 30 Days):")
    if forthcoming_birthdays:
        for name, bday in forthcoming_birthdays:
            print(f"{name}: {bday}")
    else:
        print("None")

    return forthcoming_birthdays
