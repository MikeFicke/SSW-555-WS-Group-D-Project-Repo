# This file contains unit tests for the user story: US12 - Parents not too old
# SSW-555-WS
# William Bryce - Group D

import unittest
from US12_parents_not_too_old import validate_parents_not_too_old
from io import StringIO
from contextlib import redirect_stdout

def validation(individuals_dict, families_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_parents_not_too_old(individuals_dict, families_dict)
    output = buffer.getvalue()
    return output

class TestParentsNotTooOld(unittest.TestCase):
    def test1(self):
        """
        Valid ages for parents
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",         
                "Birthday": "1990-01-01"
            },
            "@I2@": {
                "ID": "@I2@",         
                "Birthday": "1990-01-01"
            },
            "@I3@": {
                "ID": "@I3@",         
                "Birthday": "2020-01-01"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": ["@I3@"]
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test2(self):
        """
        Mother 60+ years older than children
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",         
                "Birthday": "1950-01-01"
            },
            "@I2@": {
                "ID": "@I2@",         
                "Birthday": "1950-01-01"
            },
            "@I3@": {
                "ID": "@I3@",         
                "Birthday": "2020-01-01"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": ["@I3@"]
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "ERROR: US12: Mother (@I2@) is 60 or more years older than child (@I3@)\n")

    def test3(self):
        """
        Father 80+ years older than children
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",         
                "Birthday": "1930-01-01"
            },
            "@I2@": {
                "ID": "@I2@",         
                "Birthday": "1970-01-01"
            },
            "@I3@": {
                "ID": "@I3@",         
                "Birthday": "2020-01-01"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": ["@I3@"]
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "ERROR: US12: Father (@I1@) is 80 or more years older than child (@I3@)\n")

    def test4(self):
        """
        Father is 80+ years older and mother is 60+ years older than children
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",         
                "Birthday": "1930-01-01"
            },
            "@I2@": {
                "ID": "@I2@",         
                "Birthday": "1950-01-01"
            },
            "@I3@": {
                "ID": "@I3@",         
                "Birthday": "2020-01-01"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": ["@I3@"]
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict),
                        "ERROR: US12: Father (@I1@) is 80 or more years older than child (@I3@)\n" \
                        "ERROR: US12: Mother (@I2@) is 60 or more years older than child (@I3@)\n")

    def test5(self):
        """
        Parents too old for one child, valid ages for the other child
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",         
                "Birthday": "1930-01-01"
            },
            "@I2@": {
                "ID": "@I2@",         
                "Birthday": "1950-01-01"
            },
            "@I3@": {
                "ID": "@I3@",         
                "Birthday": "1980-01-01"
            },
            "@I4@": {
                "ID": "@I4@",
                "Birthday": "2020-01-01"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": ["@I3@", "@I4@"]
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict),
                        "ERROR: US12: Father (@I1@) is 80 or more years older than child (@I4@)\n" \
                        "ERROR: US12: Mother (@I2@) is 60 or more years older than child (@I4@)\n")

if __name__ == '__main__':
    unittest.main()