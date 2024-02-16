from data_privacy_vault.app_controller import detokenize_request, tokenize_request
from flask import Flask, request

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/tokenize', methods=['POST'])
def tokenize():
    data = request.get_json()
    return tokenize_request(data)

@app.route('/detokenize', methods=['POST'])
def detokenize():
    data = request.get_json()
    return detokenize_request(data)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
