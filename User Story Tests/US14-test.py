# Group D - Michael Ficke
# SSW-555-WS

# Acknowledgement: IDE auto-complete was used for certain lines of code

# Unit testing file user story 14: no more than 5 births.

import unittest
from US14_multiple_births import validate_multiple_births
from io import StringIO
from contextlib import redirect_stdout



def validation(individuals_dict, family_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_multiple_births(individuals_dict, family_dict)
    output = buffer.getvalue()
    return output


class TestMultipleBirths(unittest.TestCase):
    def test_multiple_births_1(self):
        """
        Valid family, 3 children share a birthday
        """
        individuals_dict = {
            "@I1@": {"Birthday": "2000-06-15"},
            "@I2@": {"Birthday": "2000-06-15"},
            "@I3@": {"Birthday": "2000-06-15"}
        }
        family_dict = {
            "@F1@": {"Children": ["@I1@", "@I2@", "@I3@"]}
        }
        
        self.assertEqual(validation(individuals_dict, family_dict), "")


    def test_multiple_births_2(self):
        """
        Valid family, exactly 5 children share a birthday
        """
        individuals_dict = {
            "@I1@": {"Birthday": "2000-06-15"},
            "@I2@": {"Birthday": "2000-06-15"},
            "@I3@": {"Birthday": "2000-06-15"},
            "@I4@": {"Birthday": "2000-06-15"},
            "@I5@": {"Birthday": "2000-06-15"}
        }
        family_dict = {
            "@F1@": {"Children": ["@I1@", "@I2@", "@I3@", "@I4@", "@I5@"]}
        }
        self.assertEqual(validation(individuals_dict, family_dict), "")
        

    def test_multiple_births_3(self):
        """
        Invalid family, 6 children share a birthday
        """
        individuals_dict = {
            "@I1@": {"Birthday": "2000-06-15"},
            "@I2@": {"Birthday": "2000-06-15"},
            "@I3@": {"Birthday": "2000-06-15"},
            "@I4@": {"Birthday": "2000-06-15"},
            "@I5@": {"Birthday": "2000-06-15"},
            "@I6@": {"Birthday": "2000-06-15"}
        }
        family_dict = {
            "@F1@": {"Children": ["@I1@", "@I2@", "@I3@", "@I4@", "@I5@", "@I6@"]}
        }
        
        self.assertNotEqual(validation(individuals_dict, family_dict), "")
        

    def test_multiple_births_4(self):
        """
        Family with no children
        """
        individuals_dict = {
        }
        family_dict = {
            "@F1@": {"Children": []}
        }
        
        self.assertEqual(validation(individuals_dict, family_dict), "")
        

    def test_multiple_births_5(self):
        """
        Mixed family, some children share birthday, some don't
        """
        individuals_dict = {
            "@I1@": {"Birthday": "2000-06-15"},
            "@I2@": {"Birthday": "2000-06-15"},
            "@I3@": {"Birthday": "2000-06-15"},
            "@I4@": {"Birthday": "2000-06-15"},
            "@I5@": {"Birthday": "2000-06-15"},
            "@I6@": {"Birthday": "2000-06-18"}
        }
        family_dict = {
            "@F1@": {"Children": ["@I1@", "@I2@", "@I3@", "@I4@", "@I5@", "@I6@"]}
        }
        self.assertEqual(validation(individuals_dict, family_dict), "")


if __name__ == "__main__":
    unittest.main()
