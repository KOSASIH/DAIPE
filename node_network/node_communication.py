# Import necessary libraries
import os
import json
import socket
import threading
import time
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Node Communication class
class NodeCommunication:
    def __init__(self, node_id, node_key, node_port, network_nodes):
        self.node_id = node_id
        self.node_key = node_key
        self.node_port = node_port
        self.network_nodes = network_nodes
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(("localhost", self.node_port))
        self.socket.listen(5)
        self.threads = []

    def start_node(self):
        # Start node and listen for incoming connections
        print(f"Node {self.node_id} started and listening on port {self.node_port}")
        while True:
            conn, addr = self.socket.accept()
            print(f"Connected by {addr}")
            t = threading.Thread(target=self.handle_connection, args=(conn,))
            t.start()
            self.threads.append(t)

    def handle_connection(self, conn):
        # Handle incoming connection and receive data
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received data from {addr}: {data.decode()}")
            self.process_data(data.decode())

    def process_data(self, data):
        # Process received data and take action
        data_json = json.loads(data)
        if data_json["type"] == "message":
            print(f"Received message from node {data_json['node_id']}: {data_json['message']}")
            self.send_response(data_json["node_id"], "ack")
        elif data_json["type"] == "request":
            print(f"Received request from node {data_json['node_id']}: {data_json['request']}")
            self.send_response(data_json["node_id"], "response")

    def send_response(self, node_id, response):
        # Send response to node
        response_json = json.dumps({"type": "response", "node_id": self.node_id, "response": response})
        self.send_data(node_id, response_json)

    def send_data(self, node_id, data):
        # Send data to node
        node_port = self.network_nodes[node_id]["port"]
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect(("localhost", node_port))
        conn.sendall(data.encode())
        conn.close()

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
node_port = 8080
network_nodes = {
    "node1": {"port": 8080},
    "node2": {"port": 8081},
    "node3": {"port": 8082},
}

node_communication = NodeCommunication(node_id, node_key, node_port, network_nodes)
node_communication.start_node()
