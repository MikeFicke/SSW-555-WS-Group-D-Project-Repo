# This file contains unit tests for the user story: US 13 - Siblings spacing
# SSW-555-WS
# William Bryce - Group D

import unittest
from US13_siblings_spacing import validate_siblings_spacing
from io import StringIO
from contextlib import redirect_stdout

def validation(individuals_dict, families_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_siblings_spacing(individuals_dict, families_dict)
    output = buffer.getvalue()
    return output

class Test(unittest.TestCase):
    def test1(self):
        """
        Valid spacing, more than 8 months apart
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "2020-01-01"
            },
            "@I2@": {
                "ID": "@I2@",
                "Birthday": "2020-12-01"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Children": ["@I1@", "@I2@"]
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test2(self):
        """
        Valid spacing, less than 2 days apart
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "2020-01-01"
            },
            "@I2@": {
                "ID": "@I2@",
                "Birthday": "2020-01-02"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Children": ["@I1@", "@I2@"]
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test3(self):
        """
        Invalid sibling spacing
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "2020-01-01"
            },
            "@I2@": {
                "ID": "@I2@",
                "Birthday": "2020-04-01"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Children": ["@I1@", "@I2@"]
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "ERROR: FAMILY: US13: @F1@: Siblings (@I1@ and @I2@) have birthdays 2 days to 8 months apart\n")

    def test4(self):
        """
        Many siblings, half valid/half invalid spacing
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "2020-01-01"
            },
            "@I2@": {
                "ID": "@I2@",
                "Birthday": "2020-01-02"
            },
            "@I3@": {
                "ID": "@I3@",
                "Birthday": "2020-04-01"
            },
            "@I4@": {
                "ID": "@I4@",
                "Birthday": "2020-04-02"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Children": ["@I1@", "@I2@", "@I3@", "@I4@"]
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict),
                        "ERROR: FAMILY: US13: @F1@: Siblings (@I1@ and @I3@) have birthdays 2 days to 8 months apart\n" \
                        "ERROR: FAMILY: US13: @F1@: Siblings (@I1@ and @I4@) have birthdays 2 days to 8 months apart\n" \
                        "ERROR: FAMILY: US13: @F1@: Siblings (@I2@ and @I3@) have birthdays 2 days to 8 months apart\n" \
                        "ERROR: FAMILY: US13: @F1@: Siblings (@I2@ and @I4@) have birthdays 2 days to 8 months apart\n")

    def test5(self):
        """
        Third sibling with invalid spacing to one twin
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "2020-01-01"
            },
            "@I2@": {
                "ID": "@I2@",
                "Birthday": "2020-01-02"
            },
            "@I3@": {
                "ID": "@I3@",
                "Birthday": "2020-09-02"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Children": ["@I1@", "@I2@", "@I3@"]
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "ERROR: FAMILY: US13: @F1@: Siblings (@I2@ and @I3@) have birthdays 2 days to 8 months apart\n")

if __name__ == '__main__':
    unittest.main()