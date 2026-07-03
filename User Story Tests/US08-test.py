# This file contains unit tests for the user story: US08 - Birth after marriage
# SSW-555-WS
# Sam Bryan - Group D

# Acknowledgement: IDE autocomplete was used on certain lines of code.

import unittest
from US08_birth_after_marriage import validate_birth_after_marriage
from io import StringIO
from contextlib import redirect_stdout

# helper function to capture print statements for unit tests
# citation: https://www.google.com/search?q=how+to+capture+print+statements+for+unittesting+in+Python&rlz=1C1CHBF_enUS1023US1023&oq=how+to+capture+print+statements+for+unittesting+in+Python&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQIRgKGKABMgkIAhAhGAoYoAEyCQgDECEYChigATIJCAQQIRgKGKABMgkIBRAhGAoYoAEyCQgGECEYChirAjIHCAcQIRifBdIBCDcwODhqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8


def validation(individuals_dict, families_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_birth_after_marriage(individuals_dict, families_dict)
    output = buffer.getvalue()
    return output


class TestBirthAfterMarriage(unittest.TestCase):
    def test_birth_after_marriage_1(self):
        """
        Child born well after marriage, no divorce.
        """
        individuals_dict = {
            "@I3@": {
                "ID": "@I3@",
                "Birthday": "2001-01-01",
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2000-01-01",
                "Divorced": "NA",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": ["@I3@"]
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test_birth_after_marriage_2(self):
        """
        Child born before the marriage of their parents.
        """
        individuals_dict = {
            "@I3@": {
                "ID": "@I3@",
                "Birthday": "2003-01-01",
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2005-01-01",
                "Divorced": "NA",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": ["@I3@"]
            }
        }
        self.assertEqual(
            validation(individuals_dict, families_dict),
            "ERROR: Child @I3@ was born before the marriage of their parents in family @F1@\n"
        )

    def test_birth_after_marriage_3(self):
        """
        Child born more than 9 months after the divorce of their parents.
        """
        individuals_dict = {
            "@I3@": {
                "ID": "@I3@",
                "Birthday": "2011-06-01",
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2000-01-01",
                "Divorced": "2010-01-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": ["@I3@"]
            }
        }
        self.assertEqual(
            validation(individuals_dict, families_dict),
            "ERROR: Child @I3@ was born more than 9 months after the divorce of their parents in family @F1@\n"
        )

    def test_birth_after_marriage_4(self):
        """
        Child born within 9 months of the divorce of their parents.
        """
        individuals_dict = {
            "@I3@": {
                "ID": "@I3@",
                "Birthday": "2010-06-01",
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2000-01-01",
                "Divorced": "2010-01-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": ["@I3@"]
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test_birth_after_marriage_5(self):
        """
        Marriage date is "NA"
        """
        individuals_dict = {
            "@I3@": {
                "ID": "@I3@",
                "Birthday": "2001-01-01",
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "NA",
                "Divorced": "NA",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": ["@I3@"]
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test_birth_after_marriage_6(self):
        """
        Family has no children.
        """
        individuals_dict = {}
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2000-01-01",
                "Divorced": "NA",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": []
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

if __name__ == "__main__":
    unittest.main()
