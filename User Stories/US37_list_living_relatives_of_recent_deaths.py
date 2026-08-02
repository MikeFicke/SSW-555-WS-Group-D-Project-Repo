# Group D - Sam Bryan
# SSW-555-WS
# User Story: List Living Spouses and Descendants of Recent Deaths (US37)

"""
This user story lists all living spouses and descendants of individuals who
died within the last 30 days. The "recent death" logic is the same as US36.
"""

from datetime import datetime, timedelta


def get_spouses(person_id, individuals, families):
    """Return the set of the given person's spouse IDs (from all of their FAMS families)."""
    spouses = set()
    person = individuals.get(person_id)
    if not person:
        return spouses

    for fam_id in person["Spouse"]:
        family = families.get(fam_id)
        if not family:
            continue

        husband = family["Husband ID"]
        wife = family["Wife ID"]

        if person_id == husband and wife != "NA":
            spouses.add(wife)
        elif person_id == wife and husband != "NA":
            spouses.add(husband)

    return spouses


def get_descendants(person_id, individuals, families):
    """Return the set of all of the given person's descendant IDs (children, grandchildren, etc.)."""
    descendants = set()
    visited = {person_id}
    stack = [person_id]

    while stack:
        current = stack.pop()
        person = individuals.get(current)
        if not person:
            continue

        for fam_id in person["Spouse"]:
            family = families.get(fam_id)
            if not family:
                continue

            for child_id in family["Children"]:
                if child_id not in visited:
                    visited.add(child_id)
                    descendants.add(child_id)
                    stack.append(child_id)

    return descendants


def validate_living_relatives_of_recent_deaths(individuals, families):
    """
    Lists all living spouses and descendants of individuals who died within the last 30 days.
    """
    today = datetime.today().date()
    thirty_days_ago = today - timedelta(days=30)

    living_relatives = set()

    for individual in individuals.values():
        death_string = individual["Death"]
        if death_string == "NA" or death_string is None:
            # Skip; this individual is not deceased.
            continue

        death_date = datetime.strptime(death_string, "%Y-%m-%d").date()

        if not (thirty_days_ago <= death_date <= today):
            # Skip; this individual did not die within the last 30 days.
            continue

        decedent_id = individual["ID"]
        relatives = get_spouses(decedent_id, individuals, families) | get_descendants(decedent_id, individuals, families)

        for relative_id in relatives:
            relative = individuals.get(relative_id)
            if relative and relative["Alive"]:
                living_relatives.add(relative_id)

    if len(living_relatives) > 0:
        sorted_relatives = sorted(living_relatives, key=lambda x: int(x[2:-1]))
        print(f"US37: Living spouses and descendants of recently deceased individuals: {', '.join(sorted_relatives)}")
