# Group D
# SSW-555-WS
# User Story: List Upcoming Birthdays (US38)
# Author: Michael Ficke
# Acknowledgement: IDE Auto-complete was used for certain lines of code

"""
This user story lists all of the individuals that have birthdays within the next 30 days.
The logic in this code will be very similar to US35 and US36.
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


def validate_forthcoming_birthdays(individuals):
    """
    Lists all living individuals whose birthdays occur in the next 30 days.
    """
    today = datetime.today().date()
    thirty_day_future = today + timedelta(days=30)
    forthcoming_birthdays = []

    for individual in individuals.values():
        if not individual["Alive"] or individual["Birthday"] == "NA" or individual["Birthday"] is None:
            # Skip; nothing to check
            continue

        birthday = datetime.strptime(individual["Birthday"], "%Y-%m-%d").date()

        # Get the next occurrence of this birthday (handles annual recurrence)
        next_birthday = get_next_occurrence(birthday.month, birthday.day, today)

        # Check if next birthday is within the next 30 days (inclusive)
        if today <= next_birthday <= thirty_day_future:
            forthcoming_birthdays.append(individual["ID"])

    # Print the results following project convention
    if len(forthcoming_birthdays) > 0:
        print(f"US38: Upcoming birthdays: {', '.join(forthcoming_birthdays)}")
