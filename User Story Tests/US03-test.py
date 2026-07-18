# This file is for the M4.B1: Assignment: Homework Assignment 4: Test First submission.
# SSW-555-WS
# Michael Ficke - Group D

# This code file will perform unit tests on the user story for sprint 1 involving "birth before death".

# citation: https://www.geeksforgeeks.org/python/unit-testing-python-unittest/

# Acknowledgement: IDE autocomplete was used on certain lines of code.

import unittest
from US03_birth_before_death import validate_birth_before_death
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
        validate_birth_before_death(individuals_dict)
    output = buffer.getvalue()
    return output


class TestBirthBeforeDeath(unittest.TestCase):
    def test_birth_before_death_1(self):
        """
        Valid individual born 1990, died 2020.
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "1990-01-01",
                "Death": "2020-01-01",
            }
        }
        self.assertEqual(validation(individuals_dict), "")

    def test_birth_before_death_2(self):
        """
        Invalid individual born 2020, died 2010.
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "2020-01-01",
                "Death": "2010-01-01",
            }
        }
        self.assertEqual(validation(individuals_dict), "ERROR: Birth date 2020-01-01 is after or the same as death date 2010-01-01 for individual @I1@\n")

    def test_birth_before_death_3(self):
        """
        Invalid individual born 01-01-1990,died 01-01-1990.
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "1990-01-01",
                "Death": "1990-01-01",
            }
        }
        self.assertEqual(validation(individuals_dict), "ERROR: Birth date 1990-01-01 is after or the same as death date 1990-01-01 for individual @I1@\n")

    def test_birth_before_death_4(self):
        """
        Valid individual born in 1985, and has not died.
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "1985-01-01",
                "Death": "NA"
            }
        }
        self.assertEqual(validation(individuals_dict), "")

    def test_birth_before_death_5(self):
        """
        Mixture of individuals where several are valid and one is invalid.
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "2010-01-01",
                "Death": "2020-01-01",
            },
            "@I2@": {
                "ID": "@I2@",
                "Birthday": "1990-01-01",
                "Death": "2020-01-01",
            },
            "@I3@": {
                "ID": "@I3@",
                "Birthday": "2020-01-01",
                "Death": "2010-01-01",
            }
        }
        self.assertEqual(validation(individuals_dict), "ERROR: Birth date 2020-01-01 is after or the same as death date 2010-01-01 for individual @I3@\n")

if __name__ == "__main__":
    unittest.main()
