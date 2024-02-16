import secrets
from data_privacy_vault.abstract_db_connection import AbstractDBConnection

class TokenizationService:
    def __init__(self, db_connection: AbstractDBConnection):
        self.db_connection = db_connection

    def tokenize(self, sensitive_data):
        # Generate a random hexadecimal token
        token = secrets.token_hex(16)
        self.db_connection.set(token, sensitive_data)
        return token

    def detokenize(self, token):
        sensitive_data = self.db_connection.get(token)
        if sensitive_data:
            return sensitive_data.decode('utf-8')
        else:
            return "Token not found"
