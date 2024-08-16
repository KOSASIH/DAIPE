import socket

class NodeManager:
    def __init__(self, node_id, node_address):
        self.node_id = node_id
        self.node_address = node_address
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.node_address, 8080))

    def send_message(self, message):
        self.socket.send(message.encode())

    def receive_message(self):
        return self.socket.recv(1024).decode()
