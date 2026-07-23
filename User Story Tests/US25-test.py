# Group D
# SSW-555-WS
# User Story 25 unit test file
# Author: Michael Ficke
# Acknowledgement: IDE Auto-complete was used for certain lines of code

import unittest
from US25_unique_first_names_and_dates_in_family import validate_unique_first_names_and_dates_in_family
from io import StringIO
from contextlib import redirect_stdout



def validation(individuals_dict, families_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_unique_first_names_and_dates_in_family(individuals_dict, families_dict)
    output = buffer.getvalue()
    return output


class TestUniqueFirstNamesAndDatesInFamily(unittest.TestCase):
    def test_unique_first_names_and_dates_in_family_1(self):
        """
        Valid.  Two families that have different named children with different birthdays
        """
        individuals_dict = {
            "@I1@": {"ID": "@I1@", "Name": "John /Doe/", "Birthday": "2000-01-01"},
            "@I2@": {"ID": "@I2@", "Name": "Jane /Doe/", "Birthday": "2002-05-15"},
            "@I3@": {"ID": "@I3@", "Name": "Tom /Smith/", "Birthday": "2005-03-10"},
            "@I4@": {"ID": "@I4@", "Name": "Sara /Smith/", "Birthday": "2007-08-20"},
        }
        families_dict = {
            "@F1@": {"ID": "@F1@", "Children": ["@I1@", "@I2@"]},
            "@F2@": {"ID": "@F2@", "Children": ["@I3@", "@I4@"]},
        }

        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test_unique_first_names_and_dates_in_family_2(self):
        """
        Valid.  Two children share a name but have separate birthdays.
        """
        individuals_dict = {
            "@I1@": {"ID": "@I1@", "Name": "John /Doe/", "Birthday": "2000-01-01"},
            "@I2@": {"ID": "@I2@", "Name": "John /Doe/", "Birthday": "2003-06-15"},
        }
        families_dict = {
            "@F1@": {"ID": "@F1@", "Children": ["@I1@", "@I2@"]},
        }

        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test_unique_first_names_and_dates_in_family_3(self):
        """
        Valid.  Two children share a different name, but the same birthday.
        """
        individuals_dict = {
            "@I1@": {"ID": "@I1@", "Name": "John /Doe/", "Birthday": "2000-01-01"},
            "@I2@": {"ID": "@I2@", "Name": "Jane /Doe/", "Birthday": "2000-01-01"},
        }
        families_dict = {
            "@F1@": {"ID": "@F1@", "Children": ["@I1@", "@I2@"]},
        }

        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test_unique_first_names_and_dates_in_family_4(self):
        """
        Invalid.  Two children share a name and a birthday.
        """
        individuals_dict = {
            "@I1@": {"ID": "@I1@", "Name": "John /Doe/", "Birthday": "2000-01-01"},
            "@I2@": {"ID": "@I2@", "Name": "John /Doe/", "Birthday": "2000-01-01"},
        }
        families_dict = {
            "@F1@": {"ID": "@F1@", "Children": ["@I1@", "@I2@"]},
        }

        self.assertNotEqual(validation(individuals_dict, families_dict), "")

    def test_unique_first_names_and_dates_in_family_5(self):
        """
        Invalid.  Two families; only one has children with a matching name and birthday
        """
        individuals_dict = {
            "@I1@": {"ID": "@I1@", "Name": "John /Doe/", "Birthday": "2000-01-01"},
            "@I2@": {"ID": "@I2@", "Name": "Jane /Doe/", "Birthday": "2002-05-15"},
            "@I3@": {"ID": "@I3@", "Name": "Tom /Smith/", "Birthday": "2005-03-10"},
            "@I4@": {"ID": "@I4@", "Name": "Tom /Smith/", "Birthday": "2005-03-10"},
        }
        families_dict = {
            "@F1@": {"ID": "@F1@", "Children": ["@I1@", "@I2@"]},
            "@F2@": {"ID": "@F2@", "Children": ["@I3@", "@I4@"]},
        }

        self.assertNotEqual(validation(individuals_dict, families_dict), "")

if __name__ == "__main__":
    unittest.main()