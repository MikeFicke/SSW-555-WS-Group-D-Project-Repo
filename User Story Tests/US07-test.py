# This file contains unit tests for the user story: US07 - Less than 150 years old
# SSW-555-WS
# Michael Ficke - Group D

# Acknowledgement: IDE autocomplete was used on certain lines of code.

import unittest
from US07_less_than_150_years_old import validate_age_less_than_150
from io import StringIO
from contextlib import redirect_stdout

# helper function to capture print statements for unit tests
# citation: https://www.google.com/search?q=how+to+capture+print+statements+for+unittesting+in+Python&rlz=1C1CHBF_enUS1023US1023&oq=how+to+capture+print+statements+for+unittesting+in+Python&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQIRgKGKABMgkIAhAhGAoYoAEyCQgDECEYChigATIJCAQQIRgKGKABMgkIBRAhGAoYoAEyCQgGECEYChirAjIHCAcQIRifBdIBCDcwODhqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8


def validation(individuals_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_age_less_than_150(individuals_dict)
    output = buffer.getvalue()
    return output


class TestAgeLessThan150(unittest.TestCase):
    def test_age_less_than_150_1(self):
        """
        Living person under 150
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "2000-01-01",
                "Death": "NA",
            }
        }
        
        self.assertEqual(validation(individuals_dict), "")

    def test_age_less_than_150_2(self):
        """
        Living person who is 150+ years old
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "1750-01-01",
                "Death": "NA",
            }
        }
        self.assertEqual(validation(individuals_dict), "ERROR: INDIVIDUAL: @I1@: Age is 150 years or older.\n")

    def test_age_less_than_150_3(self):
        """
        Dead person who lived under 150 years
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "1900-01-01",
                "Death": "2020-01-01",
            }
        }
        self.assertEqual(validation(individuals_dict), "")

    def test_age_less_than_150_4(self):
        """
        Dead person who lived 150+ years
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "1800-01-01",
                "Death": "1960-01-01",
            }
        }
        self.assertEqual(validation(individuals_dict), "ERROR: INDIVIDUAL: @I1@: Age is 150 years or older.\n")

    def test_age_less_than_150_5(self):
        """
        Person born in NA
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "NA",
                "Death": "NA",
            }
        }
        self.assertEqual(validation(individuals_dict), "")

    def test_age_less_than_150_6(self):
        """
        Birthday is None.
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": None,
                "Death": "NA",
            }
        }
        self.assertEqual(validation(individuals_dict), "")
    
    def test_age_less_than_150_7(self):
        """
        Birthday is an empty string
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "",
                "Death": "NA",
            }
        }
        self.assertEqual(validation(individuals_dict), "")

    def test_age_less_than_150_8(self):
        """
        Death date is None (Not "NA")
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "2000-01-01",
                "Death": None,
            }
        }
        self.assertEqual(validation(individuals_dict), "")

    def test_age_less_than_150_9(self):
        """
        Person is exactly 149 years old 
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "1876-11-01",
                "Death": "2025-11-01",
            }
        }
        self.assertEqual(validation(individuals_dict), "")

    def test_age_less_than_150_10(self):
        """
        Person is exactly 150 years old
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "1875-11-01",
                "Death": "2025-11-01",
            }
        }
        self.assertEqual(validation(individuals_dict), "ERROR: INDIVIDUAL: @I1@: Age is 150 years or older.\n")


if __name__ == "__main__":
    unittest.main()
