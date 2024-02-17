import secrets
from data_privacy_vault import config
from data_privacy_vault.abstract_db_connection import AbstractDBConnection
from data_privacy_vault.encryption_service import EncryptionService

key = config.data_encryption_key
encryption_service = EncryptionService(key)

class TokenizationService:
    def __init__(self, db_connection: AbstractDBConnection):
        self.db_connection = db_connection

    def tokenize(self, sensitive_data):
        # Generate a random hexadecimal token
        token = secrets.token_hex(16)
        encrypted_sensitive_data = encryption_service.encrypt(sensitive_data)
        self.db_connection.set(token, encrypted_sensitive_data)
        return token

    def detokenize(self, token):
        encrypted_sensitive_data = self.db_connection.get(token)
        if encrypted_sensitive_data:
            return encryption_service.decrypt(encrypted_sensitive_data).decode('UTF-8')
        else:
            return "Token not found"
