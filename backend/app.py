from flask import Flask, request, jsonify
from wallet import create_wallet
from signature import sign_document, verify_signature

app = Flask(__name__)

@app.route('/wallet', methods=['GET'])
def generate_wallet():
    wallet = create_wallet()
    return jsonify(wallet)

@app.route('/sign', methods=['POST'])
def sign():
    data = request.json
    message = data.get('message')
    private_key = data.get('private_key')
    signature = sign_document(message, private_key)
    return jsonify({'signature': signature})

@app.route('/verify', methods=['POST'])
def verify():
    data = request.json
    message = data.get('message')
    signature = data.get('signature')
    public_key = data.get('public_key')
    is_valid = verify_signature(message, signature, public_key)
    return jsonify({'valid': is_valid})

if __name__ == '__main__':
    app.run(debug=True)
