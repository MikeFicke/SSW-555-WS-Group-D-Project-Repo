# This file contains unit tests for the user story: US37 - List living spouses
# and descendants of individuals who died within the last 30 days
# SSW-555-WS
# Group D

import unittest
from datetime import datetime, timedelta
from US37_list_living_relatives_of_recent_deaths import validate_living_relatives_of_recent_deaths
from io import StringIO
from contextlib import redirect_stdout


def validation(individuals_dict, families_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_living_relatives_of_recent_deaths(individuals_dict, families_dict)
    output = buffer.getvalue()
    return output


class Test(unittest.TestCase):
    def test_living_spouse_of_recent_death(self):
        """
        Living spouse of someone who died 10 days ago should be listed.
        """
        recent_death = (datetime.today() - timedelta(days=10)).strftime("%Y-%m-%d")
        individuals_dict = {
            "@I1@": {"ID": "@I1@", "Death": recent_death, "Alive": False, "Spouse": ["@F1@"]},
            "@I2@": {"ID": "@I2@", "Death": "NA", "Alive": True, "Spouse": ["@F1@"]},
        }
        families_dict = {
            "@F1@": {"ID": "@F1@", "Husband ID": "@I1@", "Wife ID": "@I2@", "Children": []},
        }
        self.assertEqual(
            validation(individuals_dict, families_dict),
            "US37: Living spouses and descendants of recently deceased individuals: @I2@\n",
        )

    def test_living_child_of_recent_death(self):
        """
        Living child of someone who died 5 days ago should be listed.
        """
        recent_death = (datetime.today() - timedelta(days=5)).strftime("%Y-%m-%d")
        individuals_dict = {
            "@I1@": {"ID": "@I1@", "Death": recent_death, "Alive": False, "Spouse": ["@F1@"]},
            "@I2@": {"ID": "@I2@", "Death": "NA", "Alive": True, "Spouse": ["@F1@"]},
            "@I3@": {"ID": "@I3@", "Death": "NA", "Alive": True, "Spouse": []},
        }
        families_dict = {
            "@F1@": {"ID": "@F1@", "Husband ID": "@I1@", "Wife ID": "@I2@", "Children": ["@I3@"]},
        }
        self.assertEqual(
            validation(individuals_dict, families_dict),
            "US37: Living spouses and descendants of recently deceased individuals: @I2@, @I3@\n",
        )

    def test_living_grandchild_of_recent_death(self):
        """
        Living grandchild (descendant two generations down) should also be listed.
        """
        recent_death = (datetime.today() - timedelta(days=5)).strftime("%Y-%m-%d")
        individuals_dict = {
            "@I1@": {"ID": "@I1@", "Death": recent_death, "Alive": False, "Spouse": ["@F1@"]},
            "@I2@": {"ID": "@I2@", "Death": "NA", "Alive": True, "Spouse": ["@F1@"]},
            "@I3@": {"ID": "@I3@", "Death": "NA", "Alive": True, "Spouse": ["@F2@"]},
            "@I4@": {"ID": "@I4@", "Death": "NA", "Alive": True, "Spouse": ["@F2@"]},
            "@I5@": {"ID": "@I5@", "Death": "NA", "Alive": True, "Spouse": []},
        }
        families_dict = {
            "@F1@": {"ID": "@F1@", "Husband ID": "@I1@", "Wife ID": "@I2@", "Children": ["@I3@"]},
            "@F2@": {"ID": "@F2@", "Husband ID": "@I3@", "Wife ID": "@I4@", "Children": ["@I5@"]},
        }
        self.assertEqual(
            validation(individuals_dict, families_dict),
            "US37: Living spouses and descendants of recently deceased individuals: @I2@, @I3@, @I5@\n",
        )

    def test_deceased_relative_excluded(self):
        """
        A deceased descendant should not appear, even though they're related.
        """
        recent_death = (datetime.today() - timedelta(days=5)).strftime("%Y-%m-%d")
        individuals_dict = {
            "@I1@": {"ID": "@I1@", "Death": recent_death, "Alive": False, "Spouse": ["@F1@"]},
            "@I2@": {"ID": "@I2@", "Death": "NA", "Alive": True, "Spouse": ["@F1@"]},
            "@I3@": {"ID": "@I3@", "Death": "2010-01-01", "Alive": False, "Spouse": []},
        }
        families_dict = {
            "@F1@": {"ID": "@F1@", "Husband ID": "@I1@", "Wife ID": "@I2@", "Children": ["@I3@"]},
        }
        self.assertEqual(
            validation(individuals_dict, families_dict),
            "US37: Living spouses and descendants of recently deceased individuals: @I2@\n",
        )

    def test_death_outside_30_day_window_excluded(self):
        """
        A death from more than 30 days ago should not trigger any listing.
        """
        old_death = (datetime.today() - timedelta(days=45)).strftime("%Y-%m-%d")
        individuals_dict = {
            "@I1@": {"ID": "@I1@", "Death": old_death, "Alive": False, "Spouse": ["@F1@"]},
            "@I2@": {"ID": "@I2@", "Death": "NA", "Alive": True, "Spouse": ["@F1@"]},
        }
        families_dict = {
            "@F1@": {"ID": "@F1@", "Husband ID": "@I1@", "Wife ID": "@I2@", "Children": []},
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test_no_deaths(self):
        """
        No deceased individuals at all - nothing should be listed.
        """
        individuals_dict = {
            "@I1@": {"ID": "@I1@", "Death": "NA", "Alive": True, "Spouse": []},
        }
        families_dict = {}
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test_no_living_relatives(self):
        """
        Recently deceased individual has no living spouse or descendants.
        """
        recent_death = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
        individuals_dict = {
            "@I1@": {"ID": "@I1@", "Death": recent_death, "Alive": False, "Spouse": []},
        }
        families_dict = {}
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test_deduplicates_relative_shared_by_two_decedents(self):
        """
        A living relative connected to two recently-deceased individuals
        should only be listed once.
        """
        recent_death = (datetime.today() - timedelta(days=2)).strftime("%Y-%m-%d")
        individuals_dict = {
            "@I1@": {"ID": "@I1@", "Death": recent_death, "Alive": False, "Spouse": ["@F1@"]},
            "@I2@": {"ID": "@I2@", "Death": recent_death, "Alive": False, "Spouse": ["@F1@"]},
            "@I3@": {"ID": "@I3@", "Death": "NA", "Alive": True, "Spouse": []},
        }
        families_dict = {
            "@F1@": {"ID": "@F1@", "Husband ID": "@I1@", "Wife ID": "@I2@", "Children": ["@I3@"]},
        }
        self.assertEqual(
            validation(individuals_dict, families_dict),
            "US37: Living spouses and descendants of recently deceased individuals: @I3@\n",
        )


if __name__ == '__main__':
    unittest.main()
