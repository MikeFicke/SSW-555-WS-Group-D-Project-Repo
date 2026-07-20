# This file contains unit tests for the user story: US23 - Unique name and birth date
# SSW-555-WS
# William Bryce - Group D

import unittest
from US23_unique_name_and_birth_date import validate_unique_name_and_birth_date
from io import StringIO
from contextlib import redirect_stdout

def validation(individuals_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_unique_name_and_birth_date(individuals_dict)
    output = buffer.getvalue()
    return output

class Test(unittest.TestCase):
    def test1(self):
        """
        Valid individuals, different name and birth date
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Name": "John /Doe/",
                "Birthday": "2000-06-01",
            },
            "@I2@": {
                "ID": "@I2@",
                "Name": "Test /One/",
                "Birthday": "1995-10-25",
            }
        }
        families_dict = {} 
        self.assertEqual(validation(individuals_dict), "")

    def test2(self):
        """
        Valid individuals, same name + different birth dates
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Name": "John /Doe/",
                "Birthday": "2000-06-01",
            },
            "@I2@": {
                "ID": "@I2@",
                "Name": "John /Doe/",
                "Birthday": "1995-10-25",
            }
        }
        families_dict = {}
        self.assertEqual(validation(individuals_dict), "")

    def test3(self):
        """
        Valid individuals, different names + same birth dates
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Name": "John /Doe/",
                "Birthday": "2000-06-01",
            },
            "@I2@": {
                "ID": "@I2@",
                "Name": "Test /Three/",
                "Birthday": "2000-06-01",
            }
        }
        families_dict = {}
        self.assertEqual(validation(individuals_dict), "")

    def test4(self):
        """
        Invalid individuals, same name and birth date
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Name": "John /Doe/",
                "Birthday": "2000-06-01",
            },
            "@I2@": {
                "ID": "@I2@",
                "Name": "John /Doe/",
                "Birthday": "2000-06-01",
            }
        }
        families_dict = {}
        self.assertEqual(validation(individuals_dict), "ERROR: US23: INDIVIDUALS (@I1@, @I2@): More than one individual with name (John /Doe/) and birth date (2000-06-01).\n")

    def test5(self):
        """
        Two pairs of invalid individuals with same name and birth date
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Name": "John /Doe/",
                "Birthday": "2000-06-01",
            },
            "@I2@": {
                "ID": "@I2@",
                "Name": "John /Doe/",
                "Birthday": "2000-06-01",
            },
            "@I3@": {
                "ID": "@I3@",
                "Name": "Jane /Doe/",
                "Birthday": "2000-06-01",
            },
            "@I4@": {
                "ID": "@I4@",
                "Name": "Jane /Doe/",
                "Birthday": "2000-06-01",
            }
        }
        families_dict = {}
        self.assertEqual(validation(individuals_dict), 
                        "ERROR: US23: INDIVIDUALS (@I1@, @I2@): More than one individual with name (John /Doe/) and birth date (2000-06-01).\n"
                        "ERROR: US23: INDIVIDUALS (@I3@, @I4@): More than one individual with name (Jane /Doe/) and birth date (2000-06-01).\n")

if __name__ == '__main__':
    unittest.main()