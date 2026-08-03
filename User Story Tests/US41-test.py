# This file contains unit tests for the user story: US41 - Include partial dates
# SSW-555-WS
# William Bryce - Group D

import unittest
from US41_include_partial_dates import validate_include_partial_dates
from io import StringIO
from contextlib import redirect_stdout

def validation(individuals_dict, families_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_include_partial_dates(individuals_dict, families_dict)
    output = buffer.getvalue()
    return output

class Test(unittest.TestCase):
    def test1(self):
        """
        Full valid dates
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
        self.assertEqual(validation(individuals_dict, families_dict), 
                        "US41: INDIVIDUAL (@I1@): Birthday = 2000-06-01, Death = 2020-06-01\n" \
                        "US41: FAMILY (@F1@): Married = 2000-06-01, Divorced = 2020-06-01\n")

    def test2(self):
        """
        All dates missing days
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",         
                "Birthday": "2000-06",
                "Death": "2020-06"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2000-06",
                "Divorced": "2020-06"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), 
                        "US41: INDIVIDUAL (@I1@): Birthday = 2000-06-01, Death = 2020-06-01\n" \
                        "US41: FAMILY (@F1@): Married = 2000-06-01, Divorced = 2020-06-01\n")

    def test3(self):
        """
        All missing month and day
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",         
                "Birthday": "2000",
                "Death": "2020"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2000",
                "Divorced": "2020"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), 
                        "US41: INDIVIDUAL (@I1@): Birthday = 2000-01-01, Death = 2020-01-01\n" \
                        "US41: FAMILY (@F1@): Married = 2000-01-01, Divorced = 2020-01-01\n")

if __name__ == '__main__':
    unittest.main()