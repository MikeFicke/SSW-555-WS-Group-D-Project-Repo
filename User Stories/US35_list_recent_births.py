# Group D
# SSW-555-WS
# User Story: List Recent Births (US35)
# Author: Michael Ficke
# Acknowledgement: IDE Auto-complete was used for certain lines of code

"""
This user story lists all individuals from the GEDCOM file who were born within the last 30 days
"""

from datetime import datetime, timedelta

def validate_recent_births(individuals):
    """
    Validates that all individuals were born within the last 30 days
    """
    # Get today's date
    today = datetime.today().date()

    # Get the date 30 days ago
    # citation: https://www.google.com/search?q=how+to+use+timedelta+in+Python+to+calculate+days+apart+between+two+dates%3F&sca_esv=2c404eaf43af4804&rlz=1C1CHBF_enUS1023US1023&sxsrf=APpeQnveG1_Kw5GkSbJ4PYp62_0tbXNXtA%3A1785451955859&udm=50&source=chrome.ob&fbs=ABfTbFVyMZGZf1hfvX9uKjN_-G8cxpBkeIeqYwoCbfNVc4vKE4f6ZJqUzPbNrAmWktdS6nG82-1N4OXO01WJkKgjHAhRM6ScTiHqzjAJLebouTbGuy4vj0NVx0QN6KObJnDwqlpzpbc9KkDPc7uS48iQTdKnZOML_UnFPDHKx-qlCXk-s-WbZzNzLu_x64IXm_u1PE0MKsnFqPNm-zKHHhuyMRiRFjpoag&aep=1&ntc=1&cs=1&sa=X&ved=2ahUKEwihnt7svvuVAxVqhYkEHeh3OWgQ2J8OegQIEhAD&biw=1536&bih=825.2000122070312&dpr=2.5&sourceid=chrome&ccb=1&hl=en-US&atvm=2&mstk=AUtExfCKs6eWUYC4fA8_v3KmrVgJTo22N4U1CBajSzLTAZgQZ8UT0M1Hqmpaawe-gjbZKbqZ9SnBwnv-AnVpOJUkqQr4uA6Lte6F_MRplHmbA_vlPUEajXAHZo7IazukSKQbn5Uj5k8orkUwdUJh76L4Jn7laAYDHj_tlqE&csuir=1&mtid=ztVras_THr-x5NoPmNSzqQQ
    thirty_days_ago = today - timedelta(days=30)

    # Create a list to store the ids of the recently born individuals
    recent_births = []

    # Loop through the individuals dictionary
    for individual in individuals.values():
        # Get the birthday as a string
        birthday_string = individual["Birthday"]
        if birthday_string == "NA" or birthday_string is None:
            # Skip; there is no value to check
            continue
        # Convert the birthday string into a datetime object for comparison
        birthday_date = datetime.strptime(birthday_string, "%Y-%m-%d").date()

        # Check if the birthday is within the last 30 days
        if thirty_days_ago <= birthday_date <= today:
            # Add the individual's id to the list
            recent_births.append(individual["ID"])

    # Print the list of recently born individuals
    if len(recent_births) > 0:
        print(f"US35: Recent births: {', '.join(recent_births)}")
