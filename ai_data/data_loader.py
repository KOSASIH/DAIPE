# Data Loader class
class DataLoader:
    def __init__(self, data_contract):
        self.data_contract = data_contract

    def load(self):
        # Load data from source
        if self.data_contract.data_type == "csv":
            data = pd.read_csv(self.data_contract.data_source)
        elif self.data_contract.data_type == "json":
            data = pd.read_json(self.data_contract.data_source)
        elif self.data_contract.data_type == "parquet":
            data = pd.read_parquet(self.data_contract.data_source)
        else:
            raise ValueError("Invalid data type")

        return data

    def __str__(self):
        return f"DataLoader(data_contract={self.data_contract})"

# Example usage
data_loader = DataLoader(data_contract)
data = data_loader.load()
print(data.head())
