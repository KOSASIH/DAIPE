# Import necessary libraries
import os
import json
import requests
import psutil

# Node Monitoring class
class NodeMonitoring:
    def __init__(self, node_id, monitoring_server_url):
        self.node_id = node_id
        self.monitoring_server_url = monitoring_server_url

    def monitor_node(self):
        # Monitor node resources and send data to monitoring server
        node_data = {
            "node_id": self.node_id,
            "cpu_usage": psutil.cpu_percent(),
            "memory_usage": psutil.virtual_memory().percent,
            "storage_usage": psutil.disk_usage('/').percent
        }
        response = requests.post(self.monitoring_server_url, data=json.dumps(node_data))
        if response.status_code == 200:
            print(f"Node {self.node_id} monitoring data sent successfully")
        else:
            print(f"Error sending node {self.node_id} monitoring data: {response.text}")

    def start_monitoring(self):
        # Start monitoring node resources at regular intervals
        while True:
            self.monitor_node()
            time.sleep(60)  # Monitor every 60 seconds

# Example usage
node_id = "node1"
monitoring_server_url = "https://monitoring-server.com/monitor"

node_monitoring = NodeMonitoring(node_id, monitoring_server_url)
node_monitoring.start_monitoring()
