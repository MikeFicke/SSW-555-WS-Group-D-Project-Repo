# This file contains unit tests for the user story: US10 - Marriage after 14
# SSW-555-WS
# William Bryce - Group D

import unittest
from US10_marriage_after_14 import validate_marriage_after_14
from io import StringIO
from contextlib import redirect_stdout

def validation(individuals_dict, families_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_marriage_after_14(individuals_dict, families_dict)
    output = buffer.getvalue()
    return output

class TestMarriageAfter14(unittest.TestCase):
    def test1(self):
        """
        Valid marriage, 14 years after birth of both spouses
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "2000-01-01"
            },
            "@I2@": {
                "ID": "@I2@",
                "Birthday": "2000-01-01"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2020-01-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test2(self):
        """
        Husband married before age 14
        """
        individuals_dict = {
            "@I1@": {
                "Name": "John /Doe/",
                "ID": "@I1@",
                "Birthday": "2007-01-01"
            },
            "@I2@": {
                "Name": "Jane /Doe/",
                "ID": "@I2@",
                "Birthday": "2000-01-01"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2020-01-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "ERROR: FAMILY: US10: @F1@: Individual John /Doe/ was married before age 14.\n")

    def test3(self):
        """
        Wife married before age 14
        """
        individuals_dict = {
            "@I1@": {
                "Name": "John /Doe/",
                "ID": "@I1@",
                "Birthday": "2000-01-01"
            },
            "@I2@": {
                "Name": "Jane /Doe/",
                "ID": "@I2@",
                "Birthday": "2007-01-01"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2020-01-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "ERROR: FAMILY: US10: @F1@: Individual Jane /Doe/ was married before age 14.\n")

    def test4(self):
        """
        Marriage before 14 years after birth of both spouses
        """
        individuals_dict = {
            "@I1@": {
                "Name": "John /Doe/",
                "ID": "@I1@",
                "Birthday": "2007-01-01"
            },
            "@I2@": {
                "Name": "Jane /Doe/",
                "ID": "@I2@",
                "Birthday": "2007-01-01"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2020-01-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict),
                        "ERROR: FAMILY: US10: @F1@: Individual John /Doe/ was married before age 14.\n" \
                        "ERROR: FAMILY: US10: @F1@: Individual Jane /Doe/ was married before age 14.\n")

    def test5(self):
        """
        Marriage exactly 14 years after birth of both spouses
        """
        individuals_dict = {
            "@I1@": {
                "Name": "John /Doe/",
                "ID": "@I1@",
                "Birthday": "2006-01-01"
            },
            "@I2@": {
                "Name": "Jane /Doe/",
                "ID": "@I2@",
                "Birthday": "2006-01-01"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2020-01-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

if __name__ == '__main__':
    unittest.main()