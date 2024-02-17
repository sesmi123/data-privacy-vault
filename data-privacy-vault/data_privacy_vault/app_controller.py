from flask import jsonify
from data_privacy_vault import config
from data_privacy_vault.redis_connection import RedisConnection
from data_privacy_vault.tokenization_service import TokenizationService

redis_config = {
    "host": config.redis["host"],
    "port": config.redis["port"],
    "db": config.redis["db"],
}
redis_conn = RedisConnection(**redis_config)
redis_conn.connect()

tokenization_service = TokenizationService(redis_conn)


class ApplicationController():

    def tokenize_request(self, data):
        try:
            # Check if request payload is valid
            if not data or 'id' not in data or 'data' not in data:
                return jsonify({'error': 'Invalid request payload'}), 400
            
            req_id = data['id']
            fields_data = data['data']
            
            # Tokenize each field value
            tokenized_data = {}
            for field, value in fields_data.items():
                tokenized_data[field] = tokenization_service.tokenize(value)
            
            # Construct the response payload
            response_payload = {'id': req_id, 'data': tokenized_data}
            
            return jsonify(response_payload), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def detokenize_request(self, data):
        try:
            # Check if request payload is valid
            if not data or 'id' not in data or 'data' not in data:
                return jsonify({'error': 'Invalid request payload'}), 400
            
            req_id = data['id']
            fields_data = data['data']
            
            # Tokenize each field value
            detokenized_data = {}
            for field, value in fields_data.items():
                detokenized_value = tokenization_service.detokenize(value)
                detokenized_data[field] = {"found": detokenized_value != "Token not found", 
                                        "value": detokenized_value if detokenized_value != "Token not found" else ""}

            # Construct the response payload
            response_payload = {'id': req_id, 'data': detokenized_data}
            
            return jsonify(response_payload), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500