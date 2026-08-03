# This file contains unit tests for the user story: US32 - List multiple births
# SSW-555-WS
# William Bryce - Group D

import unittest
from US32_list_multiple_births import validate_list_multiple_births
from io import StringIO
from contextlib import redirect_stdout

def validation(individuals_dict, families_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_list_multiple_births(individuals_dict, families_dict)
    output = buffer.getvalue()
    return output

class Test(unittest.TestCase):
    def test1(self):
        """
        No multiple births
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",         
                "Birthday": "2000-06-01"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Children": ["@I1@"]
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test2(self):
        """
        One multiple birth, twins
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",         
                "Birthday": "2000-06-01"
            },
            "@I2@": {
                "ID": "@I2@",         
                "Birthday": "2000-06-01"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Children": ["@I1@", "@I2@"]
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "US32: @F1@: Multiple births: @I1@, @I2@\n")

    def test3(self):
        """
        One multiple birth, triplets
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",         
                "Birthday": "2000-06-01"
            },
            "@I2@": {
                "ID": "@I2@",         
                "Birthday": "2000-06-01"
            },
            "@I3@": {
                "ID": "@I3@",
                "Birthday": "2000-06-02"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Children": ["@I1@", "@I2@", "@I3@"]
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "US32: @F1@: Multiple births: @I1@, @I2@, @I3@\n")

    def test4(self):
        """
        Two groups of multiple births in one family
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",         
                "Birthday": "2000-06-01"
            },
            "@I2@": {
                "ID": "@I2@",         
                "Birthday": "2000-06-01"
            },
            "@I3@": {
                "ID": "@I3@",         
                "Birthday": "2003-01-01"
            },
            "@I4@": {
                "ID": "@I4@",         
                "Birthday": "2003-01-01"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Children": ["@I1@", "@I2@", "@I3@", "@I4@"]
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), 
                        "US32: @F1@: Multiple births: @I1@, @I2@\n" \
                        "US32: @F1@: Multiple births: @I3@, @I4@\n")

    def test5(self):
        """
        Two families each with twins
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",         
                "Birthday": "2000-06-01"
            },
            "@I2@": {
                "ID": "@I2@",         
                "Birthday": "2000-06-01"
            },
            "@I3@": {
                "ID": "@I3@",         
                "Birthday": "2000-01-01"
            },
            "@I4@": {
                "ID": "@I4@",         
                "Birthday": "2000-01-01"
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Children": ["@I1@", "@I2@"]
            },
            "@F2@": {
                "ID": "@F2@",
                "Children": ["@I3@", "@I4@"]
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), 
                        "US32: @F1@: Multiple births: @I1@, @I2@\n" \
                        "US32: @F2@: Multiple births: @I3@, @I4@\n")

if __name__ == '__main__':
    unittest.main()