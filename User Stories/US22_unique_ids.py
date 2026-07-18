# Group D
# SSW-555-WS
# User Story: Unique IDs
# All individual IDs should be unique, and all family IDs should be unique
# Author: Michael Ficke
# Acknowledgement: IDE Auto-complete was used for certain lines of code

"""
This user story is more challenging than I was first led to believe because
the pretty_print.py file stores individuals and families in Python dictionaries with ID keys.
As a result, if a duplicate ID appears, the parser silntly overwrites the earlier entry.
Therefore, for this user story to be correctly implemented, we have to look at the raw GEDCOM lines instead of the dictionaries.
"""

def validate_unique_ids(file_contents):
    """
    Check if there are any duplicate individual or family IDs by parsing through the raw GEDCOM data.
    """
    individual_ids = []
    family_ids = []
    for line in file_contents:
        # strip whitespace out and split into tokens
        no_whitespace_line = line.strip()
        tokenized_no_whitespace_line = no_whitespace_line.split()

        # If there are fewer than 3 tokens, skip the line as it does not have all of the information we need
        # Expected format is: "<level> <id> <tag>"
        if len(tokenized_no_whitespace_line) < 3:
            continue
        
        level = tokenized_no_whitespace_line[0]
        individual_id = tokenized_no_whitespace_line[1]
        individual_tag = tokenized_no_whitespace_line[2]

        # It can be assumed that the level we are looking at for this information will always be zero.  Therefore, if it is not, skip the information
        if level != '0':
            continue

        if individual_tag == "INDI":
            individual_ids.append(individual_id)
        elif individual_tag == "FAM":
            family_ids.append(individual_id)
        else:
            # skip
            continue

    # Check for duplicate individual IDS using a set, as a set does not contain duplicates
    known_individual_ids = set()
    
    for id in individual_ids:
        if id in known_individual_ids:
            print(f"ERROR: Individual ID {id} appears more than once in the GEDCOM file.")
        else:
            known_individual_ids.add(id)
    
    # Similar logic for family IDs
    known_family_ids = set()

    for id in family_ids:
        if id in known_family_ids:
            print(f"ERROR: Family ID {id} appears more than once in the GEDCOM file.")
        else:
            known_family_ids.add(id)
