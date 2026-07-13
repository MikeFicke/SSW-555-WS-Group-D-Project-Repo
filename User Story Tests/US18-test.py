# This file contains unit tests for the user story: US 18 - Siblings should not marry one another
# SSW-555-WS
# Samantha Bryan - Group D

import unittest
from US18_no_marriage_between_siblings import validate_no_marriage_between_siblings
from io import StringIO
from contextlib import redirect_stdout

def validation(families_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_no_marriage_between_siblings(families_dict)
    output = buffer.getvalue()
    return output

class Test(unittest.TestCase):
    def test1(self):
        """
        Valid data, husband and wife are not siblings
        """
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": ["@I3@", "@I4@"]
            },
            "@F2@": {
                "ID": "@F2@",
                "Husband ID": "@I5@",
                "Wife ID": "@I6@",
                "Children": []
            }
        }
        self.assertEqual(validation(families_dict), "")

    def test2(self):
        """
        Husband and wife are siblings (both children in the same family)
        """
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": ["@I3@", "@I4@"]
            },
            "@F2@": {
                "ID": "@F2@",
                "Husband ID": "@I3@",
                "Wife ID": "@I4@",
                "Children": []
            }
        }
        self.assertEqual(validation(families_dict), "ERROR: FAMILY: US18: @F2@: Husband (@I3@) and Wife (@I4@) are siblings from family (@F1@)\n")

    def test3(self):
        """
        Half-siblings are not flagged (only share one family as full siblings; different families as children means not siblings here)
        """
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": ["@I3@"]
            },
            "@F2@": {
                "ID": "@F2@",
                "Husband ID": "@I1@",
                "Wife ID": "@I6@",
                "Children": ["@I4@"]
            },
            "@F3@": {
                "ID": "@F3@",
                "Husband ID": "@I3@",
                "Wife ID": "@I4@",
                "Children": []
            }
        }
        self.assertEqual(validation(families_dict), "")

    def test4(self):
        """
        Multiple sibling marriages flagged across different families
        """
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": ["@I3@", "@I4@"]
            },
            "@F2@": {
                "ID": "@F2@",
                "Husband ID": "@I5@",
                "Wife ID": "@I6@",
                "Children": ["@I7@", "@I8@"]
            },
            "@F3@": {
                "ID": "@F3@",
                "Husband ID": "@I3@",
                "Wife ID": "@I4@",
                "Children": []
            },
            "@F4@": {
                "ID": "@F4@",
                "Husband ID": "@I7@",
                "Wife ID": "@I8@",
                "Children": []
            }
        }
        self.assertEqual(
            validation(families_dict),
            "ERROR: FAMILY: US18: @F3@: Husband (@I3@) and Wife (@I4@) are siblings from family (@F1@)\n"
            "ERROR: FAMILY: US18: @F4@: Husband (@I7@) and Wife (@I8@) are siblings from family (@F2@)\n"
        )

    def test5(self):
        """
        Only children of the same family (siblings), not just any two people, are flagged
        """
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": ["@I3@"]
            },
            "@F2@": {
                "ID": "@F2@",
                "Husband ID": "@I4@",
                "Wife ID": "@I5@",
                "Children": ["@I6@"]
            },
            "@F3@": {
                "ID": "@F3@",
                "Husband ID": "@I3@",
                "Wife ID": "@I6@",
                "Children": []
            }
        }
        self.assertEqual(validation(families_dict), "")

if __name__ == '__main__':
    unittest.main()
