# Group D - Sam Bryan
# SSW-555-WS
# User Story: List siblings in families by decreasing age, oldest siblings first (US28)

from datetime import datetime, date


def sort_siblings_by_age(children, individuals):
    """
    Sort a family's list of child IDs by decreasing age (oldest sibling first).

    # args: children is a list of individual IDs belonging to a family
    #       individuals is the dictionary of all individuals in the family tree
    # returns: a new list of the same IDs, ordered oldest to youngest.
    #          Individuals with an unknown ("NA") birthday are placed last,
    #          in their original relative order.
    """
    def birth_date_key(child_id):
        birthday = individuals.get(child_id, {}).get("Birthday", "NA")
        if not birthday or birthday == "NA":
            # Unknown birthday; push to the end (treated as youngest/unknown).
            return date.max
        return datetime.strptime(birthday, "%Y-%m-%d").date()

    # sorted() is stable, so siblings with unknown birthdays keep their
    # original relative order among themselves.
    return sorted(children, key=birth_date_key)
