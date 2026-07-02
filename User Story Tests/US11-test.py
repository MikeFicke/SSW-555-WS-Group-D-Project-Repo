# This file contains unit tests for the user story: US11 - no bigamy
# SSW-555-WS
# Michael Ficke - Group D

# Acknowledgement: IDE autocomplete was used on certain lines of code.

import unittest
from US11_no_bigamy import validate_no_bigamy
from io import StringIO
from contextlib import redirect_stdout

# helper function to capture print statements for unit tests
# citation: https://www.google.com/search?q=how+to+capture+print+statements+for+unittesting+in+Python&rlz=1C1CHBF_enUS1023US1023&oq=how+to+capture+print+statements+for+unittesting+in+Python&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQIRgKGKABMgkIAhAhGAoYoAEyCQgDECEYChigATIJCAQQIRgKGKABMgkIBRAhGAoYoAEyCQgGECEYChirAjIHCAcQIRifBdIBCDcwODhqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8


def validation(individuals_dict, families_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_no_bigamy(individuals_dict, families_dict)
    output = buffer.getvalue()
    return output


class TestNoBigamy(unittest.TestCase):
    def test_no_bigamy_1(self):
        """
        Person with only one marriage
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Spouse": ["@F1@"],
                "Death": "NA",
            },
            "@I2@": {
                "ID": "@I2@",
                "Spouse": ["@F1@"],
                "Death": "NA",
            }
        }
        families_dict = {
            "@F1@": {
                "Married": "2000-01-01",
                "Divorced": "NA",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test_no_bigamy_2(self):
        """
        Person with two sequential marriages (no overlap)
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Spouse": ["@F1@", "@F2@"],
                "Death": "NA",
            },
            "@I2@": {
                "ID": "@I2@",
                "Spouse": ["@F1@"],
                "Death": "NA",
            },
            "@I3@": {
                "ID": "@I3@",
                "Spouse": ["@F2@"],
                "Death": "NA",
            }
        }
        families_dict = {
            "@F1@": {
                "Married": "2000-01-01",
                "Divorced": "2005-01-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            },
            "@F2@": {
                "Married": "2006-01-01",
                "Divorced": "NA",
                "Husband ID": "@I1@",
                "Wife ID": "@I3@"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test_no_bigamy_3(self):
        """
        Two overlapping marriages
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Spouse": ["@F1@", "@F2@"],
                "Death": "NA",
            },
            "@I2@": {
                "ID": "@I2@",
                "Spouse": ["@F1@"],
                "Death": "NA",
            },
            "@I3@": {
                "ID": "@I3@",
                "Spouse": ["@F2@"],
                "Death": "NA",
            }
        }
        families_dict = {
            "@F1@": {
                "Married": "2000-01-01",
                "Divorced": "NA",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            },
            "@F2@": {
                "Married": "2003-01-01",
                "Divorced": "NA",
                "Husband ID": "@I1@",
                "Wife ID": "@I3@"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), f"ERROR: Person {individuals_dict['@I1']['ID']} is married to more than one person at the same time.\n")
    
    def test_no_bigamy_4(self):
        """
        No spouse list
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Spouse": "NA",
                "Death": "NA",
            },
        }
        families_dict = {}
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test_no_bigamy_5(self):
        """
        Spouse died, then person remarried
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Spouse": ["@F1@", "@F2@"],
                "Death": "NA",
            },
            "@I2@": {
                "ID": "@I2@",
                "Spouse": ["@F1@"],
                "Death": "2004-01-01",
            },
            "@I3@": {
                "ID": "@I3@",
                "Spouse": ["@F2@"],
                "Death": "NA",
            }
        }
        families_dict = {
            "@F1@": {
                "Married": "2000-01-01",
                "Divorced": "NA",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            },
            "@F2@": {
                "Married": "2006-01-01",
                "Divorced": "NA",
                "Husband ID": "@I1@",
                "Wife ID": "@I3@"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")
