# Import necessary libraries
import os
import json
import requests
from jinja2 import Template
from datetime import datetime

# Incident Response class
class IncidentResponse:
    def __init__(self, incident_id, incident_type, severity, description, affected_systems):
        self.incident_id = incident_id
        self.incident_type = incident_type
        self.severity = severity
        self.description = description
        self.affected_systems = affected_systems

    def generate_response(self):
        # Load response template
        template = Template(filename="response_template.j2")

        # Render response template with incident data
        response = template.render(
            incident_id=self.incident_id,
            incident_type=self.incident_type,
            severity=self.severity,
            description=self.description,
            affected_systems=self.affected_systems,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        return response

    def send_response(self, notification_system):
        # Send response to notification system
        notification_system.send_notification(self.generate_response())

# Example usage
incident_response = IncidentResponse(
    incident_id="INC123",
    incident_type="Malware Outbreak",
    severity="High",
    description="Malware outbreak detected on multiple systems",
    affected_systems=["system1", "system2", "system3"]
)

notification_system = NotificationSystem()
incident_response.send_response(notification_system)
