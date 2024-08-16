# Data Preprocessor class
class DataPreprocessor:
    def __init__(self, data):
        self.data = data

    def preprocess(self):
        # Handle missing values
        self.data.fillna(self.data.mean(), inplace=True)

        # Handle outliers
        self.data = self.data[(np.abs(self.data) <= 3 * self.data.std()).all(axis=1)]

        # Encode categorical variables
        categorical_cols = self.data.select_dtypes(include=["object"]).columns
        for col in categorical_cols:
            self.data[col] = pd.get_dummies(self.data[col], drop_first=True)

        return self.data

    def __str__(self):
        return f"DataPreprocessor(data={self.data})"

# Example usage
data_preprocessor = DataPreprocessor(data)
processed_data = data_preprocessor.preprocess()
print(processed_data.head())
