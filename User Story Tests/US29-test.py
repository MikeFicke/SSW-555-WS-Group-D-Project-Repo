# This file contains unit tests for the user story: US 29 - List deceased
# SSW-555-WS
# William Bryce - Group D

import unittest
from US29_list_deceased import validate_list_deceased
from io import StringIO
from contextlib import redirect_stdout

def validation(individuals_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_list_deceased(individuals_dict)
    output = buffer.getvalue()
    return output

class Test(unittest.TestCase):
    def test1(self):
        """
        One deceased individual
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Alive": False,
                "Death": "2020-06-01"
            }
        }
        families_dict = {} 
        self.assertEqual(validation(individuals_dict), "US29: Deceased Individuals: @I1@\n")

    def test2(self):
        """
        No individuals on file
        """
        individuals_dict = {}
        families_dict = {} 
        self.assertEqual(validation(individuals_dict), "")

    def test3(self):
        """
        One deceased, one living
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Alive": False,
                "Death": "2020-06-01"
            },
            "@I2@": {
                "ID": "@I2@",
                "Alive": True,
                "Death": "NA"
            }
        }
        families_dict = {} 
        self.assertEqual(validation(individuals_dict), "US29: Deceased Individuals: @I1@\n")

    def test4(self):
        """
        Many deceased
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Alive": False,
                "Death": "2020-06-01"
            },
            "@I2@": {
                "ID": "@I2@",
                "Alive": False,
                "Death": "2021-07-25"
            },
            "@I3@": {
                "ID": "@I3@",
                "Alive": False,
                "Death": "2018-11-08"
            },
            "@I4@": {
                "ID": "@I4@",
                "Alive": False,
                "Death": "2025-02-16"
            },
            "@I5@": {
                "ID": "@I5@",
                "Alive": False,
                "Death": "2019-03-12"
            }
        }
        families_dict = {} 
        self.assertEqual(validation(individuals_dict), "US29: Deceased Individuals: @I1@, @I2@, @I3@, @I4@, @I5@\n")

    def test5(self):
        """
        Many deceased and living
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Alive": False,
                "Death": "2020-06-01"
            },
            "@I2@": {
                "ID": "@I2@",
                "Alive": False,
                "Death": "2021-07-251"
            },
            "@I3@": {
                "ID": "@I3@",
                "Alive": True,
                "Death": "2018-09-16"
            },
            "@I4@": {
                "ID": "@I4@",
                "Alive": True,
                "Death": "2012-09-18"
            },
            "@I5@": {
                "ID": "@I5@",
                "Alive": False,
                "Death": "2019-03-12"
            },
            "@I6@": {
                "ID": "@I6@",
                "Alive": True,
                "Death": "2013-04-03"
            },
            "@I7@": {
                "ID": "@I7@",
                "Alive": False,
                "Death": "2020-06-01"
            },
            "@I8@": {
                "ID": "@I8@",
                "Alive": True,
                "Death": "2018-11-08"
            },
            "@I9@": {
                "ID": "@I9@",
                "Alive": False,
                "Death": "2025-02-16"
            },
            "@I10@": {
                "ID": "@I10@",
                "Alive": True,
                "Death": "2006-01-15"
            }
        }
        families_dict = {} 
        self.assertEqual(validation(individuals_dict), "US29: Deceased Individuals: @I1@, @I2@, @I5@, @I7@, @I9@\n")

if __name__ == '__main__':
    unittest.main()