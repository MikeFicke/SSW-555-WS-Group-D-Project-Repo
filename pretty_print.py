# Group D
# SSW-555-WS
# GEDCOM Pretty Print

# This program reads a GEDCOM file from the command line, parses individuals
# and families, and pretty-prints two summary tables: People and Families.

# package needed to interpret command line arguments
import sys

# package needed to display the GEDCOM data in a table
from pretty_print import PrettyTable

# valid GEDCOM tags, organized by their expected level in the GEDCOM data
valid_tags = {
    0: {"INDI", "FAM", "HEAD", "TRLR", "NOTE"},
    1: {"NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS",
        "MARR", "HUSB", "WIFE", "CHIL", "DIV"},
    2: {"DATE"}
}

if __name__ == "__main__":
    # Take the GEDCOM file path as input
    try:
        gedcom_data_file = sys.argv[1]
        with open(gedcom_data_file, 'r') as file:
            file_contents = file.readlines()

        # Create dictionaries to store individual and family data
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
                individuals[current_id] = {"ID": current_id, "Name": "NA", "Gender": "NA", "Birth": "NA", "Death": "NA", "Child": "NA", "Spouse": "NA"}
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
                    current_event = "Birth"
                elif tag == "DEAT":
                    current_event = "Death"
                elif tag == "FAMC":
                    individuals[current_id]["Child"] = args
                elif tag == "FAMS":
                    individuals[current_id]["Spouse"] = args
            elif current_type == "FAM":
                if tag == "MARR":
                    current_event = "Marriage"
                elif tag == "DIV":
                    current_event = "Divorce"
                elif tag == "HUSB":
                    families[current_id]["Husband ID"] = args
                elif tag == "WIFE":
                    families[current_id]["Wife ID"] = args
                elif tag == "CHIL":
                    families[current_id]["Children"].append(args)
        elif level == 2 and tag == "DATE" and current_event is not None:
            split_args = args.strip()
            day = split_args[0]
            month = split_args[1]
            year = split_args[2]
            date_string = day + " " + month + ", " + year

            if current_event == "BIRT":
                individuals[current_id]["Birth"] = date_string
            elif current_event == "DEAT":
                individuals[current_id]["Death"] = date_string
            elif current_event == "MARR":
                families[current_id]["Married"] = date_string
            elif current_event == "DIV":
                families[current_id]["Divorced"] = date_string
            current_event = None
        
        # Print the People table
        print("People:")
        people_table = PrettyTable()
        people_table.field_names = ["ID", "Name", "Gender", "Birth", "Age", "Alive", "Death", "Child", "Spouse"]
        for row in individuals.values():
            people_table.add_row([row["ID"], row["Name"], row["Gender"], row["Birth"], row["Age"], row["Alive"], row["Death"], row["Child"], row["Spouse"]])
        
        print(people_table)
        print()

        # Print the Families table
        print("Families:")
        families_table = PrettyTable()
        families_table.field_names = ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"]
        for row in families.values():
            families_table.add_row([row["ID"], row["Married"], row["Divorced"], row["Husband ID"], row["Wife ID"], row["Children"]])
        
        print(families_table)
        print()

    except FileNotFoundError as fe:
        print(f"File not found: {fe}")
    except IndexError:
        print("Usage: python pretty_print.py <path_to_gedcom_file>")
        sys.exit(1)
    except Exception as er:
        print(f"FATAL ERROR: {er}")
