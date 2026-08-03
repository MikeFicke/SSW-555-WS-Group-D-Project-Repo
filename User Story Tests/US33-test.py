# This file contains unit tests for the user story: US33 - List orphans
# SSW-555-WS
# William Bryce - Group D

import unittest
from US33_list_orphans import validate_list_orphans
from io import StringIO
from contextlib import redirect_stdout

def validation(individuals_dict, families_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_list_orphans(individuals_dict, families_dict)
    output = buffer.getvalue()
    return output

class Test(unittest.TestCase):
    def test1(self):
        """
        No orphans, both parents alive
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "1980-01-01",
                "Death": "NA"
            },
            "@I2@": {
                "ID": "@I2@",
                "Birthday": "1980-01-01",
                "Death": "NA"
            },
            "@I3@": {
                "ID": "@I3@",
                "Birthday": "2000-01-01",
                "Death": "NA"
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
        No orphans, both parents dead but child >18 years old
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "1980-01-01",
                "Death": "2023-05-17"
            },
            "@I2@": {
                "ID": "@I2@",
                "Birthday": "1980-01-01",
                "Death": "2024-06-08"
            },
            "@I3@": {
                "ID": "@I3@",
                "Birthday": "2000-01-01",
                "Death": "NA"
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

    def test3(self):
        """
        One orphan
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "1980-01-01",
                "Death": "2020-01-09"
            },
            "@I2@": {
                "ID": "@I2@",
                "Birthday": "1980-01-01",
                "Death": "2020-01-09"
            },
            "@I3@": {
                "ID": "@I3@",
                "Birthday": "2016-01-01",
                "Death": "NA"
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
        self.assertEqual(validation(individuals_dict, families_dict), "US33: Orphans: @I3@\n")

    def test4(self):
        """
        Multiple orphans
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "1980-01-01",
                "Death": "2020-01-09"
            },
            "@I2@": {
                "ID": "@I2@",
                "Birthday": "1980-01-01",
                "Death": "2020-01-09"
            },
            "@I3@": {
                "ID": "@I3@",
                "Birthday": "2016-01-01",
                "Death": "NA"
            },
            "@I4@": {
                "ID": "@I4@",
                "Birthday": "2016-01-01",
                "Death": "NA"
            },
            "@I5@": {
                "ID": "@I5@",
                "Birthday": "2016-01-01",
                "Death": "NA"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": ["@I3@", "@I4@", "@I5@"]
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "US33: Orphans: @I3@, @I4@, @I5@\n")

    def test5(self):
        """
        Three children, two orphans and one >18 years old
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "1980-01-01",
                "Death": "2020-01-09"
            },
            "@I2@": {
                "ID": "@I2@",
                "Birthday": "1980-01-01",
                "Death": "2020-01-09"
            },
            "@I3@": {
                "ID": "@I3@",
                "Birthday": "2016-01-01",
                "Death": "NA"
            },
            "@I4@": {
                "ID": "@I4@",
                "Birthday": "2016-01-01",
                "Death": "NA"
            },
            "@I5@": {
                "ID": "@I5@",
                "Birthday": "2000-01-01",
                "Death": "NA"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": ["@I3@", "@I4@", "@I5@"]
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "US33: Orphans: @I3@, @I4@\n")

if __name__ == '__main__':
    unittest.main()