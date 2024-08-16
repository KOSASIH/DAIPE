# Data Contract class
class DataContract:
    def __init__(self, data_type, data_schema, data_source, data_destination):
        self.data_type = data_type
        self.data_schema = data_schema
        self.data_source = data_source
        self.data_destination = data_destination

    def validate(self):
        # Validate data type
        if self.data_type not in ["csv", "json", "parquet"]:
            raise ValueError("Invalid data type")

        # Validate data schema
        if not isinstance(self.data_schema, dict):
            raise ValueError("Invalid data schema")

        # Validate data source
        if not isinstance(self.data_source, str):
            raise ValueError("Invalid data source")

        # Validate data destination
        if not isinstance(self.data_destination, str):
            raise ValueError("Invalid data destination")

    def to_dict(self):
        return {
            "data_type": self.data_type,
            "data_schema": self.data_schema,
            "data_source": self.data_source,
            "data_destination": self.data_destination
        }

    def __str__(self):
        return f"DataContract(data_type={self.data_type}, data_schema={self.data_schema}, data_source={self.data_source}, data_destination={self.data_destination})"

# Example usage
data_contract = DataContract(
    data_type="csv",
    data_schema={"column1": "int", "column2": "string"},
    data_source="data.csv",
    data_destination="processed_data.csv"
)

print(data_contract.to_dict())
