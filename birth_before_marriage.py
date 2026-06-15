# Group D - Michael Ficke
# SSW-555-WS
# User Story: Birth before marriage
# Birth should occur before marriage of an individual

import datetime

def birth_before_marriag(individual_dict, family_dict):
    """
    Function that checks if a family's spouses' birthdates occur before their marriage.
    Uses data from the `parse_gedcom` function in `pretty_print.py`.
    """
    for family in family_dict:
        marriage_date = family["Marrid"]  # TODO: we need to get every marriage that the user had, not just one
        if marriage_date == "NA":
            continue  # there is no data, skip
        # citation: https://www.google.com/search?q=python+how+to+convert+a+sring+date+to+a+yyyy-mm-dd+format%3F&rlz=1C1CHBF_enUS1023US1023&oq=python+how+to+convert+a+sring+date+to+a+yyyy-mm-dd+format%3F&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQIRgKGKABMgkIAhAhGAoYqwIyCQgDECEYChirAjIHCAQQIRiPAjIHCAUQIRiPAtIBCDkzMDRqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8
        marriage_date = datetime.datetime.strftime(marriage_date, "%Y-%m-%d")
        husband_id = family["Husband ID"]
        wife_id = family["Wife ID"]
        if not husband_id or husband_id == "NA" or husband_id not in family:
            continue  # Husband not found, skip
        husband_birthday = family[husband_id]["Birthday"]
        if not husband_birthday or husband_birthday == "NA":
            continue  # Husband's birthday not found, skip
        # citation: https://www.google.com/search?q=python+how+toconvert+a+string+into+a+date&rlz=1C1CHBF_enUS1023US1023&oq=python+how+toconvert+a+string+into+a+date&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yCAgCEAAYFhgeMggIAxAAGBYYHjIICAQQABgWGB4yCAgFEAAYFhgeMggIBhAAGBYYHjIICAcQABgWGB4yCAgIEAAYFhgeMggICRAAGBYYHtIBCDQ1MzJqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8
        husband_birthday = datetime.strptime(husband_birthday, "%Y-%m-%d")
        if husband_birthday >= marriage_date:
            print(f"ERROR: Husband's birthday in family {family['Family ID']} is after marriage date {marriage_date}")
        if not wife_id or wife_id == "NA" or husband_id not in family:
            continue  # Wife not found, skip
        wife_birthday = family[wife_id]["Birthday"]
        if not wife_birthday or wife_birthday == "NA":
            continue  # Wife's birthday not found, skip
        wife_birthday = datetime.strptime(wife_birthday, "%Y-%m-%d")
        if wife_birthday >= marriage_date:
            print(f"ERROR: Wife's birthday in family {family['Family ID']} is after marriage date {marriage_date}")
