# Import necessary libraries
import os
import json
import requests
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Node Registration class
class NodeRegistration:
    def __init__(self, node_id, node_key, registration_server_url):
        self.node_id = node_id
        self.node_key = node_key
        self.registration_server_url = registration_server_url

    def register_node(self):
        # Register node with registration server
        registration_data = {
            "node_id": self.node_id,
            "node_key": self.node_key,
            "node_type": "compute_node",
            "node_capabilities": ["cpu", "memory", "storage"]
        }
        encrypted_registration_data = self.encrypt_data(json.dumps(registration_data))
        response = requests.post(self.registration_server_url, data=encrypted_registration_data)
        if response.status_code == 200:
            print(f"Node {self.node_id} registered successfully")
        else:
            print(f"Error registering node {self.node_id}: {response.text}")

    def encrypt_data(self, data):
        # Encrypt data using Fernet symmetric encryption
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.node_key.encode(),
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(self.node_key.encode()))
        f = Fernet(key)
        encrypted_data = f.encrypt(data.encode())
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        # Decrypt data using Fernet symmetric encryption
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.node_key.encode(),
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(self.node_key.encode()))
        f = Fernet(key)
        decrypted_data = f.decrypt(encrypted_data)
        return decrypted_data.decode()

# Example usage
node_id = "node1"
node_key = "my_secret_key"
registration_server_url = "https://registration-server.com/register"

node_registration = NodeRegistration(node_id, node_key, registration_server_url)
node_registration.register_node()
