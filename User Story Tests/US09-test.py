# This file contains unit tests for the user story: US09 - Birth before parent death
# SSW-555-WS
# Sam Bryan - Group D

# Acknowledgement: IDE autocomplete was used on certain lines of code.

import unittest
from US09_birth_before_parent_death import validate_birth_before_parent_death
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
        validate_birth_before_parent_death(individuals_dict, families_dict)
    output = buffer.getvalue()
    return output


class TestBirthBeforeParentDeath(unittest.TestCase):
    def test_birth_before_parent_death_1(self):
        """
        Child born before both parents' deaths.
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Death": "2020-01-01",
            },
            "@I2@": {
                "ID": "@I2@",
                "Death": "2019-01-01",
            },
            "@I3@": {
                "ID": "@I3@",
                "Birthday": "2001-01-01",
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": ["@I3@"]
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test_birth_before_parent_death_2(self):
        """
        Child born after the death of their mother.
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Death": "NA",
            },
            "@I2@": {
                "ID": "@I2@",
                "Death": "2000-01-01",
            },
            "@I3@": {
                "ID": "@I3@",
                "Birthday": "2001-01-01",
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": ["@I3@"]
            }
        }
        self.assertEqual(
            validation(individuals_dict, families_dict),
            "ERROR: Child @I3@ was born after the death of their mother @I2@ in family @F1@\n"
        )

    def test_birth_before_parent_death_3(self):
        """
        Child born more than 9 months after the death of their father.
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Death": "2000-01-01",
            },
            "@I2@": {
                "ID": "@I2@",
                "Death": "NA",
            },
            "@I3@": {
                "ID": "@I3@",
                "Birthday": "2001-06-01",
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": ["@I3@"]
            }
        }
        self.assertEqual(
            validation(individuals_dict, families_dict),
            "ERROR: Child @I3@ was born more than 9 months after the death of their father @I1@ in family @F1@\n"
        )

    def test_birth_before_parent_death_4(self):
        """
        Child born within 9 months of the death of their father.
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Death": "2000-01-01",
            },
            "@I2@": {
                "ID": "@I2@",
                "Death": "NA",
            },
            "@I3@": {
                "ID": "@I3@",
                "Birthday": "2000-06-01",
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": ["@I3@"]
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test_birth_before_parent_death_5(self):
        """
        Both parents are living (Death is "NA")
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Death": "NA",
            },
            "@I2@": {
                "ID": "@I2@",
                "Death": "NA",
            },
            "@I3@": {
                "ID": "@I3@",
                "Birthday": "2001-01-01",
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": ["@I3@"]
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

    def test_birth_before_parent_death_6(self):
        """
        Family has no children.
        """
        individuals_dict = {
            "@I1@": {
                "ID": "@I1@",
                "Death": "2000-01-01",
            },
            "@I2@": {
                "ID": "@I2@",
                "Death": "NA",
            }
        }
        families_dict = {
            "@F1@": {
                "ID": "@F1@",
                "Husband ID": "@I1@",
                "Wife ID": "@I2@",
                "Children": []
            }
        }
        self.assertEqual(validation(individuals_dict, families_dict), "")

if __name__ == "__main__":
    unittest.main()
