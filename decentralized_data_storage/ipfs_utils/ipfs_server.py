# Import necessary libraries
import os
import json
import ipfshttpclient
from flask import Flask, request, jsonify
from flask_cors import CORS
from ipfsapi import IpfsApi

# IPFS Server class
class IpfsServer:
    def __init__(self, ipfs_api, ipfs_http_client):
        self.ipfs_api = ipfs_api
        self.ipfs_http_client = ipfs_http_client

    def add_file(self, file_path):
        # Add file to IPFS
        with open(file_path, "rb") as f:
            file_hash = self.ipfs_api.add(f.read())
        return file_hash

    def get_file(self, file_hash):
        # Get file from IPFS
        file_data = self.ipfs_api.cat(file_hash)
        return file_data

    def pin_file(self, file_hash):
        # Pin file to IPFS
        self.ipfs_api.pin_add(file_hash)

    def unpin_file(self, file_hash):
        # Unpin file from IPFS
        self.ipfs_api.pin_rm(file_hash)

    def get_file_info(self, file_hash):
        # Get file info from IPFS
        file_info = self.ipfs_api.object_stat(file_hash)
        return file_info

    def search_files(self, query):
        # Search files in IPFS
        search_results = self.ipfs_api.search(query)
        return search_results

# Flask API
app = Flask(__name__)
CORS(app)

# IPFS API client
ipfs_api = IpfsApi()

# IPFS HTTP client
ipfs_http_client = ipfshttpclient.connect()

# IPFS Server instance
ipfs_server = IpfsServer(ipfs_api, ipfs_http_client)

# API endpoints
@app.route("/add_file", methods=["POST"])
def add_file():
    file_path = request.form["file_path"]
    file_hash = ipfs_server.add_file(file_path)
    return jsonify({"file_hash": file_hash})

@app.route("/get_file", methods=["GET"])
def get_file():
    file_hash = request.args.get("file_hash")
    file_data = ipfs_server.get_file(file_hash)
    return jsonify({"file_data": file_data})

@app.route("/pin_file", methods=["POST"])
def pin_file():
    file_hash = request.form["file_hash"]
    ipfs_server.pin_file(file_hash)
    return jsonify({"message": "File pinned successfully"})

@app.route("/unpin_file", methods=["POST"])
def unpin_file():
    file_hash = request.form["file_hash"]
    ipfs_server.unpin_file(file_hash)
    return jsonify({"message": "File unpinned successfully"})

@app.route("/get_file_info", methods=["GET"])
def get_file_info():
    file_hash = request.args.get("file_hash")
    file_info = ipfs_server.get_file_info(file_hash)
    return jsonify({"file_info": file_info})

@app.route("/search_files", methods=["GET"])
def search_files():
    query = request.args.get("query")
    search_results = ipfs_server.search_files(query)
    return jsonify({"search_results": search_results})

if __name__ == "__main__":
    app.run(debug=True)
