import ipfshttpclient

class IpfsClient:
    def __init__(self, host, port):
        self.client = ipfshttpclient.connect(host, port)

    def add_file(self, file_path):
        return self.client.add(file_path)

    def get_file(self, file_hash):
        return self.client.cat(file_hash)
