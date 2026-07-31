# Group D
# SSW-555-WS
# User Story: List Upcoming Anniversaries (US39)
# Author: Michael Ficke
# Acknowledgement: IDE Auto-complete was used for certain lines of code

"""
This user story lists the upcoming anniversaries of individuals that are alive and married.
The logic for this user story will be similar to US38.
"""

from datetime import datetime, timedelta, date


def get_next_occurrence(month, day, today):
    """
    Given a month and day, return the next occurrence of that date
    on or after today. Handles year wrap-around (e.g., Dec to Jan)
    and Feb 29 in non-leap years.
    """
    # citation: https://www.google.com/search?q=python+date+replace+year+leap+year+feb+29
    try:
        current_year_date = date(today.year, month, day)
    except ValueError:
        # Feb 29 in a non-leap year; fall back to Feb 28
        current_year_date = date(today.year, 2, 28)

    if current_year_date < today:
        # Already passed this year; next occurrence is next year
        try:
            return date(today.year + 1, month, day)
        except ValueError:
            return date(today.year + 1, 2, 28)
    return current_year_date


def validate_upcoming_anniversaries(individuals, families):
    """
    Lists all living, currently married (not divorced) couples whose
    marriage anniversaries occur in the next 30 days.
    """
    today = datetime.today().date()
    upcoming_thirty_days = today + timedelta(days=30)
    upcoming_anniversaries = []

    for family in families.values():
        # Must have a marriage date
        if family["Married"] == "NA" or family["Married"] is None:
            # Skip; nothing to check.
            continue
        # Extra check for divorced couples; they do not celebrate anniversaries.
        if family["Divorced"] != "NA" and family["Divorced"] is not None:
            # Skip; nothing to check.
            continue

        husband_id = family["Husband ID"]
        wife_id = family["Wife ID"]

        # Both spouses need to exist in the individuals dict
        if husband_id not in individuals or wife_id not in individuals:
            # Skip; nothing to check.
            continue

        # Both spouses need to be alive to celebrate an anniversary.
        if not individuals[husband_id]["Alive"] or not individuals[wife_id]["Alive"]:
            # Skip; nothing to check.
            continue

        marriage_date = datetime.strptime(family["Married"], "%Y-%m-%d").date()
        next_anniversary = get_next_occurrence(marriage_date.month, marriage_date.day, today)

        if today <= next_anniversary <= upcoming_thirty_days:
            upcoming_anniversaries.append(family["ID"])

    # Print the results following project convention
    if len(upcoming_anniversaries) > 0:
        print(f"US39: Upcoming anniversaries: {', '.join(upcoming_anniversaries)}")
