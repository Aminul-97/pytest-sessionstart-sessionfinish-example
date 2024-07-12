import pytest
from src.rsa import Encrypt_decrypt

# Fixture to generate objact
@pytest.fixture(scope="session")
def rsa_object():
    return Encrypt_decrypt(50)

# Fixture to generate keys
@pytest.fixture
def generate_keys(rsa_object):
    return rsa_object.generate_keys()

# Testing encryption/decryption
def test_rsa(generate_keys, rsa_object):
    public_key, private_key, modulus = generate_keys
    message = "This is a message!"
    encrypted_message = rsa_object.encrypt_message(message, public_key, modulus)
    assert rsa_object.decrypt_message(encrypted_message, private_key, modulus) == message