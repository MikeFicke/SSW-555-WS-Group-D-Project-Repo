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


class TestMultipleBirths(unittest.TestCase):
    def test_multiple_births_1(self):
        """
        Valid family, all males share the father's last name
        """
        individuals = {
            '@I1@': {'NAME': 'John /Smith/', 'SEX': 'M'},
            '@I2@': {'NAME': 'Jane /Doe/', 'SEX': 'F'},
            '@I3@': {'NAME': 'Michael /Smith/', 'SEX': 'M'},
            '@I4@': {'NAME': 'David /Smith/', 'SEX': 'M'},
        }
        families = {
            '@F1@': {'HUSB': '@I1@', 'WIFE': '@I2@', 'CHILDREN': ['@I3@', '@I4@']},
        }

        self.assertEqual(validation(individuals, families), "")


    def test_multiple_births_2(self):
        """
        Invalid family, one male child has a different last name
        """
        individuals = {
            '@I1@': {'NAME': 'John /Smith/', 'SEX': 'M'},
            '@I2@': {'NAME': 'Jane /Doe/', 'SEX': 'F'},
            '@I3@': {'NAME': 'Michael /Smith/', 'SEX': 'M'},
            '@I4@': {'NAME': 'David /Doe/', 'SEX': 'M'},
        }
        families = {
            '@F1@': {'HUSB': '@I1@', 'WIFE': '@I2@', 'CHILDREN': ['@I3@', '@I4@']},
        }

        self.assertEqual(validation(individuals, families), "ERROR: US16: David /Doe/'s last name 'Doe' does not match the husband's last name 'Smith'")
        
        

    def test_multiple_births_3(self):
        """
        Family with only female children
        """
        individuals = {
            '@I1@': {'NAME': 'John /Smith/', 'SEX': 'M'},
            '@I2@': {'NAME': 'Jane /Doe/', 'SEX': 'F'},
            '@I3@': {'NAME': 'Sarah /Smith/', 'SEX': 'F'},
            '@I4@': {'NAME': 'Emily /Smith/', 'SEX': 'F'},
        }
        families = {
            '@F1@': {'HUSB': '@I1@', 'WIFE': '@I2@', 'CHILDREN': ['@I3@', '@I4@']},
        }

        self.assertEqual(validation(individuals, families), "")
        
        

    def test_multiple_births_4(self):
        """
        Family with no children
        """
        individuals = {
            '@I1@': {'NAME': 'John /Smith/', 'SEX': 'M'},
            '@I2@': {'NAME': 'Jane /Doe/', 'SEX': 'F'},
        }
        families = {
            '@F1@': {'HUSB': '@I1@', 'WIFE': '@I2@', 'CHILDREN': []},
        }

        self.assertEqual(validation(individuals, families), "")
        
        

    def test_multiple_births_5(self):
        """
        Mixed family, some male children match, one does not
        """
        individuals = {
            '@I1@': {'NAME': 'John /Smith/', 'SEX': 'M'},
            '@I2@': {'NAME': 'Jane /Doe/', 'SEX': 'F'},
            '@I3@': {'NAME': 'Michael /Smith/', 'SEX': 'M'},
            '@I4@': {'NAME': 'David /Doe/', 'SEX': 'M'},
            '@I5@': {'NAME': 'Sarah /Smith/', 'SEX': 'F'},
            '@I6@': {'NAME': 'Emily /Doe/', 'SEX': 'F'},
        }
        families = {
            '@F1@': {'HUSB': '@I1@', 'WIFE': '@I2@', 'CHILDREN': ['@I3@', '@I4@', '@I5@', '@I6@']},
        }

        self.assertEqual(validation(individuals, families), "ERROR: US16: David /Doe/'s last name 'Doe' does not match the husband's last name 'Smith'")        


if __name__ == "__main__":
    unittest.main()
