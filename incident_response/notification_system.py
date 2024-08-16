# Import necessary libraries
import os
import json
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP

# Notification System class
class NotificationSystem:
    def __init__(self, notification_config):
        self.notification_config = notification_config

    def send_notification(self, response):
        # Load notification configuration
        notification_config = self.notification_config

        # Send notification via email
        msg = MIMEMultipart()
        msg["Subject"] = "Incident Response - " + response["incident_id"]
        msg["From"] = notification_config["email_from"]
        msg["To"] = notification_config["email_to"]

        body = response["response"]
        msg.attach(MIMEText(body, "plain"))

        server = SMTP(notification_config["smtp_server"], notification_config["smtp_port"])
        server.starttls()
        server.login(notification_config["smtp_username"], notification_config["smtp_password"])
        server.sendmail(notification_config["email_from"], notification_config["email_to"], msg.as_string())
        server.quit()

        # Send notification via API
        api_url = notification_config["api_url"]
        api_key = notification_config["api_key"]
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        response = requests.post(api_url, headers=headers, json=response)
        if response.status_code != 200:
            print("Error sending notification via API")

    def load_notification_config(self):
        # Load notification configuration from file
        with open("notification_config.json", "r") as f:
            notification_config = json.load(f)
        return notification_config

# Example usage
notification_system = NotificationSystem(NotificationSystem().load_notification_config())
