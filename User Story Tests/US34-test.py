# This file contains unit tests for the user story: US34 - List large age
# gap married couples (older spouse more than twice the younger spouse's age
# at time of marriage)
# SSW-555-WS
# Group D

import unittest
from US34_large_age_gap_married_couples import validate_large_age_gap_married_couples
from io import StringIO
from contextlib import redirect_stdout


def validation(individuals_dict, families_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_large_age_gap_married_couples(individuals_dict, families_dict)
    output = buffer.getvalue()
    return output


class Test(unittest.TestCase):
    def test_large_age_gap(self):
        """
        Husband is more than twice the wife's age at marriage.
        """
        individuals_dict = {
            "@I1@": {"Birthday": "1950-01-01"},  # husband, 50 at marriage
            "@I2@": {"Birthday": "1980-01-01"},  # wife, 20 at marriage
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2000-01-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
            }
        }
        self.assertEqual(
            validation(individuals_dict, families_dict),
            "US34: Families where the older spouse was more than twice the younger spouse's age at marriage: @F1@\n",
        )

    def test_no_families(self):
        """
        No families on file.
        """
        self.assertEqual(validation({}, {}), "")

    def test_close_age_not_flagged(self):
        """
        Spouses close in age; should not appear.
        """
        individuals_dict = {
            "@I1@": {"Birthday": "1970-01-01"},  # husband, 30 at marriage
            "@I2@": {"Birthday": "1975-01-01"},  # wife, 25 at marriage
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2000-01-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test_exactly_twice_not_flagged(self):
        """
        Boundary: older spouse is exactly twice the younger spouse's age.
        Should NOT be flagged since the rule requires "more than" twice.
        """
        individuals_dict = {
            "@I1@": {"Birthday": "1960-01-01"},  # husband, 40 at marriage
            "@I2@": {"Birthday": "1980-01-01"},  # wife, 20 at marriage
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2000-01-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test_just_over_twice_flagged(self):
        """
        Boundary: older spouse is one year more than twice the younger
        spouse's age. Should be flagged.
        """
        individuals_dict = {
            "@I1@": {"Birthday": "1959-01-01"},  # husband, 41 at marriage
            "@I2@": {"Birthday": "1980-01-01"},  # wife, 20 at marriage
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2000-01-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
            }
        }
        self.assertEqual(
            validation(individuals_dict, families_dict),
            "US34: Families where the older spouse was more than twice the younger spouse's age at marriage: @F1@\n",
        )

    def test_wife_older_flagged(self):
        """
        Wife is the older spouse and more than twice the husband's age.
        """
        individuals_dict = {
            "@I1@": {"Birthday": "1980-01-01"},  # husband, 20 at marriage
            "@I2@": {"Birthday": "1950-01-01"},  # wife, 50 at marriage
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2000-01-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
            }
        }
        self.assertEqual(
            validation(individuals_dict, families_dict),
            "US34: Families where the older spouse was more than twice the younger spouse's age at marriage: @F1@\n",
        )

    def test_no_marriage_date_skipped(self):
        """
        Family with no recorded marriage date should be skipped.
        """
        individuals_dict = {
            "@I1@": {"Birthday": "1950-01-01"},
            "@I2@": {"Birthday": "1980-01-01"},
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "NA",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test_missing_birthday_skipped(self):
        """
        Family where one spouse has no recorded birthday should be skipped.
        """
        individuals_dict = {
            "@I1@": {"Birthday": "NA"},
            "@I2@": {"Birthday": "1980-01-01"},
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2000-01-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test_multiple_families_only_gap_listed(self):
        """
        Multiple families; only the one with a large age gap should be listed.
        """
        individuals_dict = {
            "@I1@": {"Birthday": "1950-01-01"},  # husband, 50 at marriage
            "@I2@": {"Birthday": "1980-01-01"},  # wife, 20 at marriage
            "@I3@": {"Birthday": "1970-01-01"},  # husband, 30 at marriage
            "@I4@": {"Birthday": "1975-01-01"},  # wife, 25 at marriage
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2000-01-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
            },
            "@F2@": {
                "ID": "@F2@",
                "Married": "2000-01-01",
                "Husband ID": "@I3@",
                "Wife ID": "@I4@",
            },
        }
        self.assertEqual(
            validation(individuals_dict, families_dict),
            "US34: Families where the older spouse was more than twice the younger spouse's age at marriage: @F1@\n",
        )


if __name__ == '__main__':
    unittest.main()
