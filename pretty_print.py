# Group D
# SSW-555-WS
# GEDCOM Pretty Print

# This module parses a GEDCOM file and pretty-prints two summary tables:
# People and Families.

from prettytable import PrettyTable

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
    current_type = None  # Either INDI or FAM
    current_event = None  # Either BIRT, DEAT, MARR, DIV

    for line in file_contents:
        stripped_line = line.strip()
        line_tokens = stripped_line.split()

        if not line_tokens:
            continue

        try:
            level = int(line_tokens[0])
        except ValueError:
            continue

        tag = ""
        args = ""

        data_length = len(line_tokens)
        if data_length >= 3 and line_tokens[2] in ("INDI", "FAM"):
            # Special case: "0 @I1@ INDI" — ID comes before the tag
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
            if current_type == "INDI":
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
            split_args = args.strip().split()
            day = split_args[0]
            month = split_args[1]
            year = split_args[2]
            date_string = day + " " + month + ", " + year

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
        indi["Alive"] = indi["Death"] == "NA"
        indi["Age"] = "NA"

    return individuals, families


def print_people(individuals):
    """Print the People table."""
    print("People")
    people_table = PrettyTable()
    people_table.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
    for row in individuals.values():
        people_table.add_row([row["ID"], row["Name"], row["Gender"], row["Birthday"], row["Age"], row["Alive"], row["Death"], row["Child"], row["Spouse"]])
    print(people_table)
    print()


def print_families(families, individuals):
    """Print the Families table."""
    print("Families")
    families_table = PrettyTable()
    families_table.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
    for row in families.values():
        husb_name = individuals[row["Husband ID"]]["Name"] if row["Husband ID"] in individuals else "NA"
        wife_name = individuals[row["Wife ID"]]["Name"] if row["Wife ID"] in individuals else "NA"
        families_table.add_row([row["ID"], row["Married"], row["Divorced"], row["Husband ID"], husb_name, row["Wife ID"], wife_name, row["Children"]])
    print(families_table)
    print()
