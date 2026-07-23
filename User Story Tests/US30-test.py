# This file contains unit tests for the user story: US 30 - List living married
# SSW-555-WS
# William Bryce - Group D

import unittest
from US30_list_living_married import validate_list_living_married
from io import StringIO
from contextlib import redirect_stdout

def validation(individuals_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_list_living_married(individuals_dict)
    output = buffer.getvalue()
    return output

class Test(unittest.TestCase):
    def test1(self):
        """
        One living/married individual
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Alive": True,
                "Death": "NA",
                "Spouse": ["@I2@"]
            }
        }
        families_dict = {} 
        self.assertEqual(validation(individuals_dict), "US30: Living married individuals: @I1@\n")

    def test2(self):
        """
        No individuals on file
        """
        individuals_dict = {}
        families_dict = {} 
        self.assertEqual(validation(individuals_dict), "")

    def test3(self):
        """
        One living/married, one living/not married, two deceased
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Alive": True,
                "Death": "NA",
                "Spouse": ["@I2@"]
            },
            "@I3@": {
                "ID": "@I3@",
                "Alive": True,
                "Death": "NA",
                "Spouse": []
            },
            "@I4@": {
                "ID": "@I4@",
                "Alive": False,
                "Death": "2020-06-01",
                "Spouse": ["@I6@"]
            },
            "@I5@": {
                "ID": "@I5@",
                "Alive": False,
                "Death": "2021-07-25",
                "Spouse": []
            }
        }
        families_dict = {} 
        self.assertEqual(validation(individuals_dict), "US30: Living married individuals: @I1@\n")

    def test4(self):
        """
        Many living/married individuals
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Alive": True,
                "Death": "NA",
                "Spouse": ["@I6@"]
            },
            "@I2@": {
                "ID": "@I2@",
                "Alive": True,
                "Death": "NA",
                "Spouse": ["@I1@"]
            },
            "@I3@": {
                "ID": "@I3@",
                "Alive": True,
                "Death": "NA",
                "Spouse": ["@I8@"]
            },
            "@I4@": {
                "ID": "@I4@",
                "Alive": True,
                "Death": "NA",
                "Spouse": ["@I9@"]
            },
            "@I5@": {
                "ID": "@I5@",
                "Alive": True,
                "Death": "NA",
                "Spouse": ["@I10@"]
            }
        }
        families_dict = {} 
        self.assertEqual(validation(individuals_dict), "US30: Living married individuals: @I1@, @I2@, @I3@, @I4@, @I5@\n")

    def test5(self):
        """
        
        """
        individuals_dict = {
           "@I1@": {
                "ID": "@I1@",
                "Alive": True,
                "Death": "NA",
                "Spouse": ["@I3@"]
            },
            "@I2@": {
                "ID": "@I2@",
                "Alive": True,
                "Death": "NA",
                "Spouse": []
            },
            "@I3@": {
                "ID": "@I3@",
                "Alive": True,
                "Death": "NA",
                "Spouse": ["@I1@"]
            },
            "@I4@": {
                "ID": "@I4@",
                "Alive": False,
                "Death": "2012-09-18",
                "Spouse": ["@I8@"]
            },
            "@I5@": {
                "ID": "@I5@",
                "Alive": False,
                "Death": "2013-04-03",
                "Spouse": []
            },
            "@I6@": {
                "ID": "@I6@",
                "Alive": True,
                "Death": "NA",
                "Spouse": ["@I7@"]
            }
        }
        families_dict = {} 
        self.assertEqual(validation(individuals_dict), "US30: Living married individuals: @I1@, @I3@, @I6@\n")

if __name__ == '__main__':
    unittest.main()