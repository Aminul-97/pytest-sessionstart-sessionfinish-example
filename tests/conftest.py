import pytest
from src.api_manager import Manage_api

@pytest.hookimpl()
def pytest_sessionstart(session):
    try:
        api_mgr = Manage_api("https://digidates.de/api/v1/checkdate?date=2023-01-01")
        if api_mgr.check_connection() == 200:
             print("API connection successful!")
        else:
            raise Exception("Invalid link.")
    except:
        raise Exception("Failed to connect!")
    print("==== Entering the tests ====")

@pytest.hookimpl()
def pytest_sessionfinish(session):
    print("\nTest session finished!")
    
