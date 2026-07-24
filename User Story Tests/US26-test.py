# Group D
# SSW-555-WS
# Unit test for US26
# Author: Michael Ficke
# Acknowledgement: IDE Auto-complete was used for certain lines of code

import unittest
from US26_corresponding_entries import validate_corresponding_entries
from io import StringIO
from contextlib import redirect_stdout



def validation(individuals_dict, families_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_corresponding_entries(individuals_dict, families_dict)
    output = buffer.getvalue()
    return output


class TestCorrespondingEntries(unittest.TestCase):
    def test_corresponding_entries_1(self):
        """
        Valid.  All individuals and families are fully consistent.
        """
        individuals_dict = {
            "@I1@": {"ID": "@I1@", "Name": "John /Doe/", "Birthday": "2000-01-01", "Child": "NA", "Spouse": ["@F1@"]},
            "@I2@": {"ID": "@I2@", "Name": "Jane /Doe/", "Birthday": "2002-05-15", "Child": "NA", "Spouse": ["@F1@"]},
            "@I3@": {"ID": "@I3@", "Name": "Tom /Doe/", "Birthday": "2005-03-10", "Child": "@F1@", "Spouse": []},
            "@I4@": {"ID": "@I4@", "Name": "Sara /Doe/", "Birthday": "2007-08-20", "Child": "@F1@", "Spouse": []},
        }
        families_dict = {
            "@F1@": {"ID": "@F1@", "Husband ID": "@I1@", "Wife ID": "@I2@", "Children": ["@I3@", "@I4@"]},
        }

        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test_corresponding_entries_2(self):
        """
        Invalid.  Individual says Child = @F1@, but family @F1@ does not list them in Children.
        """
        individuals_dict = {
            "@I1@": {"ID": "@I1@", "Name": "John /Doe/", "Birthday": "2000-01-01", "Child": "NA", "Spouse": ["@F1@"]},
            "@I2@": {"ID": "@I2@", "Name": "Jane /Doe/", "Birthday": "2002-05-15", "Child": "NA", "Spouse": ["@F1@"]},
            "@I3@": {"ID": "@I3@", "Name": "Tom /Doe/", "Birthday": "2005-03-10", "Child": "@F1@", "Spouse": []},
        }
        families_dict = {
            "@F1@": {"ID": "@F1@", "Husband ID": "@I1@", "Wife ID": "@I2@", "Children": []},
        }

        self.assertNotEqual(validation(individuals_dict, families_dict), "")

    def test_corresponding_entries_3(self):
        """
        Invalid.  Individual says Spouse = [@F1@], but family @F1@ does not list them as husband or wife.
        """
        individuals_dict = {
            "@I1@": {"ID": "@I1@", "Name": "John /Doe/", "Birthday": "2000-01-01", "Child": "NA", "Spouse": ["@F1@"]},
            "@I2@": {"ID": "@I2@", "Name": "Jane /Doe/", "Birthday": "2002-05-15", "Child": "NA", "Spouse": ["@F1@"]},
            "@I3@": {"ID": "@I3@", "Name": "Tom /Doe/", "Birthday": "2005-03-10", "Child": "NA", "Spouse": ["@F1@"]},
        }
        families_dict = {
            "@F1@": {"ID": "@F1@", "Husband ID": "@I1@", "Wife ID": "@I2@", "Children": []},
        }

        self.assertNotEqual(validation(individuals_dict, families_dict), "")

    def test_corresponding_entries_4(self):
        """
        Invalid.  Family lists a child @I3@, but that individual's Child field does not point back.
        """
        individuals_dict = {
            "@I1@": {"ID": "@I1@", "Name": "John /Doe/", "Birthday": "2000-01-01", "Child": "NA", "Spouse": ["@F1@"]},
            "@I2@": {"ID": "@I2@", "Name": "Jane /Doe/", "Birthday": "2002-05-15", "Child": "NA", "Spouse": ["@F1@"]},
            "@I3@": {"ID": "@I3@", "Name": "Tom /Doe/", "Birthday": "2005-03-10", "Child": "NA", "Spouse": []},
        }
        families_dict = {
            "@F1@": {"ID": "@F1@", "Husband ID": "@I1@", "Wife ID": "@I2@", "Children": ["@I3@"]},
        }

        self.assertNotEqual(validation(individuals_dict, families_dict), "")

    def test_corresponding_entries_5(self):
        """
        Invalid.  Family lists @I1@ as husband, but @I1@'s Spouse list does not reference that family.
        """
        individuals_dict = {
            "@I1@": {"ID": "@I1@", "Name": "John /Doe/", "Birthday": "2000-01-01", "Child": "NA", "Spouse": []},
            "@I2@": {"ID": "@I2@", "Name": "Jane /Doe/", "Birthday": "2002-05-15", "Child": "NA", "Spouse": ["@F1@"]},
        }
        families_dict = {
            "@F1@": {"ID": "@F1@", "Husband ID": "@I1@", "Wife ID": "@I2@", "Children": []},
        }

        self.assertNotEqual(validation(individuals_dict, families_dict), "")

    def test_corresponding_entries_6(self):
        """
        Invalid.  Multiple errors: husband not referencing family, and child not referencing family.
        """
        individuals_dict = {
            "@I1@": {"ID": "@I1@", "Name": "John /Doe/", "Birthday": "2000-01-01", "Child": "NA", "Spouse": []},
            "@I2@": {"ID": "@I2@", "Name": "Jane /Doe/", "Birthday": "2002-05-15", "Child": "NA", "Spouse": ["@F1@"]},
            "@I3@": {"ID": "@I3@", "Name": "Tom /Doe/", "Birthday": "2005-03-10", "Child": "NA", "Spouse": []},
        }
        families_dict = {
            "@F1@": {"ID": "@F1@", "Husband ID": "@I1@", "Wife ID": "@I2@", "Children": ["@I3@"]},
        }

        self.assertNotEqual(validation(individuals_dict, families_dict), "")

if __name__ == "__main__":
    unittest.main()
