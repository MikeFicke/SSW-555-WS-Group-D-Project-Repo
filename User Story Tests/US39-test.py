# Group D
# SSW-555-WS
# Unit test for US39
# Author: Michael Ficke
# Acknowledgement: IDE Auto-complete was used for certain lines of code

import unittest
from US39_list_upcoming_anniversaries import validate_upcoming_anniversaries
from io import StringIO
from contextlib import redirect_stdout
from datetime import datetime, timedelta


def validation(individuals_dict, families_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_upcoming_anniversaries(individuals_dict, families_dict)
    output = buffer.getvalue()
    return output


class TestUpcomingAnniversaries(unittest.TestCase):
    def test_upcoming_anniversaries_1(self):
        """
        Living couple with marriage anniversary in 15 days.
        """
        # citation: https://www.google.com/search?q=how+to+use+timedelta+in+Python+to+calculate+days+apart+between+two+dates%3F
        future_date = datetime.today() + timedelta(days=15)
        # Marriage date in a past year but with month/day 15 days from now
        marriage_date = future_date.replace(year=2000).strftime("%Y-%m-%d")
        individuals = {
            "@I1@": {"ID": "@I1@", "Name": "John /Doe/", "Alive": True, "Birthday": "1975-03-10", "Death": "NA"},
            "@I2@": {"ID": "@I2@", "Name": "Jane /Doe/", "Alive": True, "Birthday": "1978-06-22", "Death": "NA"}
        }
        families = {
            "@F1@": {"ID": "@F1@", "Husband ID": "@I1@", "Wife ID": "@I2@", "Married": marriage_date, "Divorced": "NA", "Children": []}
        }
        self.assertEqual(validation(individuals, families), "US39: Upcoming anniversaries: @F1@\n")

    def test_upcoming_anniversaries_2(self):
        """
        Divorced couple with anniversary in 15 days. Should NOT appear.
        """
        future_date = datetime.today() + timedelta(days=15)
        marriage_date = future_date.replace(year=2000).strftime("%Y-%m-%d")
        divorce_date = (future_date.replace(year=2010)).strftime("%Y-%m-%d")
        individuals = {
            "@I1@": {"ID": "@I1@", "Name": "John /Doe/", "Alive": True, "Birthday": "1975-03-10", "Death": "NA"},
            "@I2@": {"ID": "@I2@", "Name": "Jane /Doe/", "Alive": True, "Birthday": "1978-06-22", "Death": "NA"}
        }
        families = {
            "@F1@": {"ID": "@F1@", "Husband ID": "@I1@", "Wife ID": "@I2@", "Married": marriage_date, "Divorced": divorce_date, "Children": []}
        }
        self.assertEqual(validation(individuals, families), "")

    def test_upcoming_anniversaries_3(self):
        """
        Married couple where wife is deceased. Should NOT appear.
        """
        future_date = datetime.today() + timedelta(days=15)
        marriage_date = future_date.replace(year=2000).strftime("%Y-%m-%d")
        individuals = {
            "@I1@": {"ID": "@I1@", "Name": "John /Doe/", "Alive": True, "Birthday": "1975-03-10", "Death": "NA"},
            "@I2@": {"ID": "@I2@", "Name": "Jane /Doe/", "Alive": False, "Birthday": "1978-06-22", "Death": "2023-01-15"}
        }
        families = {
            "@F1@": {"ID": "@F1@", "Husband ID": "@I1@", "Wife ID": "@I2@", "Married": marriage_date, "Divorced": "NA", "Children": []}
        }
        self.assertEqual(validation(individuals, families), "")

    def test_upcoming_anniversaries_4(self):
        """
        Boundary: anniversary exactly 30 days out (inclusive) and 31 days out (excluded).
        """
        date_30 = datetime.today() + timedelta(days=30)
        date_31 = datetime.today() + timedelta(days=31)
        marriage_30 = date_30.replace(year=1995).strftime("%Y-%m-%d")
        marriage_31 = date_31.replace(year=1998).strftime("%Y-%m-%d")
        individuals = {
            "@I1@": {"ID": "@I1@", "Name": "John /Doe/", "Alive": True, "Birthday": "1970-01-01", "Death": "NA"},
            "@I2@": {"ID": "@I2@", "Name": "Jane /Doe/", "Alive": True, "Birthday": "1972-02-02", "Death": "NA"},
            "@I3@": {"ID": "@I3@", "Name": "Bob /Smith/", "Alive": True, "Birthday": "1973-03-03", "Death": "NA"},
            "@I4@": {"ID": "@I4@", "Name": "Alice /Smith/", "Alive": True, "Birthday": "1974-04-04", "Death": "NA"}
        }
        families = {
            "@F1@": {"ID": "@F1@", "Husband ID": "@I1@", "Wife ID": "@I2@", "Married": marriage_30, "Divorced": "NA", "Children": []},
            "@F2@": {"ID": "@F2@", "Husband ID": "@I3@", "Wife ID": "@I4@", "Married": marriage_31, "Divorced": "NA", "Children": []}
        }
        self.assertEqual(validation(individuals, families), "US39: Upcoming anniversaries: @F1@\n")

    def test_upcoming_anniversaries_5(self):
        """
        No married couples at all. Should produce empty output.
        """
        individuals = {
            "@I1@": {"ID": "@I1@", "Name": "John /Doe/", "Alive": True, "Birthday": "1975-03-10", "Death": "NA"}
        }
        families = {}
        self.assertEqual(validation(individuals, families), "")


if __name__ == '__main__':
    unittest.main()
