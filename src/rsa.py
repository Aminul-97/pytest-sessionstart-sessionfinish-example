from rsa_python import rsa

class Encrypt_decrypt:
    """
    Class to encrypt/decrypt a message.

    Args:
    Key:int

    Returns:
    None
    """
    def __init__(self, key:int):
        self.key = key
    
    def generate_keys(self) -> tuple:
        """
        Function to generate keys.
        """
        keys = rsa.generate_key_pair(self.key)
        return keys["public"], keys["private"], keys["modulus"]

    def encrypt_message(self, message, public_key, modulus) -> str:
        """
        Function to encrypt message.
        """
        return rsa.encrypt(message, public_key, modulus)
    
    def decrypt_message(self, encrypted_message, private_key, modulus) -> str:
        """
        Function to decrypt message.
        """
        return rsa.decrypt(encrypted_message, private_key, modulus)

    
"""
ed = Encrypt_decrypt(10)
public_key, private_key, modulus = ed.generate_keys()
print(public_key)
print(private_key)
print(modulus)
message = "This is a message!"
encrypted_message = ed.encrypt_message(message, public_key, modulus)
print(encrypted_message)
print(ed.decrypt_message(encrypted_message, private_key, modulus))
"""