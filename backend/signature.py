from ecdsa import SigningKey, VerifyingKey, SECP256k1
import hashlib
import binascii

def sign_document(message, private_key_hex):
    private_key = SigningKey.from_string(bytes.fromhex(private_key_hex), curve=SECP256k1)
    message_hash = hashlib.sha256(message.encode()).digest()
    signature = private_key.sign(message_hash)
    return binascii.hexlify(signature).decode()

def verify_signature(message, signature_hex, public_key_hex):
    try:
        public_key = VerifyingKey.from_string(bytes.fromhex(public_key_hex), curve=SECP256k1)
        message_hash = hashlib.sha256(message.encode()).digest()
        return public_key.verify(bytes.fromhex(signature_hex), message_hash)
    except Exception:
        return False
