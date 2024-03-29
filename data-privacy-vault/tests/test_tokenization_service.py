import unittest
from unittest import mock
from unittest.mock import MagicMock
from data_privacy_vault.redis_connection import RedisConnection
from data_privacy_vault.tokenization_service import TokenizationService

class TestTokenizationService(unittest.TestCase):

    def setUp(self):
        self.redis_conn = MagicMock(spec=RedisConnection)
        self.token_service = TokenizationService(self.redis_conn)

    @mock.patch("data_privacy_vault.tokenization_service.secrets")
    @mock.patch("data_privacy_vault.tokenization_service.encryption_service")
    def test_tokenize_sets_the_token_and_sensitive_data_in_database(self, mock_encryption_service, mock_secrets):
        token = "mock_token"
        mock_secrets.token_hex.return_value = token
        sensitive_data = "sensitive_data"
        encrypted_sensitive_data = "encrypted_sensitive_data"
        mock_encryption_service.encrypt.return_value = encrypted_sensitive_data

        self.token_service.tokenize(sensitive_data)

        self.redis_conn.set.assert_called_once_with(token, encrypted_sensitive_data)

    @mock.patch("data_privacy_vault.tokenization_service.secrets")
    @mock.patch("data_privacy_vault.tokenization_service.encryption_service")
    def test_tokenize_returns_the_token_for_sensitive_data(self, mock_encryption_service, mock_secrets):
        token = "mock_token"
        mock_secrets.token_hex.return_value = token
        sensitive_data = "sensitive_data"
        encrypted_sensitive_data = "encrypted_sensitive_data"
        mock_encryption_service.encrypt.return_value = encrypted_sensitive_data

        result_token = self.token_service.tokenize(sensitive_data)

        self.assertEqual(result_token, token)

    @mock.patch("data_privacy_vault.tokenization_service.encryption_service")
    def test_detokenize_invokes_get_from_redis_db(self, mock_encryption_service):
        token = "mock_token"

        self.token_service.detokenize(token)

        self.redis_conn.get.assert_called_once_with(token)

    @mock.patch("data_privacy_vault.tokenization_service.encryption_service")
    def test_detokenize_with_valid_token_returns_sensitive_data(self, mock_encryption_service):
        token = "mock_token"
        sensitive_data = "sensitive_data"
        encrypted_sensitive_data = "encrypted_sensitive_data"
        self.redis_conn.get.return_value = encrypted_sensitive_data
        mock_encryption_service.decrypt.return_value = sensitive_data.encode('UTF-8')

        detokenized_data = self.token_service.detokenize(token)

        self.assertEqual(detokenized_data, sensitive_data)

    def test_detokenize_with_invalid_token(self):
        invalid_token = "invalid_token"
        self.redis_conn.get.return_value = None

        detokenized_data = self.token_service.detokenize(invalid_token)
        
        self.assertEqual(detokenized_data, "Token not found")

if __name__ == '__main__':
    unittest.main()
