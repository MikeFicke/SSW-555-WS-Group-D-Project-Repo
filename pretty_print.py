# Group D
# SSW-555-WS
# GEDCOM Pretty Print

# This module parses a GEDCOM file and pretty-prints two summary tables:
# People and Families.

# Acknowledgement: IDE auto-complete was used for certain code lines in this file

from prettytable import PrettyTable
import datetime

# citation: https://github.com/MikeFicke/SSW-555-WS-M2.B3

# valid GEDCOM tags, organized by their expected level in the GEDCOM data
valid_tags = {
    0: {"INDI", "FAM", "HEAD", "TRLR", "NOTE"},
    1: {"NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS",
        "MARR", "HUSB", "WIFE", "CHIL", "DIV"},
    2: {"DATE"}
}


def parse_gedcom(file_contents):
    """Parse GEDCOM file lines and return individuals and families dictionaries."""
    individuals = {}
    families = {}
    current_id = None
    current_type = None
    current_event = None

    for line in file_contents:
        # Split into words, strip whitespace, skip blank lines
        stripped_line = line.strip()
        line_tokens = stripped_line.split()

        if not line_tokens:
            continue

        try:
            # Get the level number
            level = int(line_tokens[0])
        except ValueError:
            continue

        tag = ""
        args = ""

        data_length = len(line_tokens)
        if data_length >= 3 and line_tokens[2] in ("INDI", "FAM"):
            # Special case: "0 @I1@ INDI" — ID comes before the tag.  Location of tag changes based on the length.
            tag = line_tokens[2]
            args = line_tokens[1]
        elif data_length >= 2:
            tag = line_tokens[1]
            if data_length > 2:
                args = ' '.join(line_tokens[2:])
        else:
            continue

        if level == 0:
            current_event = None
            # Identify if we are parsing an individual or a family, otherwise we skip.
            if tag == "INDI":
                current_id = args
                current_type = "INDI"
                individuals[current_id] = {"ID": current_id, "Name": "NA", "Gender": "NA", "Birthday": "NA", "Death": "NA", "Child": "NA", "Spouse": []}
            elif tag == "FAM":
                current_id = args
                current_type = "FAM"
                families[current_id] = {"ID": current_id, "Married": "NA", "Divorced": "NA", "Husband ID": "NA", "Wife ID": "NA", "Children": []}
            else:
                current_id = None
                current_type = None
        elif level == 1 and current_id is not None:
            # Identify the tag at level 1.
            # Check if we are parsing an individual or a family.
            if current_type == "INDI":
                # Check the tag for individuals
                if tag == "NAME":
                    individuals[current_id]["Name"] = args
                elif tag == "SEX":
                    individuals[current_id]["Gender"] = args
                elif tag == "BIRT":
                    current_event = "BIRT"
                elif tag == "DEAT":
                    current_event = "DEAT"
                elif tag == "FAMC":
                    individuals[current_id]["Child"] = args
                elif tag == "FAMS":
                    individuals[current_id]["Spouse"].append(args)
            elif current_type == "FAM":
                # Check the tag for families
                if tag == "MARR":
                    current_event = "MARR"
                elif tag == "DIV":
                    current_event = "DIV"
                elif tag == "HUSB":
                    families[current_id]["Husband ID"] = args
                elif tag == "WIFE":
                    families[current_id]["Wife ID"] = args
                elif tag == "CHIL":
                    families[current_id]["Children"].append(args)
        elif level == 2 and tag == "DATE" and current_event is not None:
            # Split the date into day, month, year and format it
            # citation: https://www.google.com/search?q=python+sprtime+and+strftime&rlz=1C1CHBF_enUS1023US1023&oq=python+sprtime+and+strftime&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQABgNGIAEMgoIAhAAGAgYDRgeMgoIAxAAGAgYDRgeMgoIBBAAGAgYDRgeMgoIBRAAGAgYDRgeMgoIBhAAGAgYDRgeMg0IBxAAGIYDGIAEGIoFMgcICBAAGO8FMgcICRAAGO8F0gEIMzY5NGowajeoAgCwAgA&sourceid=chrome&ie=UTF-8
            date_string = datetime.datetime.strftime(datetime.datetime.strptime(args, "%d %b %Y"), "%Y-%m-%d")
            
            # Check if the current event is a birth, death, marriage, or divorce and set the date
            if current_event == "BIRT":
                individuals[current_id]["Birthday"] = date_string
            elif current_event == "DEAT":
                individuals[current_id]["Death"] = date_string
            elif current_event == "MARR":
                families[current_id]["Married"] = date_string
            elif current_event == "DIV":
                families[current_id]["Divorced"] = date_string
            current_event = None

    # Compute Alive and Age for each individual
    for indi in individuals.values():
        indi["Alive"] = indi["Death"] == "NA"  # "Is this person's Death field still 'NA' ? "  Boolean check
        # Calculate the age
        if indi["Birthday"] == "NA":
            indi["Age"] = "NA"
        else:
            birth_year = int(indi["Birthday"].split("-")[0])  #  YYYY-MM-DD
            if indi["Death"] != "NA":  # Person is dead
                death_year = int(indi["Death"].split("-")[0])  #  YYYY-MM-DD
            else:
                death_year = datetime.date.today().year  # Use the current year because the person is living
            indi["Age"] = death_year - birth_year  # Calculate the age

    return individuals, families

