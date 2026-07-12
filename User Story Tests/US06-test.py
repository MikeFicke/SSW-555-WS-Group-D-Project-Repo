# This file contains unit tests for the user story: US06 - Divorce before death
# SSW-555-WS
# William Bryce - Group D

import unittest
from US06_divorce_before_death import validate_divorce_before_death
from io import StringIO
from contextlib import redirect_stdout

def validation(individuals_dict, families_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_divorce_before_death(individuals_dict, families_dict)
    output = buffer.getvalue()
    return output

class TestDivorceBeforeDeath(unittest.TestCase):
    def test1(self):
        """
        Valid divorce date before husband's death
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Death": "2020-06-01"
            },
            "@I2@": {
                "ID": "@I2@",
                "Death": "NA"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Divorced": "1990-01-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test2(self):
        """
        Divorce after husband's death
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Death": "2020-06-01"
            },
            "@I2@": {
                "ID": "@I2@",
                "Death": "NA"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Divorced": "2022-05-14",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "ERROR: FAMILY: US06: @F1@: Divorced 2022-05-14 after husband's (@I1@) death on 2020-06-01\n")

    def test3(self):
        """
        Divorce after wife's death
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Death": "NA"
            },
            "@I2@": {
                "ID": "@I2@",
                "Death": "2020-06-01"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Divorced": "2022-06-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "ERROR: FAMILY: US06: @F1@: Divorced 2022-06-01 after wife's (@I2@) death on 2020-06-01\n")

    def test4(self):
        """
        Divorce after death of both husband and wife
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Death": "2020-06-01"
            },
            "@I2@": {
                "ID": "@I2@",
                "Death": "2015-01-03"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Divorced": "2022-06-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict),
                        "ERROR: FAMILY: US06: @F1@: Divorced 2022-06-01 after husband's (@I1@) death on 2020-06-01\n" \
                        "ERROR: FAMILY: US06: @F1@: Divorced 2022-06-01 after wife's (@I2@) death on 2015-01-03\n")

    def test5(self):
        """
        Valid divorce date before death of both spouses
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Death": "2020-06-01"
            },
            "@I2@": {
                "ID": "@I2@",
                "Death": "2015-01-03"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Divorced": "2010-08-15",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test6(self):
        """
        Valid divorce date, both living
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Death": "NA"
            },
            "@I2@": {
                "ID": "@I2@",
                "Death": "NA"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Divorced": "2010-08-15",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

if __name__ == '__main__':
    unittest.main()