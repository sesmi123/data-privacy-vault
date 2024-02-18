import unittest
from unittest.mock import MagicMock, patch
from data_privacy_vault import config
from flask import Response
from data_privacy_vault.auth import check_auth, authenticate, requires_auth

class TestAuthFunctions(unittest.TestCase):

    def setUp(self):
        self.username = config.auth["username"]
        self.password = config.auth["password"]

    def test_check_auth(self):
        # Test with correct credentials
        self.assertTrue(check_auth(self.username, self.password))
        
        # Test with incorrect credentials
        self.assertFalse(check_auth("wrong_user", "wrong_password"))

    def test_authenticate(self):
        response = authenticate()
        self.assertIsInstance(response, Response)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data.decode('utf-8'), 'Could not verify your access level for this URL.\nYou have to login with proper credentials')
        self.assertIn('WWW-Authenticate', response.headers)
        self.assertEqual(response.headers['WWW-Authenticate'], 'Basic realm="Login Required"')

if __name__ == '__main__':
    unittest.main()
