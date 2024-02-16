from flask import jsonify
from data_privacy_vault.tokenization_service import TokenizationService

tokenization_service = TokenizationService()


def tokenize_request(data):
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


def detokenize_request(data):
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
