# This file contains unit tests for the user story: US05 - Marriage before death
# SSW-555-WS
# Group D

import unittest
from US05_marriage_before_death import validate_marriage_before_death
from io import StringIO
from contextlib import redirect_stdout


def validation(individual_dict, family_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_marriage_before_death(individual_dict, family_dict)
    output = buffer.getvalue()
    return output


class TestMarriageBeforeDeath(unittest.TestCase):
    def test_both_spouses_alive(self):
        individuals = {
            "@I1@": {"ID": "@I1@", "Death": "NA"},
            "@I2@": {"ID": "@I2@", "Death": "NA"},
        }
        families = {
            "@F1@": {"ID": "@F1@", "Married": "2000-01-01", "Husband ID": "@I1@", "Wife ID": "@I2@"}
        }
        self.assertEqual(validation(individuals, families), "")

    def test_husband_died_after_marriage(self):
        individuals = {
            "@I1@": {"ID": "@I1@", "Death": "2010-01-01"},
            "@I2@": {"ID": "@I2@", "Death": "NA"},
        }
        families = {
            "@F1@": {"ID": "@F1@", "Married": "2000-01-01", "Husband ID": "@I1@", "Wife ID": "@I2@"}
        }
        self.assertEqual(validation(individuals, families), "")

    def test_husband_died_before_marriage(self):
        individuals = {
            "@I1@": {"ID": "@I1@", "Death": "1990-01-01"},
            "@I2@": {"ID": "@I2@", "Death": "NA"},
        }
        families = {
            "@F1@": {"ID": "@F1@", "Married": "2000-01-01", "Husband ID": "@I1@", "Wife ID": "@I2@"}
        }
        self.assertEqual(
            validation(individuals, families),
            "ERROR: Death date in family @F1@ is before marriage date 2000-01-01 00:00:00\n",
        )

    def test_wife_died_before_marriage(self):
        individuals = {
            "@I1@": {"ID": "@I1@", "Death": "NA"},
            "@I2@": {"ID": "@I2@", "Death": "1990-01-01"},
        }
        families = {
            "@F1@": {"ID": "@F1@", "Married": "2000-01-01", "Husband ID": "@I1@", "Wife ID": "@I2@"}
        }
        self.assertEqual(
            validation(individuals, families),
            "ERROR: Death date in family @F1@ is before marriage date 2000-01-01 00:00:00\n",
        )

    def test_both_spouses_died_before_marriage_is_single_error(self):
        """
        Both spouses' deaths predate the marriage - the check is an OR condition,
        so only one error line should be printed per family, not two.
        """
        individuals = {
            "@I1@": {"ID": "@I1@", "Death": "1990-01-01"},
            "@I2@": {"ID": "@I2@", "Death": "1991-01-01"},
        }
        families = {
            "@F1@": {"ID": "@F1@", "Married": "2000-01-01", "Husband ID": "@I1@", "Wife ID": "@I2@"}
        }
        self.assertEqual(
            validation(individuals, families),
            "ERROR: Death date in family @F1@ is before marriage date 2000-01-01 00:00:00\n",
        )

    def test_marriage_date_na_is_skipped(self):
        individuals = {
            "@I1@": {"ID": "@I1@", "Death": "1990-01-01"},
            "@I2@": {"ID": "@I2@", "Death": "NA"},
        }
        families = {
            "@F1@": {"ID": "@F1@", "Married": "NA", "Husband ID": "@I1@", "Wife ID": "@I2@"}
        }
        self.assertEqual(validation(individuals, families), "")

    def test_missing_spouse_record_does_not_crash(self):
        """
        Husband ID/Wife ID that isn't present in individual_dict should be treated
        like a missing death date rather than raising a KeyError.
        """
        individuals = {}
        families = {
            "@F1@": {"ID": "@F1@", "Married": "2000-01-01", "Husband ID": "@I1@", "Wife ID": "@I2@"}
        }
        self.assertEqual(validation(individuals, families), "")

    def test_death_same_day_as_marriage_is_not_an_error(self):
        individuals = {
            "@I1@": {"ID": "@I1@", "Death": "2000-01-01"},
            "@I2@": {"ID": "@I2@", "Death": "NA"},
        }
        families = {
            "@F1@": {"ID": "@F1@", "Married": "2000-01-01", "Husband ID": "@I1@", "Wife ID": "@I2@"}
        }
        self.assertEqual(validation(individuals, families), "")


if __name__ == "__main__":
    unittest.main()
