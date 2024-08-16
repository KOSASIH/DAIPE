import pandas as pd
from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    def __init__(self, data):
        self.data = data
        self.model = IsolationForest(contamination=0.1)

    def train(self):
        self.model.fit(self.data)

    def predict(self, new_data):
        return self.model.predict(new_data)
