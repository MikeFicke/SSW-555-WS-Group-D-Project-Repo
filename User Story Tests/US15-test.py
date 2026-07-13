# This file contains unit tests for the user story: US15 - Fewer than 15 siblings
# SSW-555-WS
# Sam Bryan - Group D

import unittest
from US15_fewer_than_15_siblings import validate_fewer_than_15_siblings
from io import StringIO
from contextlib import redirect_stdout

# helper function to capture print statements for unit tests


def validation(families_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_fewer_than_15_siblings(families_dict)
    output = buffer.getvalue()
    return output


class TestFewerThan15Siblings(unittest.TestCase):
    def test_fewer_than_15_siblings_1(self):
        """
        Family with no children
        """
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Children": []
            }
        }
        self.assertEqual(validation(families_dict), "")

    def test_fewer_than_15_siblings_2(self):
        """
        Family with well under 15 children
        """
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Children": [f"@I{i}@" for i in range(5)]
            }
        }
        self.assertEqual(validation(families_dict), "")

    def test_fewer_than_15_siblings_3(self):
        """
        Family with exactly 14 children (still valid)
        """
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Children": [f"@I{i}@" for i in range(14)]
            }
        }
        self.assertEqual(validation(families_dict), "")

    def test_fewer_than_15_siblings_4(self):
        """
        Family with exactly 15 children (invalid)
        """
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Children": [f"@I{i}@" for i in range(15)]
            }
        }
        self.assertIn("ERROR", validation(families_dict))

    def test_fewer_than_15_siblings_5(self):
        """
        Family with more than 15 children (invalid)
        """
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Children": [f"@I{i}@" for i in range(20)]
            }
        }
        self.assertIn("ERROR", validation(families_dict))

    def test_fewer_than_15_siblings_6(self):
        """
        Multiple families, only one of which is invalid
        """
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Children": [f"@I{i}@" for i in range(3)]
            },
            "@F2@": {
                "ID": "@F2@",
                "Children": [f"@I{i}@" for i in range(16)]
            }
        }
        output = validation(families_dict)
        self.assertIn("@F2@", output)
        self.assertNotIn("@F1@", output)


if __name__ == "__main__":
    unittest.main()
