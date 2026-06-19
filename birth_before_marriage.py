# Group D - Michael Ficke
# SSW-555-WS
# User Story: Birth before marriage
# Birth should occur before marriage of an individual

import datetime

def validate_birth_before_marriage(individual_dict, family_dict):
    """
    Function that checks if a family's spouses' birthdates occur before their marriage.
    Uses data from the `parse_gedcom` function in `pretty_print.py`.
    """
    for family in family_dict.values():
        marriage_date = family["Married"]
        if marriage_date == "NA":
            continue  # there is no data, skip
        # citation: https://www.google.com/search?q=python+how+to+convert+a+sring+date+to+a+yyyy-mm-dd+format%3F&rlz=1C1CHBF_enUS1023US1023&oq=python+how+to+convert+a+sring+date+to+a+yyyy-mm-dd+format%3F&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQIRgKGKABMgkIAhAhGAoYqwIyCQgDECEYChirAjIHCAQQIRiPAjIHCAUQIRiPAtIBCDkzMDRqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8
        marriage_date = datetime.datetime.strptime(marriage_date, "%Y-%m-%d")
        husband_id = family["Husband ID"]
        wife_id = family["Wife ID"]
        if husband_id and husband_id != "NA" and husband_id in individual_dict:
            husband_birthday = individual_dict[husband_id]["Birthday"]
            if husband_birthday and husband_birthday != "NA":
                # citation: https://www.google.com/search?q=python+how+to+convert+a+string+into+a+date&rlz=1C1CHBF_enUS1023US1023&oq=python+how+toconvert+a+string+into+a+date&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yCAgCEAAYFhgeMggIAxAAGBYYHjIICAQQABgWGB4yCAgFEAAYFhgeMggIBhAAGBYYHjIICAcQABgWGB4yCAgIEAAYFhgeMggICRAAGBYYHtIBCDQ1MzJqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8
                husband_birthday = datetime.datetime.strptime(husband_birthday, "%Y-%m-%d")
                if husband_birthday >= marriage_date:
                    print(f"ERROR: Husband's birthday in family {family['ID']} is after marriage date {marriage_date}")
        if wife_id and wife_id != "NA" and wife_id in individual_dict:
            wife_birthday = individual_dict[wife_id]["Birthday"]
            if wife_birthday and wife_birthday != "NA":
                # citation: https://www.google.com/search?q=python+how+to+convert+a+string+into+a+date&rlz=1C1CHBF_enUS1023US1023&oq=python+how+toconvert+a+string+into+a+date&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yCAgCEAAYFhgeMggIAxAAGBYYHjIICAQQABgWGB4yCAgFEAAYFhgeMggIBhAAGBYYHjIICAcQABgWGB4yCAgIEAAYFhgeMggICRAAGBYYHtIBCDQ1MzJqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8
                wife_birthday = datetime.datetime.strptime(wife_birthday, "%Y-%m-%d")
                if wife_birthday >= marriage_date:
                    print(f"ERROR: Wife's birthday in family {family['ID']} is after marriage date {marriage_date}")
