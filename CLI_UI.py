from Finance_Service import FinanceService
from tabulate import tabulate

class CashFlow:
    def __init__(self):
        self.manager = FinanceService()
        
    # Add income method    
    def add_income(self):
        print("--- Add Income ---")
        
        amount = float(input("Amount: "))
        category = input("Category: ")
        date = input("Date (DD-MM-YYYY): ")
        
        self.manager.add_income(amount, category, date)
        print("Income added successfully!")
    
    # Adding expense method
    def add_expense(self):
        print("--- Add Expense ---")
        
        amount = float(input("Amount: "))
        category = input("Category: ")
        date = input("Date (DD-MM-YYYY): ")
        
        self.manager.add_expense(amount, category, date)
        print("Expense added successfully!")
        
    # View All transactions
    def view_transactions(self):
        
        data = self.manager.view_transactions()
        
        if not data:
            print("No transactions found!")
            return
        
        table = [[entry["id"], entry["category"], entry["amount"], entry["date"]] for entry in data]
        print("\n" + tabulate(table, headers=["ID", "Category", "Amount", "Date"], tablefmt="fancy_grid"))
    
    #search transactions method
    def search_transactions(self):
        query = input("\nEnter Category/Date(DD-MM-YYYY): ").strip()
        if not query:
            return
        
        results = self.manager.search_transactions(query)
        if not results:
            print( "No results found." )
            return
        
        table = [[entry["id"], entry["category"], entry["amount"], entry["date"]] for entry in results]
        print("\n" + tabulate(table, headers=["ID", "Category", "Amount", "Date"], tablefmt="fancy_grid"))
        
        return True
        
    #delete transaction method
    def delete_transaction(self):    
        try:
            id = int(input("\nEnter Transaction ID to delete: "))
            if self.manager.delete_transaction(id):
                print(f"Transaction {id} deleted.")
            else:
                print("Transaction ID not found.")
        except ValueError:
            print("Invalid ID.")
    
    # update transaction method        
    def update_transaction(self):
        
        try:
            id = int(input("\nEnter Transaction ID to update: "))
            
            amount_input = input("New Amount (leave blank to keep current): ").strip()
            category_input = input("New Category (leave blank to keep current): ").strip()
            date_input = input("New Date (DD-MM-YYYY, leave blank to keep current): ").strip()
            
            amount = float(amount_input) if amount_input else None
            category = category_input if category_input else None
            date = date_input if date_input else None
            
            if self.manager.update_transaction(id, amount, category, date):
                print(f"Transaction {id} updated.")
            else:
                print("Transaction ID not found.")
        except ValueError:
            print("Invalid input.")   
        
    def display_features(self):
        while True:
            
            print("1. " +  "Add a new income" )
            print("2. " + "Add a new expense" )
            print("3. " + "View all transactions" )
            print("4. " + "Search for a transaction" )
            print("5. " + "Delete a transaction" )
            print("6. " + "Update a transaction" )
            print("7. " + "View summary report" )
            print("0. " + "Exit" )    
            
            choice = input("\nChoose an option: ")
                
            match choice:   
                case '1':
                    self.add_income()
                case '2':
                    self.add_expense()
                case '3':
                    self.view_transactions()
                case '4':
                    self.search_transactions()
                case '5':
                    self.delete_transaction()
                case '6':
                    self.update_transaction()
                case '7':
                    pass
                case '0':
                    pass
                case _:
                    print( "Invalid choice. Please try again." )        
            