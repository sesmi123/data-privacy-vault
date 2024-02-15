import json
import unittest
from unittest import mock
from data_privacy_vault.app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_hello_endpoint(self):
        response = self.app.get('/hello')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Hello, World!')

    @mock.patch("data_privacy_vault.app.tokenization_service")
    def test_tokenize_endpoint(self, tokenization_service_mock):

        # Arrange
        tokenization_service_mock.tokenize.return_value = "valuetoken"
        payload = {
            "id": "req-12345",
            "data": {
                "field": "value"
            }
        }

        # Act
        response = self.app.post('/tokenize', json = payload)

        # Assert
        tokenization_service_mock.tokenize.assert_called_once_with("value")
        self.assertEqual(response.status_code, 201)
        expected_response = {
            "id": "req-12345",
            "data": {
                "field": "valuetoken"
            }
        }
        self.assertEqual(json.loads(response.data), expected_response)

    @mock.patch("data_privacy_vault.app.tokenization_service")
    def test_detokenize_endpoint(self, tokenization_service_mock):

        # Arrange
        tokenization_service_mock.detokenize.return_value = "value"
        payload = {
            "id": "req-12345",
            "data": {
                "field": "valuetoken"
            }
        }

        # Act
        response = self.app.post('/detokenize', json = payload)

        # Assert
        tokenization_service_mock.detokenize.assert_called_once_with("valuetoken")
        self.assertEqual(response.status_code, 200)
        expected_response = {
            "id": "req-12345",
            "data": {
                "field": {
                    "found": True,
                    "value": "value"
                }
            }
        }
        self.assertEqual(json.loads(response.data), expected_response)

if __name__ == '__main__':
    unittest.main()