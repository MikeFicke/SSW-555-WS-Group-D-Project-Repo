# This file contains unit tests for the user story: US 20 - Aunts and uncles should not marry their nieces or nephews
# SSW-555-WS
# Samantha Bryan - Group D

import unittest
from US20_no_marriage_between_aunt_uncle_and_niece_nephew import validate_no_marriage_between_aunt_uncle_and_niece_nephew
from io import StringIO
from contextlib import redirect_stdout

def validation(families_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_no_marriage_between_aunt_uncle_and_niece_nephew(families_dict)
    output = buffer.getvalue()
    return output

class Test(unittest.TestCase):
    def test1(self):
        """
        Valid data, husband and wife are not related
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
                "Children": []
            }
        }
        self.assertEqual(validation(families_dict), "")

    def test2(self):
        """
        Husband is the uncle of the wife: husband (@I2@) is a sibling of wife's father (@I1@) from @F1@
        """
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Husband ID": "@I0@",
                "Wife ID": "@I0W@",
                "Children": ["@I1@", "@I2@"]
            },
            "@F2@": {
                "ID": "@F2@",
                "Husband ID": "@I1@",
                "Wife ID": "@I5@",
                "Children": ["@I6@"]
            },
            "@F3@": {
                "ID": "@F3@",
                "Husband ID": "@I2@",
                "Wife ID": "@I6@",
                "Children": []
            }
        }
        self.assertEqual(
            validation(families_dict),
            "ERROR: FAMILY: US20: @F3@: Husband (@I2@) and Wife (@I6@) are aunt/uncle and niece/nephew\n"
        )

    def test3(self):
        """
        Wife is the aunt of the husband: wife (@I2@) is a sibling of husband's mother (@I1@) from @F1@
        """
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Husband ID": "@I0@",
                "Wife ID": "@I0W@",
                "Children": ["@I1@", "@I2@"]
            },
            "@F2@": {
                "ID": "@F2@",
                "Husband ID": "@I5@",
                "Wife ID": "@I1@",
                "Children": ["@I6@"]
            },
            "@F3@": {
                "ID": "@F3@",
                "Husband ID": "@I6@",
                "Wife ID": "@I2@",
                "Children": []
            }
        }
        self.assertEqual(
            validation(families_dict),
            "ERROR: FAMILY: US20: @F3@: Husband (@I6@) and Wife (@I2@) are aunt/uncle and niece/nephew\n"
        )

    def test4(self):
        """
        First cousins should not be flagged by this validation (that's US19's job)
        """
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Husband ID": "@I0@",
                "Wife ID": "@I0W@",
                "Children": ["@I1@", "@I4@"]
            },
            "@F2@": {
                "ID": "@F2@",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": ["@I3@"]
            },
            "@F3@": {
                "ID": "@F3@",
                "Husband ID": "@I4@",
                "Wife ID": "@I5@",
                "Children": ["@I6@"]
            },
            "@F4@": {
                "ID": "@F4@",
                "Husband ID": "@I3@",
                "Wife ID": "@I6@",
                "Children": []
            }
        }
        self.assertEqual(validation(families_dict), "")

    def test5(self):
        """
        Multiple aunt/uncle-niece/nephew marriages flagged across different families
        """
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Husband ID": "@I0@",
                "Wife ID": "@I0W@",
                "Children": ["@I1@", "@I2@"]
            },
            "@F2@": {
                "ID": "@F2@",
                "Husband ID": "@I1@",
                "Wife ID": "@I5@",
                "Children": ["@I6@"]
            },
            "@F3@": {
                "ID": "@F3@",
                "Husband ID": "@I2@",
                "Wife ID": "@I6@",
                "Children": []
            },
            "@F4@": {
                "ID": "@F4@",
                "Husband ID": "@I10@",
                "Wife ID": "@I10W@",
                "Children": ["@I11@", "@I12@"]
            },
            "@F5@": {
                "ID": "@F5@",
                "Husband ID": "@I15@",
                "Wife ID": "@I11@",
                "Children": ["@I16@"]
            },
            "@F6@": {
                "ID": "@F6@",
                "Husband ID": "@I16@",
                "Wife ID": "@I12@",
                "Children": []
            }
        }
        self.assertEqual(
            validation(families_dict),
            "ERROR: FAMILY: US20: @F3@: Husband (@I2@) and Wife (@I6@) are aunt/uncle and niece/nephew\n"
            "ERROR: FAMILY: US20: @F6@: Husband (@I16@) and Wife (@I12@) are aunt/uncle and niece/nephew\n"
        )

    def test6(self):
        """
        Husband or wife has no known parent family - should not error out or be flagged
        """
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": []
            }
        }
        self.assertEqual(validation(families_dict), "")

if __name__ == '__main__':
    unittest.main()
