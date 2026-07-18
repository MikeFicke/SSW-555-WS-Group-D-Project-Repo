# Group D - Michael Ficke
# SSW-555-WS
# Unit test file for US22

# Acknowledgement: IDE auto-complete was used for certain lines of code

import unittest
from US22_unique_ids import validate_unique_ids
from io import StringIO
from contextlib import redirect_stdout



def validation(file_contents):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_unique_ids(file_contents)
    output = buffer.getvalue()
    return output


class TestUniqueIDs(unittest.TestCase):
    def test_unique_ids_1(self):
        """
        Valid.  All ids are unique.
        """
        file_contents = [
            "0 @I1@ INDI",
            "1 NAME John /Smith/",
            "0 @I2@ INDI",
            "1 NAME Jane /Doe/",
            "0 @F1@ FAM",
            "1 HUSB @I1@",
            "1 WIFE @I2@"
        ]

        self.assertEqual(validation(file_contents), "")

    def test_unique_ids_2(self):
        """
        Invalid.  Duplicate individual ID.
        """
        file_contents = [
            "0 @I1@ INDI",
            "1 NAME John /Smith/",
            "0 @I1@ INDI",
            "1 NAME Different /Person/",
            "0 @F1@ FAM"
        ]

        self.assertEqual(validation(file_contents), "ERROR: Individual ID @I1@ appears more than once in the GEDCOM file.\n")

    def test_unique_ids_3(self):
        """
        Invalid.  Duplicate family ID.
        """
        file_contents = [
            "0 @I1@ INDI",
            "0 @I2@ INDI",
            "0 @F1@ FAM",
            "1 HUSB @I1@",
            "0 @F1@ FAM",
            "1 HUSB @I2@"
        ]

        self.assertEqual(validation(file_contents), "ERROR: Family ID @F1@ appears more than once in the GEDCOM file.\n")

    def test_unique_ids_4(self):
        """
        Invalid.  Duplicate individual ID and family ID.
        """
        file_contents = [
            "0 @I1@ INDI",
            "0 @I1@ INDI",
            "0 @F1@ FAM",
            "0 @F1@ FAM"
        ]

        self.assertEqual(validation(file_contents), "ERROR: Individual ID @I1@ appears more than once in the GEDCOM file.\nERROR: Family ID @F1@ appears more than once in the GEDCOM file.\n")

    def test_unique_ids_5(self):
        """
        Valid Edge case.  The file contents are empty.
        """
        file_contents = []
        
        self.assertEqual(validation(file_contents), "")
        

if __name__ == "__main__":
    unittest.main()
