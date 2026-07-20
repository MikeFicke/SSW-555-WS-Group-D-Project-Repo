# This file contains unit tests for the user story: US 19 - First cousins should not marry one another
# SSW-555-WS
# Samantha Bryan - Group D

import unittest
from US19_no_marriage_between_first_cousins import validate_no_marriage_between_first_cousins
from io import StringIO
from contextlib import redirect_stdout

def validation(families_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_no_marriage_between_first_cousins(families_dict)
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

    def test2(self):
        """
        Husband and wife are first cousins: their parents (@I1@ and @I4@) are siblings from @F1@
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
        self.assertEqual(
            validation(families_dict),
            "ERROR: FAMILY: US19: @F4@: Husband (@I3@) and Wife (@I6@) are first cousins\n"
        )

    def test3(self):
        """
        Husband and wife are siblings, not cousins - should not be flagged by this validation
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
        self.assertEqual(validation(families_dict), "")

    def test4(self):
        """
        Multiple first-cousin marriages flagged across different families
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
            },
            "@F5@": {
                "ID": "@F5@",
                "Husband ID": "@I10@",
                "Wife ID": "@I10W@",
                "Children": ["@I11@", "@I14@"]
            },
            "@F6@": {
                "ID": "@F6@",
                "Husband ID": "@I11@",
                "Wife ID": "@I12@",
                "Children": ["@I13@"]
            },
            "@F7@": {
                "ID": "@F7@",
                "Husband ID": "@I14@",
                "Wife ID": "@I15@",
                "Children": ["@I16@"]
            },
            "@F8@": {
                "ID": "@F8@",
                "Husband ID": "@I13@",
                "Wife ID": "@I16@",
                "Children": []
            }
        }
        self.assertEqual(
            validation(families_dict),
            "ERROR: FAMILY: US19: @F4@: Husband (@I3@) and Wife (@I6@) are first cousins\n"
            "ERROR: FAMILY: US19: @F8@: Husband (@I13@) and Wife (@I16@) are first cousins\n"
        )

    def test5(self):
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
