from Storage import StorageManager


class FinanceService:
    def __init__(self):
        self.storage = StorageManager()
    
    # Adding income methods
    def add_income(self, amount, category, date):
        """Add an income entry as a dictionary."""
        data = self.storage.load()
        new_id = max([entry.get("id", 0) for entry in data], default=0) + 1
        new_entry = {
            "id": new_id,
            "category": category,
            "amount": amount,  
            "date": date,
            "type": "income"
        }
        data.append(new_entry)
        return self.storage.save(data)
    
    # Adding expense methods
    def add_expense(self, amount, category, date):
        """Add an expense entry."""
        data = self.storage.load()
        new_id = max([entry.get("id", 0) for entry in data], default=0) + 1
        new_entry = {
            "id": new_id,
            "category": category,
            "amount": amount,  
            "date": date,
            "type": "expense"
        }
        data.append(new_entry)
        return self.storage.save(data)
    
        
        
    
    