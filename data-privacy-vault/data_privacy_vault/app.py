from data_privacy_vault.app_controller import ApplicationController
from data_privacy_vault.auth import requires_auth
from flask import Flask, request

app = Flask(__name__)
controller = ApplicationController()

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/tokenize', methods=['POST'])
@requires_auth
def tokenize():
    data = request.get_json()
    return controller.tokenize_request(data)

@app.route('/detokenize', methods=['POST'])
@requires_auth
def detokenize():
    data = request.get_json()
    return controller.detokenize_request(data)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
