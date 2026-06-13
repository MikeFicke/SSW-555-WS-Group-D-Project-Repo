# Group D
# SSW-555-WS

# This reads a GEDCOM file from the command line, parses it,
# pretty-prints the data, and runs unit tests.

# citation: https://github.com/MikeFicke/SSW-555-WS-M2.B3

import sys
from pretty_print import parse_gedcom, print_people, print_families

if __name__ == "__main__":
    try:
        gedcom_data_file = sys.argv[1]
        with open(gedcom_data_file, 'r') as file:
            file_contents = file.readlines()

        # Step 1: Parse the GEDCOM file
        individuals, families = parse_gedcom(file_contents)

        # Step 2: Pretty-print the tables
        print_people(individuals)
        print_families(families, individuals)

        # Step 3: Run unit tests / validations
        # TODO

        # Save terminal output as a text file
        # citation: https://www.google.com/search?q=how+to+output+terminal+outputs+to+a+text+file+in+Python&sca_esv=7f84a317695edff8&rlz=1C1CHBF_enUS1023US1023&sxsrf=ANbL-n7W5Mn-MFzFwoi1yTcPZDPfeGxnUg%3A1781305106935&ei=Eo8saofcOM7-ptQP3-DV-Qk&biw=1536&bih=825&ved=0ahUKEwiHrYrR5oKVAxVOv4kEHV9wNZ8Q4dUDCBA&uact=5&oq=how+to+output+terminal+outputs+to+a+text+file+in+Python&gs_lp=Egxnd3Mtd2l6LXNlcnAiN2hvdyB0byBvdXRwdXQgdGVybWluYWwgb3V0cHV0cyB0byBhIHRleHQgZmlsZSBpbiBQeXRob24yChAhGAoYoAEYwwRImQ1Q-QZYsAtwAngBkAEAmAGJAaABpgaqAQM1LjO4AQPIAQD4AQGYAgWgAskCwgIKEAAYRxjWBBiwA5gDAIgGAZAGCJIHAzMuMqAHtSiyBwMxLjK4B7MCwgcHMC4xLjMuMcgHGYAIAQ&sclient=gws-wiz-serp
        with open("output.txt", "w") as file:
            output = sys.stdout  # Save terminal contents for restoration after
            sys.stdout = file  # Terminal outputs routed to file instead
            print_people(individuals)
            print_families(families, individuals)
            sys.stdout = output  # Restore to terminal

    except FileNotFoundError as fe:
        print(f"File not found: {fe}")
    except IndexError:
        print("Usage: python main.py <path_to_gedcom_file>")
        sys.exit(1)
    except Exception as er:
        print(f"FATAL ERROR: {er}")
