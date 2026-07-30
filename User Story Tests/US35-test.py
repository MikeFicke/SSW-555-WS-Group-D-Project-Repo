# Group D
# SSW-555-WS
# Unit test for US35
# Author: Michael Ficke
# Acknowledgement: IDE Auto-complete was used for certain lines of code

import unittest
from US35_list_recent_births import validate_recent_births
from io import StringIO
from contextlib import redirect_stdout
from datetime import datetime, timedelta


def validation(individuals_dict):
    """
    Capture the output string of the function we are unit testing for verification.
    """
    buffer = StringIO()
    with redirect_stdout(buffer):
        validate_recent_births(individuals_dict)
    output = buffer.getvalue()
    return output


class TestRecentBirths(unittest.TestCase):
    def test_recent_births_1(self):
        """
        Output demonstrating one user that has a birthday within the last 30 days
        """
        # citation: https://www.google.com/search?q=how+to+use+timedelta+in+Python+to+calculate+days+apart+between+two+dates%3F&sca_esv=2c404eaf43af4804&rlz=1C1CHBF_enUS1023US1023&sxsrf=APpeQnveG1_Kw5GkSbJ4PYp62_0tbXNXtA%3A1785451955859&udm=50&source=chrome.ob&fbs=ABfTbFVyMZGZf1hfvX9uKjN_-G8cxpBkeIeqYwoCbfNVc4vKE4f6ZJqUzPbNrAmWktdS6nG82-1N4OXO01WJkKgjHAhRM6ScTiHqzjAJLebouTbGuy4vj0NVx0QN6KObJnDwqlpzpbc9KkDPc7uS48iQTdKnZOML_UnFPDHKx-qlCXk-s-WbZzNzLu_x64IXm_u1PE0MKsnFqPNm-zKHHhuyMRiRFjpoag&aep=1&ntc=1&cs=1&sa=X&ved=2ahUKEwihnt7svvuVAxVqhYkEHeh3OWgQ2J8OegQIEhAD&biw=1536&bih=825.2000122070312&dpr=2.5&sourceid=chrome&ccb=1&hl=en-US&atvm=2&mstk=AUtExfCKs6eWUYC4fA8_v3KmrVgJTo22N4U1CBajSzLTAZgQZ8UT0M1Hqmpaawe-gjbZKbqZ9SnBwnv-AnVpOJUkqQr4uA6Lte6F_MRplHmbA_vlPUEajXAHZo7IazukSKQbn5Uj5k8orkUwdUJh76L4Jn7laAYDHj_tlqE&csuir=1&mtid=ztVras_THr-x5NoPmNSzqQQ
        five_days_ago = (datetime.today() - timedelta(days=5)).strftime("%Y-%m-%d")
        individuals = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": five_days_ago,  # We have to dynamically calculate the dates to compensate that every time this file is run, the date could be different, and therefore, the data too.
                "Death": "NA",
                "Alive": True
            }
        }
        
        self.assertEqual(validation(individuals), "US35: Recent births: @I1@\n")
    
    def test_recent_births_2(self):
        """
        Output is blank; no one was born within 30 days.
        """
        individuals = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": "1990-01-15",
                "Death": "NA",
                "Alive": True
            },
            "@I2@": {
                "ID": "@I2@",
                "Birthday": "1985-06-20",
                "Death": "NA",
                "Alive": True
            }
        }
        
        self.assertEqual(validation(individuals), "")

    def test_recent_births_3(self):
        """
        Output demonstrating two users that have birthdays within the last 30 days
        """
        ten_days_ago = (datetime.today() - timedelta(days=10)).strftime("%Y-%m-%d")
        twenty_days_ago = (datetime.today() - timedelta(days=20)).strftime("%Y-%m-%d")
        individuals = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": ten_days_ago,
                "Death": "NA",
                "Alive": True
            },
            "@I2@": {
                "ID": "@I2@",
                "Birthday": twenty_days_ago,
                "Death": "NA",
                "Alive": True
            },
            "@I3@": {
                "ID": "@I3@",
                "Birthday": "1970-03-10",
                "Death": "NA",
                "Alive": True
            }
        }
        
        self.assertEqual(validation(individuals), "US35: Recent births: @I1@, @I2@\n")

    def test_recent_births_4(self):
        """
        Output demonstrating an edge case where a birthday is exactly 30 days from today.
        Should be included (boundary is inclusive).
        """
        exactly_30_days_ago = (datetime.today() - timedelta(days=30)).strftime("%Y-%m-%d")
        individuals = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": exactly_30_days_ago,
                "Death": "NA",
                "Alive": True
            }
        }
        
        self.assertEqual(validation(individuals), "US35: Recent births: @I1@\n")

    def test_recent_births_5(self):
        """
        Output demonstrating an edge case where a birthday is 31 days from today.
        Should NOT be included (just outside the 30-day window).
        """
        thirty_one_days_ago = (datetime.today() - timedelta(days=31)).strftime("%Y-%m-%d")
        individuals = {
            "@I1@": {
                "ID": "@I1@",
                "Birthday": thirty_one_days_ago,
                "Death": "NA",
                "Alive": True
            }
        }
        
        self.assertEqual(validation(individuals), "")


if __name__ == '__main__':
    unittest.main()

