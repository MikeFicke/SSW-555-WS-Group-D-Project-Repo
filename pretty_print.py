# Group D
# SSW-555-WS
# GEDCOM Pretty Print

# This program reads a GEDCOM file from the command line, parses individuals
# and families, and pretty-prints two summary tables: People and Families.

# package needed to interpret command line arguments
import sys

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

            # TODO: accumulate parsed data into Individual/Family structures
            # TODO: after loop, pretty-print tables

    except FileNotFoundError as fe:
        print(f"File not found: {fe}")
    except IndexError:
        print("Usage: python pretty_print.py <path_to_gedcom_file>")
        sys.exit(1)
    except Exception as er:
        print(f"FATAL ERROR: {er}")
