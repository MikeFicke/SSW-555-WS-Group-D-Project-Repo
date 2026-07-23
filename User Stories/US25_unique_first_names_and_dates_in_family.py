# Group D
# SSW-555-WS
# User Story: Unique names and dates in each family
# Author: Michael Ficke
# Acknowledgement: IDE Auto-complete was used for certain lines of code

"""
No two children can have the same first name and be born on the same date.
"""

def validate_unique_first_names_and_dates_in_family(individuals, families):
    """
    Function that parses through the individuals and families dictionaries
    and uses a tracker to group children by their birthdays and names, performs a comparison, and 
    prints an error if there are duplicates found.
    """
    for family in families.values():
        # dictionary for children that we parsed with a KV-pair of (name, birthday) to ID
        children = {}
        # iterate through each child in the family
        for child_id in family["Children"]:
            # Look up the name and birthday of the child
            name = individuals[child_id]["Name"]
            birthday = individuals[child_id]["Birthday"]
            
            # Collect duplicates
            if (name, birthday) in children:
                children[(name, birthday)].append(child_id)
            else:
                children[(name, birthday)] = [child_id]

        # Identify duplicates and print errors accordingly
        # citation: https://www.google.com/search?q=python+how+to+do+a+for+loop+with+multiple+items+being+used+for+parsing+at+once&sca_esv=44c2076a61138388&rlz=1C1CHBF_enUS1023US1023&sxsrf=APpeQnsddd4P7yOP9J2YiB_mq7Lgl6CGqg%3A1784847797120&udm=50&source=chrome.ob&fbs=ABfTbFVyMZGZf1hfvX9uKjN_-G8cqu7ocb7U6ah0xpkIrGMK4LpKPoHZrc4HVz9uOAATjT1WBZlsmp16AtPwl2JD0qSy_O2ju2c2Jptc1EOmM28-b8Udopzf8P0kdJB8M3p5q8VaE92atPNve65kUMs09qPPMU2U2gRzjqjTnvFarAUKw0YkCg6gdPcF0vto5ATgbtMONVEh6KWHutcyfkEfDasvAQcvCQ&aep=1&ntc=1&cs=1&sa=X&ved=2ahUKEwjRn7OX9OmVAxWHGlkFHXO3FpQQ2J8OegQIERAD&biw=1536&bih=825.2000122070312&dpr=2.5&sourceid=chrome&ccb=1&hl=en-US&mstk=AUtExfA-JDJqlpJ6fmFq5tmDV5GSeptSm3fJNIeUhCarw1LtWPwqnCeFOcdXqR1t9rJxnxHuXrsKha2iMkBXgrmWiGKee85lk-XXBoEsn99SL_W6lqcmff8VKyZzG_k-NG08i8TXYh2EOLIlb7bXHU2QPACXtIu_wW-n0uw&csuir=1&mtid=E55iavXGJJ6f5NoPqonRgQM
        for (name, birthday), ids in children.items():
            if len(ids) >= 2:  # Duplicates found
                id_list = ', '.join(ids)  # Format the list of duplicate IDs for the error message
                print(f"ERROR: US25: FAMILY ({family['ID']}): Children ({id_list}) share the same name ({name}) and birth date ({birthday}).")
