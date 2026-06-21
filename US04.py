# Group D - Sam Bryan
# SSW-555-WS
# User Story: Marriage before divorce
# Marriage should occur before divorce of spouses, and divorce can only occur after marriage

import datetime

def validate_marriage_before_divorce(family_dict):
    """
    Function that checks if a family's spouses' marriage occurs before their divorce.
    Uses data from the `parse_gedcom` function in `pretty_print.py`.
    """
    for family in family_dict.values():
        marriage_date = family["Married"]
        if marriage_date == "NA":
            continue  # there is no data, skip
        # citation: https://www.google.com/search?q=python+how+to+convert+a+sring+date+to+a+yyyy-mm-dd+format%3F&rlz=1C1CHBF_enUS1023US1023&oq=python+how+to+convert+a+sring+date+to+a+yyyy-mm-dd+format%3F&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQIRgKGKABMgkIAhAhGAoYqwIyCQgDECEYChirAjIHCAQQIRiPAjIHCAUQIRiPAtIBCDkzMDRqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8
        marriage_date = datetime.datetime.strptime(marriage_date, "%Y-%m-%d")
        divorce_date = family["Divorced"]
        if divorce_date == "NA":
            continue  # there is no data, skip
        # citation: https://www.google.com/search?q=python+how+to+convert+a+sring+date+to+a+yyyy-mm-dd+format%3F&rlz=1C1CHBF_enUS1023US1023&oq=python+how+to+convert+a+sring+date+to+a+yyyy-mm-dd+format%3F&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQIRgKGKABMgkIAhAhGAoYqwIyCQgDECEYChirAjIHCAQQIRiPAjIHCAUQIRiPAtIBCDkzMDRqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8
        divorce_date = datetime.datetime.strptime(divorce_date, "%Y-%m-%d")
        if divorce_date and divorce_date != "NA" and divorce_date < marriage_date:
            print(f"ERROR: Divorce date in family {family['ID']} is before marriage date {marriage_date}")