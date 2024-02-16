import unittest
from unittest import mock
from unittest.mock import MagicMock
from data_privacy_vault.redis_connection import RedisConnection

class TestRedisConnection(unittest.TestCase):

    def setUp(self):
        self.redis_client = MagicMock()
        self.redis_connection = RedisConnection()
        self.redis_connection.redis_client = self.redis_client

    @mock.patch("data_privacy_vault.redis_connection.redis")
    def test_connect(self, mock_redis):
        self.redis_connection.connect()
        
        mock_redis.StrictRedis.assert_called_once_with(host='localhost', port=6379, db=0)

    def test_set(self):
        key = 'test_key'
        value = 'test_value'
        self.redis_connection.set(key, value)
        
        self.redis_client.set.assert_called_once_with(key, value)

    def test_get(self):
        key = 'test_key'
        expected_value = b'test_value' 
        self.redis_client.get.return_value = expected_value

        result = self.redis_connection.get(key)
        
        self.redis_client.get.assert_called_once_with(key)
        self.assertEqual(result, expected_value)

if __name__ == '__main__':
    unittest.main()
