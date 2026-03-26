import json
import os

class StorageManager:
    
    def __init__(self, file_path="finance_data.json"):
        self.file_path = file_path
        
    def save(self, data):
        """Save a list of dictionaries to a JSON file."""
        try:
            with open(self.file_path, "w") as f:
                json.dump(data, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
        
    def load(self):
        """Load data from the JSON file."""
        if not os.path.exists(self.file_path):
            return []
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        
        except (json.JSONDecodeError, Exception) as e:
            print(f"Error loading data: {e}")
            return []

        
    
    
    