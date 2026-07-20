# This file contains unit tests for the user story: US24 - Unique families by spouses
# SSW-555-WS
# William Bryce - Group D

import unittest
from US24_unique_families_by_spouses import validate_unique_families_by_spouses
from io import StringIO
from contextlib import redirect_stdout

def validation(individuals_dict, families_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_unique_families_by_spouses(individuals_dict, families_dict)
    output = buffer.getvalue()
    return output

class Test(unittest.TestCase):
    def test1(self):
        """
        Valid families, different spouse names and marriage date
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",         
                "Name": "John /Doe/"
            },
            "@I2@": {
                "ID": "@I2@",         
                "Name": "Jane /Doe/"
            },
            "@I3@": {
                "ID": "@I3@",
                "Name": "Spouse /One/"
            },
            "@I4@": {
                "ID": "@I4@",
                "Name": "Spouse /Two/"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2000-06-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            },
            "@F2@": {
                "ID": "@F2@",
                "Married": "2010-05-15",
                "Husband ID": "@I3@",
                "Wife ID": "@I4@"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test2(self):
        """
        Valid families, same spouse names + different marriage dates
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",         
                "Name": "John /Doe/"
            },
            "@I2@": {
                "ID": "@I2@",         
                "Name": "Jane /Doe/"
            },
            "@I3@": {
                "ID": "@I3@",
                "Name": "John /Doe/"
            },
            "@I4@": {
                "ID": "@I4@",
                "Name": "Jane /Doe/"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2000-06-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            },
            "@F2@": {
                "ID": "@F2@",
                "Married": "2010-05-15",
                "Husband ID": "@I3@",
                "Wife ID": "@I4@"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test3(self):
        """
        Valid families, different spouse names + same marriage date
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",         
                "Name": "John /Doe/"
            },
            "@I2@": {
                "ID": "@I2@",         
                "Name": "Jane /Doe/"
            },
            "@I3@": {
                "ID": "@I3@",
                "Name": "Spouse /One/"
            },
            "@I4@": {
                "ID": "@I4@",
                "Name": "Spouse /Two/"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2000-06-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            },
            "@F2@": {
                "ID": "@F2@",
                "Married": "2000-06-01",
                "Husband ID": "@I3@",
                "Wife ID": "@I4@"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test4(self):
        """
        Invalid families, same spouse names and marriage date
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",         
                "Name": "John /Doe/"
            },
            "@I2@": {
                "ID": "@I2@",         
                "Name": "Jane /Doe/"
            },
            "@I3@": {
                "ID": "@I3@",
                "Name": "John /Doe/"
            },
            "@I4@": {
                "ID": "@I4@",
                "Name": "Jane /Doe/"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2000-06-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            },
            "@F2@": {
                "ID": "@F2@",
                "Married": "2000-06-01",
                "Husband ID": "@I3@",
                "Wife ID": "@I4@"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "ERROR: US23: FAMILIES (@F1@, @F2@): More than one family with the same husband (John /Doe/), wife (Jane /Doe/), and marriage date (2000-06-01).\n")

    def test5(self):
        """
        Two pairs of invalid families, same names and marriage date
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",         
                "Name": "John /Doe/"
            },
            "@I2@": {
                "ID": "@I2@",         
                "Name": "Jane /Doe/"
            },
            "@I3@": {
                "ID": "@I3@",
                "Name": "John /Doe/"
            },
            "@I4@": {
                "ID": "@I4@",
                "Name": "Jane /Doe/"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2000-06-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            },
            "@F2@": {
                "ID": "@F2@",
                "Married": "2000-06-01",
                "Husband ID": "@I3@",
                "Wife ID": "@I4@"
            },
            "@F3@": {
                "ID": "@F3@",
                "Married": "2015-03-20",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            },
            "@F4@": {
                "ID": "@F4@",
                "Married": "2015-03-20",
                "Husband ID": "@I3@",
                "Wife ID": "@I4@"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict),
                        "ERROR: US23: FAMILIES (@F1@, @F2@): More than one family with the same husband (John /Doe/), wife (Jane /Doe/), and marriage date (2000-06-01).\n"
                        "ERROR: US23: FAMILIES (@F3@, @F4@): More than one family with the same husband (John /Doe/), wife (Jane /Doe/), and marriage date (2015-03-20).\n")

if __name__ == '__main__':
    unittest.main()