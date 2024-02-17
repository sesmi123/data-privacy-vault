from fernet import Fernet

class EncryptionService():

    def __init__(self, symmetric_key: str) -> None:
        self.key = symmetric_key
        self.cipher_suite = Fernet(self.key)

    def encrypt(self, data):
        return self.cipher_suite.encrypt(data)

    def decrypt(self, data):
        return self.cipher_suite.decrypt(data)