import unittest
from unittest.mock import MagicMock
from fernet import Fernet
from data_privacy_vault.encryption_service import EncryptionService

class TestEncryptionService(unittest.TestCase):

    def setUp(self):
        
        # Mocking Fernet class and methods
        self.mock_fernet = MagicMock(spec=Fernet)
        self.mock_fernet_instance = self.mock_fernet.return_value
        self.mock_fernet_instance.encrypt.return_value = b'encrypted_data'
        self.mock_fernet_instance.decrypt.return_value = b'decrypted_data'

        key = b'kXcLtryX58xIQkmWiLTDpZy0YViYuQdTfBBvRiOVBEQ='
        self.encryption_service = EncryptionService(key)
        self.encryption_service.cipher_suite = self.mock_fernet_instance

    def test_encryption(self):
        data = "mock_data"

        encrypted_data = self.encryption_service.encrypt(data)
        
        self.mock_fernet_instance.encrypt.assert_called_once_with(data)
        self.assertEqual(encrypted_data, b'encrypted_data')

    def test_decryption(self):
        data = "mock_data"

        decrypted_data = self.encryption_service.decrypt(data)
        
        self.mock_fernet_instance.decrypt.assert_called_once_with(data)
        self.assertEqual(decrypted_data, b'decrypted_data')

if __name__ == '__main__':
    unittest.main()
