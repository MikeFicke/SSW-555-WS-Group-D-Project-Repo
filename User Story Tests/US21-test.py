# Group D - Michael Ficke
# SSW-555-WS
# Unit test file for US21

# Acknowledgement: IDE auto-complete was used for certain lines of code

import unittest
from US21_correct_gender_role import validate_correct_gender_role
from io import StringIO
from contextlib import redirect_stdout



def validation(individuals_dict, family_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_correct_gender_role(individuals_dict, family_dict)
    output = buffer.getvalue()
    return output


class TestCorrectGenderRole(unittest.TestCase):
    def test_correct_gender_role_1(self):
        """
        Valid family.  Husband is male and wife is female.
        """
        individuals = {'@I1@': {'Name': 'John /Doe/', 'Gender': 'M'}, 
        '@I2@': {'Name': 'Jane /Smith/', 'Gender': 'F'}}

        families = {'@F1@': {'Husband ID': '@I1@', 'Wife ID': '@I2@'}}

        self.assertEqual(validation(individuals, families), "")

    def test_correct_gender_role_2(self):
        """
        Invalid family.  Husband is female.
        """
        individuals = {'@I1@': {'Name': 'John /Doe/', 'Gender': 'F'}, 
        '@I2@': {'Name': 'Jane /Smith/', 'Gender': 'F'}}

        families = {'@F1@': {'Husband ID': '@I1@', 'Wife ID': '@I2@'}}

        self.assertEqual(validation(individuals, families), "Error: Husband in family @F1@ is not male.\n")

    def test_correct_gender_role_3(self):
        """
        Invalid family.  Wife is male.
        """
        individuals = {'@I1@': {'Name': 'John /Doe/', 'Gender': 'M'}, 
        '@I2@': {'Name': 'Jane /Smith/', 'Gender': 'M'}}

        families = {'@F1@': {'Husband ID': '@I1@', 'Wife ID': '@I2@'}}

        self.assertEqual(validation(individuals, families), "Error: Wife in family @F1@ is not female.\n")

    def test_correct_gender_role_4(self):
        """
        Invalid family.  Husband is female, and wife is male.
        """
        individuals = {'@I1@': {'Name': 'John /Doe/', 'Gender': 'F'}, 
        '@I2@': {'Name': 'Jane /Smith/', 'Gender': 'M'}}

        families = {'@F1@': {'Husband ID': '@I1@', 'Wife ID': '@I2@'}}

        self.assertEqual(validation(individuals, families), "Error: Husband in family @F1@ is not male.\nError: Wife in family @F1@ is not female.\n")

    def test_correct_gender_role_5(self):
        """
        Family with missing Husband ID.  Verifies that bypass logic is working.
        """
        individuals = {'@I1@': {'Name': 'John /Doe/', 'Gender': 'M'}, 
        '@I2@': {'Name': 'Jane /Smith/', 'Gender': 'F'}} 

        families = {'@F1@': {'Husband ID': 'NA', 'Wife ID': '@I2@'}}

        self.assertEqual(validation(individuals, families), "")

if __name__ == "__main__":
    unittest.main()
