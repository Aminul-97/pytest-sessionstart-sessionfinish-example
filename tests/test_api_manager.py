import pytest
from src.api_manager import Manage_api

# Fixture to generate objact
@pytest.fixture(scope="session")
def api_manager_object():
    return Manage_api("https://digidates.de/api/v1/checkdate?date=2023-01-01")

# Fixture to generate objact with different link
@pytest.fixture(scope="session")
def api_manager_object_2():
    return Manage_api("https://digidates.de/api/v1/leapyear?year=2024")

# Testing date validation using the API
def test_date_validation(api_manager_object):
    assert api_manager_object.get_data() == "{\"checkdate\":true}"

# Checking if a year is a leap year using the API
def test_leap_year(api_manager_object_2):
    assert api_manager_object_2.get_data() == "{\"leapyear\":true}"