# citation: https://www.google.com/search?q=how+to+use+pretty+print+to+make+tables+in+Python&rlz=1C1CHBF_enUS1023US1023&oq=how+to+use+prett&gs_lcrp=EgZjaHJvbWUqCAgAEEUYJxg7MggIABBFGCcYOzIGCAEQRRg5MgcIAhAAGIAEMgcIAxAAGIAEMgcIBBAAGIAEMgcIBRAAGIAEMgcIBhAAGIAEMgcIBxAAGIAEMgcICBAAGIAEMgcICRAAGIAE0gEIMzEzNmowajmoAgCwAgA&sourceid=chrome&ie=UTF-8
def print_people(individuals):
    """Print the People table based on the formatting requirements."""
    print("Individuals")
    people_table = PrettyTable()
    people_table.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
    for row in sorted(individuals.values(), key=lambda x: int(x["ID"][2:-1])):  # extract the number in the ID
        spouse = set(row["Spouse"]) if row["Spouse"] else "NA"
        people_table.add_row([row["ID"], row["Name"], row["Gender"], row["Birthday"], row["Age"], row["Alive"], row["Death"], row["Child"], spouse])
    print(people_table)
    print()


# citation: https://www.google.com/search?q=how+to+use+pretty+print+to+make+tables+in+Python&rlz=1C1CHBF_enUS1023US1023&oq=how+to+use+prett&gs_lcrp=EgZjaHJvbWUqCAgAEEUYJxg7MggIABBFGCcYOzIGCAEQRRg5MgcIAhAAGIAEMgcIAxAAGIAEMgcIBBAAGIAEMgcIBRAAGIAEMgcIBhAAGIAEMgcIBxAAGIAEMgcICBAAGIAEMgcICRAAGIAE0gEIMzEzNmowajmoAgCwAgA&sourceid=chrome&ie=UTF-8
def print_families(families, individuals):
    """Print the Families table based on the formatting requirements."""
    print("Families")
    families_table = PrettyTable()
    families_table.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
    for row in sorted(families.values(), key=lambda x: int(x["ID"][2:-1])):  # sort families by numeric ID
        if row["Husband ID"] in individuals:
            husb_name = individuals[row["Husband ID"]]["Name"] 
        else:
            husb_name = "NA"
        if row["Wife ID"] in individuals:
            wife_name = individuals[row["Wife ID"]]["Name"] 
        else:
            wife_name = "NA"
        families_table.add_row([row["ID"], row["Married"], row["Divorced"], row["Husband ID"], husb_name, row["Wife ID"], wife_name, row["Children"]])
    print(families_table)
    print()
