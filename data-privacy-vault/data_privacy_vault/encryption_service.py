from fernet import Fernet

class EncryptionException(Exception):
    pass

class EncryptionService():

    def __init__(self, symmetric_key: str) -> None:
        self.key = symmetric_key
        self.cipher_suite = Fernet(self.key)

    def encrypt(self, data):
        return self.cipher_suite.encrypt(data)

    def decrypt(self, data):
        try:
            return self.cipher_suite.decrypt(data)
        except:
            raise EncryptionException("Failed to decrypt the value")