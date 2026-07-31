# Group D
# SSW-555-WS
# User Story: List Upcoming Anniversaries (US39)
# Author: Michael Ficke
# Acknowledgement: IDE Auto-complete was used for certain lines of code

"""
This user story lists the upcoming anniversies of individuals tha are alive and married.
The logic for this user story will be similar to US38.
"""

from datetime import datetime, timedelta

def validate_upcoming_anniversaries(individuals, families):
    today = datetime.today()
    upcoming_thirty_days = today + timedelta(days=30)
    upcoming_anniversaries = []

    for family in family.values():
        if not family["Married"] or family["Married"] == "NA" or family["Married"] == None:
            # Skip; nothing to check.
            continue
        # Extra check for divorced couples; they do not celebrate anniversaries.
        if family["Divorced"] is not None or family["Divorced"] != "NA"
            # Skip; nothing to check.
            continue

        husband_id = family["Husband ID"]
        wife_id = family["Wife ID"]

        # Both spouses need to be alive to celebrate an anniversary.
        if husband_id not in individuals or wife_id not in individuals:
            # Skip; nothing to check.
            continue

        if not individuals[husband_id]["Alive"] or not individuals[wife_id]["Alive"]:
            # Skip; nothing to check.
            continue
    
        marriage_date = datetime.strptime(family["Married"], "%d-%b-%Y")
        anniversary_date = marriage_date.replace(year=today.year)

        if today <= anniversary_date <= upcoming_thirty_days:
            upcoming_anniversaries.append((
                family["Family ID"],
                f"{individuals[husband_id]['Name']} and {individuals[wife_id]['Name']}",
                anniversary_date.strftime("%d-%b-%Y")
            ))

    if upcoming_anniversaries != []:
        print(f"US39: Upcoming Anniversaries")
        for anniversary in upcoming_anniversaries:
            print(f"{anniversary[1]} will be celebrating their anniversary on {anniversary[2]}")

    else:
        print("US39: No anniversaries coming up in the next 30 days.")
