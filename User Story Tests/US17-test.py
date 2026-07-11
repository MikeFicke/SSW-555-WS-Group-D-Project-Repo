# This file contains unit tests for the user story: US 17 - No marriages to descendants
# SSW-555-WS
# William Bryce - Group D

import unittest
from US17_no_marriages_to_descendants import validate_no_marriages_to_descendants
from io import StringIO
from contextlib import redirect_stdout

def validation(families_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_no_marriages_to_descendants(families_dict)
    output = buffer.getvalue()
    return output

class Test(unittest.TestCase):
    def test1(self):
        """
        Valid data, no marriages to descendants
        """
        individuals_dict = {}
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": ["@I3@"]
            }
        } 
        self.assertEqual(validation(families_dict), "")

    def test2(self):
        """
        Husband married to wife that is child
        """
        individuals_dict = {}
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": ["@I2@"]
            }
        }
        self.assertEqual(validation(families_dict), "ERROR: FAMILY: US17: @F1@: Husband (@I1@) married to descendant (@I2@)\n")

    def test3(self):
        """
        Wife married to husband that is child
        """
        individuals_dict = {}
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": ["@I1@"]
            }
        }
        self.assertEqual(validation(families_dict), "ERROR: FAMILY: US17: @F1@: Wife (@I2@) married to descendant (@I1@)\n")

    def test4(self):
        """
        Wife remarried to husband that is descendant
        """
        individuals_dict = {}
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": ["@I3@"]
            },
            "@F2@": {
                "ID": "@F2@",
                "Husband ID": "@I3@",
                "Wife ID": "@I4@",
                "Children": ["@I5@"]
            },
            "@F3@": {
                "ID": "@F3@",
                "Husband ID": "@I5@",
                "Wife ID": "@I2@",
                "Children": []
            }
        }
        self.assertEqual(validation(families_dict), "ERROR: FAMILY: US17: @F3@: Wife (@I2@) married to descendant (@I5@)\n")

    def test5(self):
        """
        Husband remarried to wife that is descendant
        """
        individuals_dict = {}
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": ["@I3@"]
            },
            "@F2@": {
                "ID": "@F2@",
                "Husband ID": "@I3@",
                "Wife ID": "@I4@",
                "Children": ["@I5@"]
            },
            "@F3@": {
                "ID": "@F3@",
                "Husband ID": "@I1@",
                "Wife ID": "@I5@",
                "Children": []
            }
        }
        self.assertEqual(validation(families_dict), "ERROR: FAMILY: US17: @F3@: Husband (@I1@) married to descendant (@I5@)\n")

if __name__ == '__main__':
    unittest.main()