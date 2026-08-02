# This file contains unit tests for the user story: US28 - List siblings in
# families by decreasing age, oldest siblings first
# SSW-555-WS
# Group D - Sam Bryan

import unittest
from US28_siblings_by_age import sort_siblings_by_age


class TestSiblingsByAge(unittest.TestCase):
    def test_siblings_already_oldest_first(self):
        """
        Children already listed oldest first should remain in the same order.
        """
        individuals = {
            "@I1@": {"Birthday": "2000-01-01"},
            "@I2@": {"Birthday": "2005-01-01"},
        }
        self.assertEqual(sort_siblings_by_age(["@I1@", "@I2@"], individuals), ["@I1@", "@I2@"])

    def test_siblings_reversed_order(self):
        """
        Children listed youngest first should be reordered oldest first.
        """
        individuals = {
            "@I1@": {"Birthday": "2005-01-01"},
            "@I2@": {"Birthday": "2000-01-01"},
        }
        self.assertEqual(sort_siblings_by_age(["@I1@", "@I2@"], individuals), ["@I2@", "@I1@"])

    def test_siblings_multiple_out_of_order(self):
        """
        Several siblings listed out of order should be sorted oldest to youngest.
        """
        individuals = {
            "@I1@": {"Birthday": "2010-06-15"},
            "@I2@": {"Birthday": "1998-03-01"},
            "@I3@": {"Birthday": "2004-11-20"},
        }
        self.assertEqual(
            sort_siblings_by_age(["@I1@", "@I2@", "@I3@"], individuals),
            ["@I2@", "@I3@", "@I1@"],
        )

    def test_siblings_multiple_birth_same_birthday(self):
        """
        Siblings sharing the exact same birthday (e.g. twins) keep their
        original relative order (stable sort).
        """
        individuals = {
            "@I1@": {"Birthday": "2010-06-15"},
            "@I2@": {"Birthday": "2010-06-15"},
        }
        self.assertEqual(sort_siblings_by_age(["@I1@", "@I2@"], individuals), ["@I1@", "@I2@"])

    def test_sibling_unknown_birthday_pushed_last(self):
        """
        A sibling with an unknown ("NA") birthday should be placed after
        siblings with known birthdays, regardless of listed order.
        """
        individuals = {
            "@I1@": {"Birthday": "NA"},
            "@I2@": {"Birthday": "2000-01-01"},
        }
        self.assertEqual(sort_siblings_by_age(["@I1@", "@I2@"], individuals), ["@I2@", "@I1@"])

    def test_all_siblings_unknown_birthday(self):
        """
        When no siblings have a known birthday, original order is preserved.
        """
        individuals = {
            "@I1@": {"Birthday": "NA"},
            "@I2@": {"Birthday": "NA"},
        }
        self.assertEqual(sort_siblings_by_age(["@I1@", "@I2@"], individuals), ["@I1@", "@I2@"])

    def test_no_children(self):
        """
        A family with no children returns an empty list.
        """
        individuals = {}
        self.assertEqual(sort_siblings_by_age([], individuals), [])

    def test_single_child(self):
        """
        A family with a single child returns that child unchanged.
        """
        individuals = {"@I1@": {"Birthday": "2000-01-01"}}
        self.assertEqual(sort_siblings_by_age(["@I1@"], individuals), ["@I1@"])


if __name__ == "__main__":
    unittest.main()
