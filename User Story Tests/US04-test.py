# This file is for the M4.B1: Assignment: Homework Assignment 4: Test First submission.
# SSW-555-WS
# Sam Bryan - Group D

# This code file will perform unit tests on the user story for sprint 1 involving "marriage before divorce".
# citation: https://www.geeksforgeeks.org/python/unit-testing-python-unittest/

# Acknowledgement: IDE autocomplete was used on certain lines of code.

import unittest
from  US04 import validate_marriage_before_divorce
from io import StringIO
from contextlib import redirect_stdout

# helper function to capture print statements for unit tests
# citation: https://www.google.com/search?q=how+to+capture+print+statements+for+unittesting+in+Python&rlz=1C1CHBF_enUS1023US1023&oq=how+to+capture+print+statements+for+unittesting+in+Python&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQIRgKGKABMgkIAhAhGAoYoAEyCQgDECEYChigATIJCAQQIRgKGKABMgkIBRAhGAoYoAEyCQgGECEYChirAjIHCAcQIRifBdIBCDcwODhqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8


def validation(family_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_marriage_before_divorce(family_dict)
    output = buffer.getvalue()
    return output


class TestMarriageBeforeDivorce(unittest.TestCase):
    def test_marriage_before_divorce_1(self):
        """
        Valid family with marriage before divorce.
        """
        family_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2000-01-01",
                "Divorced": "2010-01-01",
            }
        }
        self.assertEqual(validation(family_dict), "")

    def test_marriage_before_divorce_2(self):
        """
        Invalid family with divorce before marriage.
        """
        family_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2010-01-01",
                "Divorced": "2000-01-01",
            }
        }
        self.assertEqual(validation(family_dict), "ERROR: Divorce date 2000-01-01 is before marriage date 2010-01-01 for family @F1@\n")

    def test_marriage_before_divorce_3(self):
        """
        Invalid family with marriage and divorce dates not provided.
        """
        family_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "NA",
                "Divorced": "NA",
            }
        }
        self.assertEqual(validation(family_dict), "")
    
    def test_marriage_before_divorce_4(self):
        """
        Valid family with marriage before divorce.
        """
        family_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2000-01-01",
                "Divorced": "2010-01-01",
            }
        }
        self.assertEqual(validation(family_dict), "")

    def test_marriage_before_divorce_5(self):
        """
        Mixture of families where several are valid and one is invalid.
        """
        family_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2000-01-01",
                "Divorced": "2010-01-01",
            },
            "@F2@": {
                "ID": "@F2@",
                "Married": "2010-01-01",
                "Divorced": "2000-01-01",
            }
        }
        self.assertEqual(validation(family_dict), "ERROR: Divorce date 2000-01-01 is before marriage date 2010-01-01 for family @F2@\n")    

if __name__ == "__main__":
    unittest.main()
