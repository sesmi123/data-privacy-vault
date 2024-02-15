import unittest
from data_privacy_vault.tokenization_service import TokenizationService

class TestTokenizationService(unittest.TestCase):

    def setUp(self):
        self.token_service = TokenizationService()

    def test_tokenize(self):
        sensitive_data = "sensitive_data"
        token = self.token_service.tokenize(sensitive_data)
        self.assertIsNotNone(token)
        self.assertIn(token, self.token_service.token_map)
        self.assertEqual(self.token_service.token_map[token], sensitive_data)

    def test_detokenize_with_valid_token(self):
        sensitive_data = "sensitive_data"
        token = self.token_service.tokenize(sensitive_data)
        detokenized_data = self.token_service.detokenize(token)
        self.assertEqual(detokenized_data, sensitive_data)

    def test_detokenize_with_invalid_token(self):
        invalid_token = "invalid_token"
        detokenized_data = self.token_service.detokenize(invalid_token)
        self.assertEqual(detokenized_data, "Token not found")

if __name__ == '__main__':
    unittest.main()
