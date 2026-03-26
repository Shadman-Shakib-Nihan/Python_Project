from Finance_Service import FinanceService

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
                    pass
                case '4':
                    pass
                case '5':
                    self.delete_transaction()
                case '6':
                    pass
                case '7':
                    pass
                case '0':
                    pass
                case _:
                    print( "Invalid choice. Please try again." )        
            