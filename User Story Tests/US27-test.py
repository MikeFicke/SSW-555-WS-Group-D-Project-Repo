# This file contains unit tests for the user story: US27 - Include individual's current age when listing individuals
# SSW-555-WS
# Group D - Sam Bryan

import unittest
from datetime import datetime, timedelta
from US27_current_age import calculate_current_age


class TestCurrentAge(unittest.TestCase):
    def test_current_age_living_person(self):
        """
        Living person whose birthday has already occurred this year.
        """
        today = datetime.today().date()
        birthday = today.replace(year=today.year - 30) - timedelta(days=10)
        self.assertEqual(calculate_current_age(birthday.strftime("%Y-%m-%d"), "NA"), 30)

    def test_current_age_birthday_not_yet_occurred_this_year(self):
        """
        Living person whose birthday has not yet occurred this year;
        age should not be incremented early.
        """
        today = datetime.today().date()
        birthday = today.replace(year=today.year - 30) + timedelta(days=10)
        self.assertEqual(calculate_current_age(birthday.strftime("%Y-%m-%d"), "NA"), 29)

    def test_current_age_deceased_person(self):
        """
        Deceased person; age should be calculated as of their death date, not today.
        """
        individuals_dict = {
            "Birthday": "1900-01-01",
            "Death": "1975-06-15",
        }
        self.assertEqual(
            calculate_current_age(individuals_dict["Birthday"], individuals_dict["Death"]), 75
        )

    def test_current_age_deceased_before_birthday_in_death_year(self):
        """
        Deceased person who died before their birthday in the year of death.
        """
        self.assertEqual(calculate_current_age("1950-11-01", "2020-10-15"), 69)

    def test_current_age_deceased_on_birthday(self):
        """
        Deceased person who died exactly on their birthday.
        """
        self.assertEqual(calculate_current_age("1950-05-01", "2020-05-01"), 70)

    def test_current_age_birthday_na(self):
        """
        Birthday is "NA"; age cannot be calculated.
        """
        self.assertEqual(calculate_current_age("NA", "NA"), "NA")

    def test_current_age_birthday_none(self):
        """
        Birthday is None; age cannot be calculated.
        """
        self.assertEqual(calculate_current_age(None, "NA"), "NA")

    def test_current_age_birthday_empty_string(self):
        """
        Birthday is an empty string; age cannot be calculated.
        """
        self.assertEqual(calculate_current_age("", "NA"), "NA")

    def test_current_age_death_none(self):
        """
        Death is None (not "NA"); person should be treated as living.
        """
        today = datetime.today().date()
        birthday = today.replace(year=today.year - 40) - timedelta(days=10)
        self.assertEqual(calculate_current_age(birthday.strftime("%Y-%m-%d"), None), 40)

    def test_current_age_newborn(self):
        """
        Person born today should be age 0.
        """
        today = datetime.today().date()
        self.assertEqual(calculate_current_age(today.strftime("%Y-%m-%d"), "NA"), 0)


if __name__ == "__main__":
    unittest.main()
