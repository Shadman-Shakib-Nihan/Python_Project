from Finance_Service import FinanceService
from tabulate import tabulate
from colorama import Fore, Style, init
from datetime import datetime


# initial colorama
init(autoreset=True)

class CashFlow:
    def __init__(self):
        self.manager = FinanceService()
    
    # Get the transaction input from the user
    def get_transaction_input(self,):
        while True:
            try:
                
                amount = float(input("Amount: "))
                if amount > 0:
                    break
                else:
                    print(Fore.RED + "Amount cannot be zero or negative!")
            except ValueError:
                print(Fore.RED + "Invalid amount. Please enter a number.")
                continue

        print(Fore.CYAN + "Press Enter to use today's date, or enter a date (DD-MM-YYYY).")
        while True:
            date = input("Date (DD-MM-YYYY): ").strip()
            
            if not date:
                date = datetime.now().strftime("%d-%m-%Y")
                print(f"Date: {Fore.GREEN}{date}")
                
            if date:
                try:
                    datetime.strptime(date, "%d-%m-%Y")
                    break
                except ValueError:
                    print(Fore.RED + "Invalid date format. Please use DD-MM-YYYY.")

        return amount, date
       
    # Add income
    def add_income(self):
        
        print("+------------------+")
        print(f"|   {Fore.LIGHTMAGENTA_EX}ADD INCOME{Style.RESET_ALL}     |")
        print("+------------------+\n")
        
        print(Fore.CYAN + "Press Enter to use the default category (Salary), or type your own category.")
        while True:
            category = input("Category: ").strip()
            if not category:
                category = "Salary"
                print("Category: " + Fore.GREEN + category)
            
            if len(category) <= 2 or not category.replace(" ", "").isalpha():
                print(Fore.RED + "Category must be at least 2 characters long and contain only letters.")
                continue
            break 
        
        data = self.get_transaction_input()
        if not data:
            return
                    
        amount, date = data
        self.manager.add_income(amount, category, date )
        print(Fore.GREEN + "\nIncome added successfully!\n")
     
    
    
    # add expense   
    def add_expense(self):
        
        print("+------------------+")
        print(f"|   {Fore.LIGHTMAGENTA_EX}ADD EXPENSE{Style.RESET_ALL}    |")
        print("+------------------+\n")
        
        while True:
            category = input("Category: ").strip()
            if not category:
                print(Fore.RED + "Category cannot be empty!")
                continue
            
            if len(category) <= 2 or not category.replace(" ", "").isalpha():
                print(Fore.RED + "Category must be at least 2 characters long and contain only letters.")
                continue
            break
        
        data = self.get_transaction_input()
        if not data:
            return
        
        amount, date = data
        
        self.manager.add_expense(amount, category, date)
        print(Fore.GREEN + "\nExpense added successfully!\n")
        
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
        while True:
            query = input("\nEnter Category/Date(DD-MM-YYYY): ").strip()
            if not query:
                return
            
            results = self.manager.search_transactions(query)
            if not results:
                print(Fore.RED + "No results found." )
                continue
            
            
            table = [[entry["id"], entry["category"], entry["amount"], entry["date"]] for entry in results]
            print("\n" + tabulate(table, headers=["ID", "Category", "Amount", "Date"], tablefmt="fancy_grid"))
            break
        
        
    #delete transaction method
    def delete_transaction(self):
        while True:
            query = input("\nEnter a category/date (DD-MM-YYYY) to find the transaction you want to delete: ").strip()
            
            results = self.manager.search_transactions(query)
            if not results:
                print(Fore.RED + "No results found." )
                continue
            
            table = [[entry["id"], entry["category"], entry["amount"], entry["date"]] for entry in results]
            print("\n" + tabulate(table, headers=["ID", "Category", "Amount", "Date"], tablefmt="fancy_grid"))
            break    
                
        try:
            id = int(input("\nEnter Transaction ID to delete: "))
            if self.manager.delete_transaction(id):
                print(Fore.GREEN + f"Transaction {id} deleted.\n")
            else:
                print(Fore.RED + "Transaction ID not found.")
        except ValueError:
            print(Fore.RED + "Invalid ID.")
    
    # update transaction method        
    def update_transaction(self):
        while True:
            query = input("\n1.Income\n2.Expense\nPress 1/2 or Enter type to find the transaction you want to update: ").strip().lower()
            if query == "1" or query == "income":
                query = "income"
            elif query == "2" or query == "expense":
                query = "expense"
            else:
                print(Fore.RED + "Invalid input. Please enter '1' for Income or '2' for Expense.")
                continue
            
            results = self.manager.search_transactions(query)
            if not results:
                print(Fore.RED + "No results found." )
                return
            
            table = [[entry["id"], entry["category"], entry["amount"], entry["date"]] for entry in results]
            print("\n" + tabulate(table, headers=["ID", "Category", "Amount", "Date"], tablefmt="fancy_grid"))
            break
        while True:
            try:
                id = int(input("\nEnter Transaction ID to update: "))
                if not any(entry["id"] == id for entry in results):
                    print(Fore.RED + "Transaction ID not found.")
                    continue
                
                amount_input = float(input("New Amount (leave blank to keep current): ").strip())
                category_input = input("New Category (leave blank to keep current): ").strip()
                date_input = input("New Date (DD-MM-YYYY, leave blank to keep current): ").strip()
                
                amount = amount_input if amount_input else None
                category = category_input if category_input else None
                date = date_input if date_input else None
                
                if self.manager.update_transaction(id, amount, category, date):
                    print(Fore.GREEN + f"Transaction {id} updated.\n")
                else:
                    print(Fore.RED + "Transaction ID not found.")
            except ValueError:
                print(Fore.RED + "Invalid input.")
            break   
    
    #view summary report method
    def view_summary_report(self):
        summary = self.manager.get_summary()
        if not summary:
            print(Fore.RED + "No transactions found!")
            return
        
        total_income = summary["total_income"]
        total_expenses = summary["total_expenses"]
        balance = summary["balance"]
        
        print("\n--- Summary Report ---")
        print(Fore.GREEN + f"Total Income: ${total_income:.2f}")
        print(Fore.RED + f"Total Expenses: -${total_expenses:.2f}")
        print(Fore.BLUE + f"Net Balance: ${balance:.2f}")
        
         
            