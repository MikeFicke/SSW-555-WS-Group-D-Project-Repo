# Group D - Sam Bryan
# SSW-555-WS
# User Story: Marriage Before Death
# Marriage should occur before death of either spouse

import datetime

def validate_marriage_before_death(individual_dict, family_dict):
    """
    Function that checks if a family's spouses' marriage occurs before their death.
    Uses data from the `parse_gedcom` function in `pretty_print.py`.
    """
    for family in family_dict.values():
        marriage_date = family["Married"]
        if marriage_date == "NA":
            continue  # there is no data, skip
        # citation: https://www.google.com/search?q=python+how+to+convert+a+sring+date+to+a+yyyy-mm-dd+format%3F&rlz=1C1CHBF_enUS1023US1023&oq=python+how+to+convert+a+sring+date+to+a+yyyy-mm-dd+format%3F&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQIRgKGKABMgkIAhAhGAoYqwIyCQgDECEYChirAjIHCAQQIRiPAjIHCAUQIRiPAtIBCDkzMDRqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8
        marriage_date = datetime.datetime.strptime(marriage_date, "%Y-%m-%d")
        husband_death_date = individual_dict.get(family["Husband ID"], {}).get("Death", "NA")
        wife_death_date = individual_dict.get(family["Wife ID"], {}).get("Death", "NA")
        if husband_death_date == "NA" and wife_death_date == "NA":
            continue  # there is no data, skip
        # citation: https://www.google.com/search?q=python+how+to+convert+a+sring+date+to+a+yyyy-mm-dd+format%3F&rlz=1C1CHBF_enUS1023US1023&oq=python+how+to+convert+a+sring+date+to+a+yyyy-mm-dd+format%3F&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQIRgKGKABMgkIAhAhGAoYqwIyCQgDECEYChirAjIHCAQQIRiPAjIHCAUQIRiPAtIBCDkzMDRqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8
        if husband_death_date != "NA":
            husband_death_date = datetime.datetime.strptime(husband_death_date, "%Y-%m-%d")
        if wife_death_date != "NA":
            wife_death_date = datetime.datetime.strptime(wife_death_date, "%Y-%m-%d")
        if (husband_death_date and husband_death_date < marriage_date) or (wife_death_date and wife_death_date < marriage_date):
            print(f"ERROR: Death date in family {family['ID']} is before marriage date {marriage_date}")