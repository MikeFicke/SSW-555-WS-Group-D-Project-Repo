# This file contains unit tests for the user story: US02 - Birth before marriage
# SSW-555-WS
# Michael Ficke - Group D

# Acknowledgement: IDE autocomplete was used on certain lines of code.

import unittest
from US02_birth_before_marriage import validate_birth_before_marriage
from io import StringIO
from contextlib import redirect_stdout

# helper function to capture print statements for unit tests
# citation: https://www.google.com/search?q=how+to+capture+print+statements+for+unittesting+in+Python&rlz=1C1CHBF_enUS1023US1023&oq=how+to+capture+print+statements+for+unittesting+in+Python&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQIRgKGKABMgkIAhAhGAoYoAEyCQgDECEYChigATIJCAQQIRgKGKABMgkIBRAhGAoYoAEyCQgGECEYChirAjIHCAcQIRifBdIBCDcwODhqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8


def validation(individuals_dict, families_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_birth_before_marriage(individuals_dict, families_dict)
    output = buffer.getvalue()
    return output


class TestBirthBeforeMarriage(unittest.TestCase):
    def test_birth_before_marriage_1(self):
        """
        Both spouses born well before marriage.
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "1980-01-01",
            },
            "@I2@": {
                "ID": "@I2@",
                "Birthday": "1982-05-15",
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2005-06-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test_birth_before_marriage_2(self):
        """
        Husband born after marriage date.
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "2010-03-01",
            },
            "@I2@": {
                "ID": "@I2@",
                "Birthday": "1985-01-01",
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2005-06-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            }
        }
        # citation: https://www.google.com/search?q=python+when+should+I+use+assert+in+or+asset+equal&rlz=1C1CHBF_enUS1023US1023&oq=python+when+should+I+use+assert+in+or+asset+equal&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQIRigATIHCAIQIRigATIHCAMQIRigAdIBCDcxMzBqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8
        self.assertIn("ERROR", validation(individuals_dict, families_dict))

    def test_birth_before_marriage_3(self):
        """
        Wife born after marriage date
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "1980-01-01",
            },
            "@I2@": {
                "ID": "@I2@",
                "Birthday": "2010-03-01",
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2005-06-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            }
        }
        self.assertIn("ERROR", validation(individuals_dict, families_dict))

    def test_birth_before_marriage_4(self):
        """
        Birthday equals marriage date
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "2005-06-01",
            },
            "@I2@": {
                "ID": "@I2@",
                "Birthday": "1980-01-01",
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2005-06-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            }
        }
        self.assertIn("ERROR", validation(individuals_dict, families_dict))

    def test_birth_before_marriage_5(self):
        """
        Marriage date is "NA"
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "1980-01-01",
            },
            "@I2@": {
                "ID": "@I2@",
                "Birthday": "1982-01-01",
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "NA",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")
    
    def test_birth_before_marriage_6(self):
        """
        Husband ID is "NA"
        """
        individuals_dict = {
            "@I2@": {
                "ID": "@I2@",
                "Birthday": "1982-05-15",
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2005-06-01",
                "Husband ID": "NA",
                "Wife ID": "@I2@"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test_birth_before_marriage_7(self):
        """
        Wife's birthday is "NA"
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "1980-01-01",
            },
            "@I2@": {
                "ID": "@I2@",
                "Birthday": "NA",
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2005-06-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")
    
    def test_birth_before_marriage_8(self):
        """
        Both spouses born after marriage
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "2010-03-01",
            },
            "@I2@": {
                "ID": "@I2@",
                "Birthday": "2012-07-15",
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2005-06-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            }
        }
        # two errors printed here
        error_output = validation(individuals_dict, families_dict)
        self.assertEqual(error_output.count("ERROR"), 2)
        
    def test_birth_before_marriage_9(self):
        """
        Husband ID references a missing individual
        """
        individuals_dict = {  # ID1 is missing on purpose
            "@I2@": {
                "ID": "@I2@",
                "Birthday": "1982-05-15",
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2005-06-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test_birth_before_marriage_10(self):
        """
        Wife's birthday is an empty string
        """
        individuals_dict = { 
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "1980-01-01",
            },
            "@I2@": {
                "ID": "@I2@",
                "Birthday": "",
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Married": "2005-06-01",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@"
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

if __name__ == "__main__":
    unittest.main()
