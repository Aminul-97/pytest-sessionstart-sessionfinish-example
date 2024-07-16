import pytest
from src.leap_year import LeapYear


@pytest.hookimpl()
def pytest_sessionstart(session):
    leap_year = LeapYear("https://digidates.de/api/v1/leapyear")
    if leap_year.check_connection() == 200:
        print("API connection successful!")
    else:
        pytest.exit("API Connection Unsuccessful!")


@pytest.hookimpl()
def pytest_sessionfinish(session):
    print("\nTest session finished!")
