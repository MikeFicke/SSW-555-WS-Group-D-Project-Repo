# This file contains unit tests for the user story: US31 - List living single over 30
# SSW-555-WS
# Group D

import unittest
from US31_list_living_single_over_30 import validate_list_living_single_over_30
from io import StringIO
from contextlib import redirect_stdout


def validation(individuals_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_list_living_single_over_30(individuals_dict)
    output = buffer.getvalue()
    return output


class Test(unittest.TestCase):
    def test_living_single_over_30(self):
        """
        One living individual over 30 who has never been married.
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Alive": True,
                "Spouse": [],
                "Age": 35,
            }
        }
        self.assertEqual(
            validation(individuals_dict),
            "US31: Living individuals over 30 who have never been married: @I1@\n",
        )

    def test_no_individuals(self):
        """
        No individuals on file.
        """
        self.assertEqual(validation({}), "")

    def test_living_single_under_30_excluded(self):
        """
        Living, never married, but 30 or younger - should not appear.
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Alive": True,
                "Spouse": [],
                "Age": 25,
            }
        }
        self.assertEqual(validation(individuals_dict), "")

    def test_exactly_30_excluded(self):
        """
        Exactly 30 years old should not count as "over 30".
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Alive": True,
                "Spouse": [],
                "Age": 30,
            }
        }
        self.assertEqual(validation(individuals_dict), "")

    def test_living_married_over_30_excluded(self):
        """
        Living and over 30, but has been married - should not appear.
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Alive": True,
                "Spouse": ["@I2@"],
                "Age": 40,
            }
        }
        self.assertEqual(validation(individuals_dict), "")

    def test_deceased_over_30_single_excluded(self):
        """
        Deceased individual, over 30 and never married - should not appear.
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Alive": False,
                "Spouse": [],
                "Age": 45,
            }
        }
        self.assertEqual(validation(individuals_dict), "")

    def test_unknown_age_excluded(self):
        """
        Living, never married, but age is unknown ("NA") - should not appear.
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Alive": True,
                "Spouse": [],
                "Age": "NA",
            }
        }
        self.assertEqual(validation(individuals_dict), "")

    def test_mixed_group(self):
        """
        Mix of matching and non-matching individuals; only the qualifying
        living, single, over-30 individuals should be listed.
        """
        individuals_dict = {
            "@I1@": {  # matches: living, single, over 30
                "ID": "@I1@",
                "Alive": True,
                "Spouse": [],
                "Age": 32,
            },
            "@I2@": {  # excluded: married
                "ID": "@I2@",
                "Alive": True,
                "Spouse": ["@I5@"],
                "Age": 40,
            },
            "@I3@": {  # excluded: deceased
                "ID": "@I3@",
                "Alive": False,
                "Spouse": [],
                "Age": 50,
            },
            "@I4@": {  # excluded: 30 or under
                "ID": "@I4@",
                "Alive": True,
                "Spouse": [],
                "Age": 30,
            },
            "@I6@": {  # matches: living, single, over 30
                "ID": "@I6@",
                "Alive": True,
                "Spouse": [],
                "Age": 65,
            },
        }
        self.assertEqual(
            validation(individuals_dict),
            "US31: Living individuals over 30 who have never been married: @I1@, @I6@\n",
        )


if __name__ == '__main__':
    unittest.main()
