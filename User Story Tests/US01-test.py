# This file contains unit tests for the user story: US01 - Dates before current date
# SSW-555-WS
# William Bryce - Group D

import unittest
from US01_dates_before_current_date import validate_dates_before_current_date
from io import StringIO
from contextlib import redirect_stdout

def validation(individuals_dict, families_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_dates_before_current_date(individuals_dict, families_dict)
    output = buffer.getvalue()
    return output

class TestDatesBeforeCurrentDate(unittest.TestCase):
    def test1(self):
        """
        Valid individual, no error
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",         
                "Birthday": "2000-06-01",
                "Death": "2020-06-01"
            }
        }
        families_dict = {} 
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test2(self):
        """
        Invalid individual birthday
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "2030-06-01",
                "Death": "2020-06-01"
            }
        }
        families_dict = {}
        self.assertEqual(validation(individuals_dict, families_dict), "ERROR: INDIVIDUAL: US01: @I1@: Birthday 2030-06-01 occurs in the future\n")

    def test3(self):
        """
        Invalid individual death date
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "2000-06-01",
                "Death": "2030-06-01"
            }
        }
        families_dict = {}
        self.assertEqual(validation(individuals_dict, families_dict), "ERROR: INDIVIDUAL: US01: @I1@: Death 2030-06-01 occurs in the future\n")

    def test4(self):
        """
        Invalid family marriage date
        """
        individuals_dict = {}
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2030-06-01",
                "Divorced": "2000-06-01"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "ERROR: FAMILY: US01: @F1@: Marriage date 2030-06-01 occurs in the future\n")

    def test5(self):
        """
        Invalid family divorce date
        """
        individuals_dict = {}
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2000-06-01",
                "Divorced": "2030-06-01"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "ERROR: FAMILY: US01: @F1@: Divorce date 2030-06-01 occurs in the future\n")

if __name__ == '__main__':
    unittest.main()