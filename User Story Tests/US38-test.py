# Group D
# SSW-555-WS
# Unit test for US38
# Author: Michael Ficke
# Acknowledgement: IDE Auto-complete was used for certain lines of code

import unittest
from User_Stories.US38_list_upcoming_birthdays import validate_forthcoming_birthdays
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
        One individual with a birthday in 10 days.
        """
        individuals = {
            "I01": {
                "Name": "John Doe",
                "Birthday": (datetime.today() + timedelta(days=10)).strftime("%Y-%m-%d"),
                "Alive": True,
            }
        }

        self.assertEqual(validation(individuals), "Forthcoming Birthdays (Next 30 Days):\nJohn Doe: {birthday}\n")

    def test_forthcoming_birthdays_2(self):
        """
        Individual with a birtthday tha occurred 10 days ago.
        """
        individuals = {
            "I01": {
                "Name": "John Doe",
                "Birthday": (datetime.today() - timedelta(days=10)).strftime("%Y-%m-%d"),
                "Alive": True,
            }
        }

        self.assertEqual(validation(individuals), "Forthcoming Birthdays (Next 30 Days):\nNone\n")

    def test_forthcoming_birthdays_3(self):
        """
        Deceased individual with a birthday in 10 days.
        """
        individuals = {
            "I01": {
                "Name": "John Doe",
                "Birthday": (datetime.today() + timedelta(days=10)).strftime("%Y-%m-%d"),
                "Alive": False,
            }
        }

        self.assertEqual(validation(individuals), "Forthcoming Birthdays (Next 30 Days):\nNone\n")

    def test_forthcoming_birthdays_4(self):
        """
        The current date is late December, with a birthday in January of next year.
        """
        individuals = {
            "I01": {
                "Name": "John Doe",
                "Birthday": (datetime.today() + timedelta(days=31)).strftime("%Y-%m-%d"),
                "Alive": True,
            }
        }

        self.assertEqual(validation(individuals), "Forthcoming Birthdays (Next 30 Days):\nNone\n")

    def test_forthcoming_birthdays_5(self):
        """
        Edge cases: individuals with a birthday today, in 30 days, and in 31 days.
        """
        individuals = {
            "I01": {
                "Name": "John Doe",
                "Birthday": (datetime.today()).strftime("%Y-%m-%d"),
                "Alive": True,
            },
            "I02": {
                "Name": "Jane Doe",
                "Birthday": (datetime.today() + timedelta(days=30)).strftime("%Y-%m-%d"),
                "Alive": True,
            },
            "I03": {
                "Name": "Bob Doe",
                "Birthday": (datetime.today() + timedelta(days=31)).strftime("%Y-%m-%d"),
                "Alive": True,
            }
        }

        self.assertEqual(validation(individuals), "Forthcoming Birthdays (Next 30 Days):\nJohn Doe: {birthday}\nJane Doe: {birthday}\n")
