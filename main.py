# Group D
# SSW-555-WS

# This reads a GEDCOM file from the command line, parses it,
# pretty-prints the data, and runs unit tests.

# citation: https://github.com/MikeFicke/SSW-555-WS-M2.B3

import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "User Stories"))

from pretty_print import parse_gedcom, print_people, print_families
from US01_dates_before_current_date import validate_dates_before_current_date
from US02_birth_before_marriage import validate_birth_before_marriage
from US03_birth_before_death import validate_birth_before_death
from US04_marriage_before_divorce import validate_marriage_before_divorce
from US05_marriage_before_death import validate_marriage_before_death
from US06_divorce_before_death import validate_divorce_before_death
from US07_less_than_150_years_old import validate_age_less_than_150
from US08_birth_after_marriage import validate_birth_after_marriage
from US09_birth_before_parent_death import validate_birth_before_parent_death
from US10_marriage_after_14 import validate_marriage_after_14
from US11_no_bigamy import validate_no_bigamy
from US12_parents_not_too_old import validate_parents_not_too_old
from US13_siblings_spacing import validate_siblings_spacing
from US14_multiple_births import validate_multiple_births
from US15_fewer_than_15_siblings import validate_fewer_than_15_siblings
from US16_male_last_names import validate_male_last_names
from US17_no_marriages_to_descendants import validate_no_marriages_to_descendants
from US18_no_marriage_between_siblings import validate_no_marriage_between_siblings
from US19_no_marriage_between_first_cousins import validate_no_marriage_between_first_cousins
from US21_correct_gender_role import validate_correct_gender_role
from US22_unique_ids import validate_unique_ids
from US23_unique_name_and_birth_date import validate_unique_name_and_birth_date
from US24_unique_families_by_spouses import validate_unique_families_by_spouses
from US29_list_deceased import validate_list_deceased
from US30_list_living_married import validate_list_living_married
from US25_unique_first_names_and_dates_in_family import validate_unique_first_names_and_dates_in_family
from US26_corresponding_entries import validate_corresponding_entries

if __name__ == "__main__":
    try:
        gedcom_data_file = sys.argv[1]
        with open(gedcom_data_file, 'r') as file:
            file_contents = file.readlines()

        # US22 needs to be run here before the data is parsed to ensure that it works correctly with the raw data, not the dictionaries.
        validate_unique_ids(file_contents)

        # Step 1: Parse the GEDCOM file
        individuals, families = parse_gedcom(file_contents)

        # Step 2: Pretty-print the tables
        print_people(individuals)
        print_families(families, individuals)

        # Step 3: Run unit tests / validations
        # Call function to check if there are any individuals who have birth dates that are after or the same as their death date (if applicable)
        validate_birth_before_death(individuals)
        validate_birth_before_marriage(individuals, families)
        validate_dates_before_current_date(individuals, families)
        validate_marriage_before_divorce(families)
        validate_marriage_before_death(individuals, families)
        validate_divorce_before_death(individuals, families)
        validate_marriage_after_14(individuals, families)
        validate_age_less_than_150(individuals)
        validate_no_bigamy(individuals, families)
        validate_birth_before_parent_death(individuals, families)
        validate_birth_after_marriage(individuals, families)
        validate_parents_not_too_old(individuals, families)
        validate_siblings_spacing(individuals, families)
        validate_multiple_births(individuals, families)
        validate_fewer_than_15_siblings(families)
        validate_male_last_names(individuals, families)
        validate_no_marriages_to_descendants(families)
        validate_no_marriage_between_siblings(families)
        validate_no_marriage_between_first_cousins(families)
        validate_correct_gender_role(individuals, families)
        validate_unique_ids(file_contents)
        validate_unique_name_and_birth_date(individuals)
        validate_unique_families_by_spouses(individuals, families)
        validate_list_deceased(individuals)
        validate_list_living_married(individuals)
        validate_unique_first_names_and_dates_in_family(individuals, families)
        validate_corresponding_entries(individuals, families)

        # Save terminal output as a text file
        # citation: https://www.google.com/search?q=how+to+output+terminal+outputs+to+a+text+file+in+Python&sca_esv=7f84a317695edff8&rlz=1C1CHBF_enUS1023US1023&sxsrf=ANbL-n7W5Mn-MFzFwoi1yTcPZDPfeGxnUg%3A1781305106935&ei=Eo8saofcOM7-ptQP3-DV-Qk&biw=1536&bih=825&ved=0ahUKEwiHrYrR5oKVAxVOv4kEHV9wNZ8Q4dUDCBA&uact=5&oq=how+to+output+terminal+outputs+to+a+text+file+in+Python&gs_lp=Egxnd3Mtd2l6LXNlcnAiN2hvdyB0byBvdXRwdXQgdGVybWluYWwgb3V0cHV0cyB0byBhIHRleHQgZmlsZSBpbiBQeXRob24yChAhGAoYoAEYwwRImQ1Q-QZYsAtwAngBkAEAmAGJAaABpgaqAQM1LjO4AQPIAQD4AQGYAgWgAskCwgIKEAAYRxjWBBiwA5gDAIgGAZAGCJIHAzMuMqAHtSiyBwMxLjK4B7MCwgcHMC4xLjMuMcgHGYAIAQ&sclient=gws-wiz-serp
        with open("output.txt", "w") as file:
            output = sys.stdout  # Save terminal contents for restoration after
            sys.stdout = file  # Terminal outputs routed to file instead
            print_people(individuals)
            print_families(families, individuals)
            validate_birth_before_death(individuals)
            validate_birth_before_marriage(individuals, families)
            validate_dates_before_current_date(individuals, families)
            validate_marriage_before_divorce(families)
            validate_marriage_before_death(individuals, families)
            validate_divorce_before_death(individuals, families)
            validate_marriage_after_14(individuals, families)
            validate_age_less_than_150(individuals)
            validate_no_bigamy(individuals, families)
            validate_birth_before_parent_death(individuals, families)
            validate_birth_after_marriage(individuals, families)
            validate_parents_not_too_old(individuals, families)
            validate_siblings_spacing(individuals, families)
            validate_multiple_births(individuals, families)
            validate_fewer_than_15_siblings(families)
            validate_male_last_names(individuals, families)
            validate_no_marriages_to_descendants(families)
            validate_no_marriage_between_siblings(families)
            validate_no_marriage_between_first_cousins(families)
            validate_correct_gender_role(individuals, families)
            validate_unique_ids(file_contents)
            validate_unique_name_and_birth_date(individuals)
            validate_unique_families_by_spouses(individuals, families)
            validate_list_deceased(individuals)
            validate_list_living_married(individuals)
            validate_unique_first_names_and_dates_in_family(individuals, families)
            validate_corresponding_entries(individuals, families)
            sys.stdout = output  # Restore to terminal

    except FileNotFoundError as fe:
        print(f"File not found: {fe}")
    except IndexError:
        print("Usage: python main.py <path_to_gedcom_file>")
        sys.exit(1)
    except Exception as er:
        print(f"FATAL ERROR: {er}")
