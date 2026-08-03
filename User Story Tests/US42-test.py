# This file contains unit tests for the user story: US42 - Reject illegitimate dates
# SSW-555-WS
# William Bryce - Group D

import unittest
from US42_reject_illegitimate_dates import validate_reject_illegitimate_dates
from io import StringIO
from contextlib import redirect_stdout

def validation(individuals_dict, families_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_reject_illegitimate_dates(individuals_dict, families_dict)
    output = buffer.getvalue()
    return output

class Test(unittest.TestCase):
    def test1(self):
        """
        All valid dates
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",         
                "Birthday": "2000-06-01",
                "Death": "2020-06-01"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2000-06-01",
                "Divorced": "2020-06-01"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test2(self):
        """
        Invalid birth and death dates
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",         
                "Birthday": "2000-0-01",
                "Death": "2020-x-01"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2000-06-01",
                "Divorced": "2020-06-01"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), 
                        "ERROR: US42: INDIVIDUAL (@I1@): Invalid date for birthday, 2000-0-01\n" \
                        "ERROR: US42: INDIVIDUAL (@I1@): Invalid date for death, 2020-x-01\n")

    def test3(self):
        """
        Invalid dates for marriage and divorce
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",         
                "Birthday": "2000-06-01",
                "Death": "2020-06-01"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2000-0-01",
                "Divorced": "2020-x-01"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), 
                        "ERROR: US42: FAMILY (@F1@): Invalid date for marriage, 2000-0-01\n" \
                        "ERROR: US42: FAMILY (@F1@): Invalid date for divorce, 2020-x-01\n")

    def test4(self):
        """
        All dates invalid
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",         
                "Birthday": "2000-0-01",
                "Death": "2020-x-01"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2000-0-01",
                "Divorced": "2020-x-01"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), 
                        "ERROR: US42: INDIVIDUAL (@I1@): Invalid date for birthday, 2000-0-01\n" \
                        "ERROR: US42: INDIVIDUAL (@I1@): Invalid date for death, 2020-x-01\n" \
                        "ERROR: US42: FAMILY (@F1@): Invalid date for marriage, 2000-0-01\n" \
                        "ERROR: US42: FAMILY (@F1@): Invalid date for divorce, 2020-x-01\n")

    def test5(self):
        """
        Two individuals with invalid birthdays, two families with invalid marriage dates
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",         
                "Birthday": "2000-0-01",
                "Death": "2020-06-01"
            },
            "@I2@": {
                "ID": "@I2@",
                "Birthday": "2000-x-01",
                "Death": "2020-06-01"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2000-0-01",
                "Divorced": "2020-06-01"
            },
            "@F2@": {
                "ID": "@F2@",
                "Married": "2000-x-01",
                "Divorced": "2020-06-01"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), 
                        "ERROR: US42: INDIVIDUAL (@I1@): Invalid date for birthday, 2000-0-01\n" \
                        "ERROR: US42: INDIVIDUAL (@I2@): Invalid date for birthday, 2000-x-01\n" \
                        "ERROR: US42: FAMILY (@F1@): Invalid date for marriage, 2000-0-01\n" \
                        "ERROR: US42: FAMILY (@F2@): Invalid date for marriage, 2000-x-01\n")

if __name__ == '__main__':
    unittest.main()