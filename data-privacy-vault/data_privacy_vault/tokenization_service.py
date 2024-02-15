import secrets

class TokenizationService:
    def __init__(self):
        self.token_map = {}

    def tokenize(self, sensitive_data):
        # Generate a random hexadecimal token
        token = secrets.token_hex(16)
        self.token_map[token] = sensitive_data
        return token

    def detokenize(self, token):
        return self.token_map.get(token, "Token not found")
