# Group D - Michael Ficke
# SSW-555-WS
# Unit test file for US16

# Acknowledgement: IDE auto-complete was used for certain lines of code

import unittest
from US16_male_last_names import validate_male_last_names
from io import StringIO
from contextlib import redirect_stdout



def validation(individuals_dict, family_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_male_last_names(individuals_dict, family_dict)
    output = buffer.getvalue()
    return output


class TestMaleLastNames(unittest.TestCase):
    def test_male_last_names_1(self):
        """
        Valid family, all males share the father's last name
        """
        individuals = {
            '@I1@': {'Name': 'John /Smith/', 'Gender': 'M'},
            '@I2@': {'Name': 'Jane /Doe/', 'Gender': 'F'},
            '@I3@': {'Name': 'Michael /Smith/', 'Gender': 'M'},
            '@I4@': {'Name': 'David /Smith/', 'Gender': 'M'},
        }
        families = {
            '@F1@': {'Husband ID': '@I1@', 'Wife ID': '@I2@', 'Children': ['@I3@', '@I4@']},
        }

        self.assertEqual(validation(individuals, families), "")


    def test_male_last_names_2(self):
        """
        Invalid family, one male child has a different last name
        """
        individuals = {
            '@I1@': {'Name': 'John /Smith/', 'Gender': 'M'},
            '@I2@': {'Name': 'Jane /Doe/', 'Gender': 'F'},
            '@I3@': {'Name': 'Michael /Smith/', 'Gender': 'M'},
            '@I4@': {'Name': 'David /Doe/', 'Gender': 'M'},
        }
        families = {
            '@F1@': {'Husband ID': '@I1@', 'Wife ID': '@I2@', 'Children': ['@I3@', '@I4@']},
        }

        self.assertEqual(validation(individuals, families), "ERROR: US16: David /Doe/'s last name 'Doe' does not match the husband's last name 'Smith'\n")
        
        

    def test_male_last_names_3(self):
        """
        Family with only female children
        """
        individuals = {
            '@I1@': {'Name': 'John /Smith/', 'Gender': 'M'},
            '@I2@': {'Name': 'Jane /Doe/', 'Gender': 'F'},
            '@I3@': {'Name': 'Sarah /Smith/', 'Gender': 'F'},
            '@I4@': {'Name': 'Emily /Smith/', 'Gender': 'F'},
        }
        families = {
            '@F1@': {'Husband ID': '@I1@', 'Wife ID': '@I2@', 'Children': ['@I3@', '@I4@']},
        }

        self.assertEqual(validation(individuals, families), "")
        
        

    def test_male_last_names_4(self):
        """
        Family with no children
        """
        individuals = {
            '@I1@': {'Name': 'John /Smith/', 'Gender': 'M'},
            '@I2@': {'Name': 'Jane /Doe/', 'Gender': 'F'},
        }
        families = {
            '@F1@': {'Husband ID': '@I1@', 'Wife ID': '@I2@', 'Children': []},
        }

        self.assertEqual(validation(individuals, families), "")
        
        

    def test_male_last_names_5(self):
        """
        Mixed family, some male children match, one does not
        """
        individuals = {
            '@I1@': {'Name': 'John /Smith/', 'Gender': 'M'},
            '@I2@': {'Name': 'Jane /Doe/', 'Gender': 'F'},
            '@I3@': {'Name': 'Michael /Smith/', 'Gender': 'M'},
            '@I4@': {'Name': 'David /Doe/', 'Gender': 'M'},
            '@I5@': {'Name': 'Sarah /Smith/', 'Gender': 'F'},
            '@I6@': {'Name': 'Emily /Doe/', 'Gender': 'F'},
        }
        families = {
            '@F1@': {'Husband ID': '@I1@', 'Wife ID': '@I2@', 'Children': ['@I3@', '@I4@', '@I5@', '@I6@']},
        }

        self.assertEqual(validation(individuals, families), "ERROR: US16: David /Doe/'s last name 'Doe' does not match the husband's last name 'Smith'\n")        


if __name__ == "__main__":
    unittest.main()
