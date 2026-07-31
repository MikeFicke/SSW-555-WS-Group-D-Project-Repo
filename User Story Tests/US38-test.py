# Group D
# SSW-555-WS
# Unit test for US38
# Author: Michael Ficke
# Acknowledgement: IDE Auto-complete was used for certain lines of code

import unittest
from US38_list_upcoming_birthdays import validate_forthcoming_birthdays
from io import StringIO
from contextlib import redirect_stdout
from datetime import datetime, timedelta


def validation(individuals_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_forthcoming_birthdays(individuals_dict)
    output = buffer.getvalue()
    return output


class TestForthcomingBirthdays(unittest.TestCase):
    def test_forthcoming_birthdays_1(self):
        """
        One living individual with a birthday in 10 days.
        Uses a past birth year with the target month/day falling in the upcoming window.
        """
        # citation: https://www.google.com/search?q=how+to+use+timedelta+in+Python+to+calculate+days+apart+between+two+dates%3F
        future_date = datetime.today() + timedelta(days=10)
        # Build a birthday in a past year but with the same month/day as 10 days from now
        birthday = future_date.replace(year=1990).strftime("%Y-%m-%d")
        individuals = {
            "@I1@": {
                "ID": "@I1@",
                "Name": "John /Doe/",
                "Birthday": birthday,
                "Death": "NA",
                "Alive": True,
            }
        }

        self.assertEqual(validation(individuals), "US38: Upcoming birthdays: @I1@\n")

    def test_forthcoming_birthdays_2(self):
        """
        Living individual with a birthday that occurred 10 days ago. Should not appear.
        """
        past_date = datetime.today() - timedelta(days=10)
        birthday = past_date.replace(year=1990).strftime("%Y-%m-%d")
        individuals = {
            "@I1@": {
                "ID": "@I1@",
                "Name": "John /Doe/",
                "Birthday": birthday,
                "Death": "NA",
                "Alive": True,
            }
        }

        self.assertEqual(validation(individuals), "")

    def test_forthcoming_birthdays_3(self):
        """
        Deceased individual with a birthday in 10 days. Should not appear.
        """
        future_date = datetime.today() + timedelta(days=10)
        birthday = future_date.replace(year=1990).strftime("%Y-%m-%d")
        individuals = {
            "@I1@": {
                "ID": "@I1@",
                "Name": "John /Doe/",
                "Birthday": birthday,
                "Death": "2020-06-15",
                "Alive": False,
            }
        }

        self.assertEqual(validation(individuals), "")

    def test_forthcoming_birthdays_4(self):
        """
        Boundary: birthday exactly 30 days from now (inclusive) and birthday 31 days out (excluded).
        """
        date_30 = datetime.today() + timedelta(days=30)
        date_31 = datetime.today() + timedelta(days=31)
        bday_30 = date_30.replace(year=1985).strftime("%Y-%m-%d")
        bday_31 = date_31.replace(year=1985).strftime("%Y-%m-%d")
        individuals = {
            "@I1@": {
                "ID": "@I1@",
                "Name": "Jane /Doe/",
                "Birthday": bday_30,
                "Death": "NA",
                "Alive": True,
            },
            "@I2@": {
                "ID": "@I2@",
                "Name": "Bob /Doe/",
                "Birthday": bday_31,
                "Death": "NA",
                "Alive": True,
            }
        }

        self.assertEqual(validation(individuals), "US38: Upcoming birthdays: @I1@\n")

    def test_forthcoming_birthdays_5(self):
        """
        Edge case: birthday is today (0 days). Should be included.
        Also includes a second individual with birthday in 15 days.
        """
        today_bday = datetime.today().replace(year=1975).strftime("%Y-%m-%d")
        future_bday = (datetime.today() + timedelta(days=15)).replace(year=1980).strftime("%Y-%m-%d")
        individuals = {
            "@I1@": {
                "ID": "@I1@",
                "Name": "John /Doe/",
                "Birthday": today_bday,
                "Death": "NA",
                "Alive": True,
            },
            "@I2@": {
                "ID": "@I2@",
                "Name": "Jane /Doe/",
                "Birthday": future_bday,
                "Death": "NA",
                "Alive": True,
            }
        }

        self.assertEqual(validation(individuals), "US38: Upcoming birthdays: @I1@, @I2@\n")


if __name__ == '__main__':
    unittest.main()
