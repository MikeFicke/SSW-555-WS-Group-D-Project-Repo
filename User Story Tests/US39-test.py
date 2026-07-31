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


def validation(individuals_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_upcoming_anniversaries(individuals_dict)
    output = buffer.getvalue()
    return output


class TestUpcomingAnniversaries(unittest.TestCase):
    def test_upcoming_anniversaries_1(self):
        """
        Living couple with marriag anniversary in 15 days.
        """
        today = datetime.today()
        anniversary_date = today + timedelta(days=15)
        individuals = {
            "I01": {"Name": "John", "Alive": True, "Birthday": "NA"},
            "I02": {"Name": "Jane", "Alive": True, "Birthday": "NA"}
        }
        families = {
            "F01": {"Husband ID": "I01", "Wife ID": "I02", "Married": anniversary_date.strftime("%d-%b-%Y"), "Divorced": "NA"}
        }
        self.assertEqual(validation(individuals), f"US39: Upcoming Anniversaries\n{individuals['I01']['Name']} and {individuals['I02']['Name']} will be celebrating their anniversary on {anniversary_date.strftime('%d-%b-%Y')}\n")

    def test_upcoming_anniversaries_2(self):
        """
        Divorced couple with anniversary in 15 days.
        """
        today = datetime.today()
        anniversary_date = today + timedelta(days=15)
        individuals = {
            "I01": {"Name": "John", "Alive": True, "Birthday": "NA"},
            "I02": {"Name": "Jane", "Alive": True, "Birthday": "NA"}
        }
        families = {
            "F01": {"Husband ID": "I01", "Wife ID": "I02", "Married": anniversary_date.strftime("%d-%b-%Y"), "Divorced": "NA"}
        }
        self.assertEqual(validation(individuals), f"US39: Upcoming Anniversaries\n{individuals['I01']['Name']} and {individuals['I02']['Name']} will be celebrating their anniversary on {anniversary_date.strftime('%d-%b-%Y')}\n")

    def test_upcoming_anniversaries_3(self):
        """
        Married couple where either the husband or wife is deceased.
        """
        today = datetime.today()
        anniversary_date = today + timedelta(days=15)
        individuals = {
            "I01": {"Name": "John", "Alive": True, "Birthday": "NA"},
            "I02": {"Name": "Jane", "Alive": False, "Birthday": "NA"}
        }
        families = {
            "F01": {"Husband ID": "I01", "Wife ID": "I02", "Married": anniversary_date.strftime("%d-%b-%Y"), "Divorced": "NA"}
        }
        self.assertEqual(validation(individuals), f"US39: Upcoming Anniversaries\n{individuals['I01']['Name']} and {individuals['I02']['Name']} will be celebrating their anniversary on {anniversary_date.strftime('%d-%b-%Y')}\n")

    def test_upcoming_anniversaries_4(self):
        """
        Current date is in December, but the anniversary occurs next year in January.
        """
        today = datetime.today()
        anniversary_date = today + timedelta(days=15)
        individuals = {
            "I01": {"Name": "John", "Alive": True, "Birthday": "NA"},
            "I02": {"Name": "Jane", "Alive": True, "Birthday": "NA"}
        }
        families = {
            "F01": {"Husband ID": "I01", "Wife ID": "I02", "Married": anniversary_date.strftime("%d-%b-%Y"), "Divorced": "NA"}
        }
        self.assertEqual(validation(individuals), f"US39: Upcoming Anniversaries\n{individuals['I01']['Name']} and {individuals['I02']['Name']} will be celebrating their anniversary on {anniversary_date.strftime('%d-%b-%Y')}\n")

    def test_upcoming_anniversaries_5(self):
        """
        Edge cases: anniversary today, in 30 days,and in 31 days.
        """
        today = datetime.today()
        anniversary_date = today + timedelta(days=15)
        individuals = {
            "I01": {"Name": "John", "Alive": True, "Birthday": "NA"},
            "I02": {"Name": "Jane", "Alive": True, "Birthday": "NA"}
        }
        families = {
            "F01": {"Husband ID": "I01", "Wife ID": "I02", "Married": anniversary_date.strftime("%d-%b-%Y"), "Divorced": "NA"}
        }
        self.assertEqual(validation(individuals), f"US39: Upcoming Anniversaries\n{individuals['I01']['Name']} and {individuals['I02']['Name']} will be celebrating their anniversary on {anniversary_date.strftime('%d-%b-%Y')}\n")

if __name__ == '__main__':
    unittest.main()
