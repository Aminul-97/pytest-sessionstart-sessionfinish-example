import pytest
from src.rsa import Encrypt_decrypt

@pytest.hookimpl()
def pytest_sessionstart(session):
    try:
        ed = Encrypt_decrypt(12)
        print("Object Creation successful!")
        if [type(ed.generate_keys) == tuple]:
             print("Key generation successful!")
        else:
            raise Exception("Failed to generate keys. Stopping the test.")
    except:
        raise Exception("Failed to create object. Stopping the test.")
    print("==== Entering the tests ====")

@pytest.hookimpl()
def pytest_sessionfinish(session):
    print("\nTest session finish")
    
