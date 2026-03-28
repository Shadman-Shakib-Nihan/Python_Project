from Finance_Service import FinanceService
from tabulate import tabulate
from colorama import Fore, Style, init
from datetime import datetime
from utils import ValidationError, InputData


# initial colorama
init(autoreset=True)

class CashFlow:
    def __init__(self):
        self.manager = FinanceService()
        self.validator = ValidationError()
        self.input_handler = InputData()    
        
         
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
            
            if not self.validator.categoryValidation(category):
                print(Fore.RED + "Category must be at least 2 characters long and contain only letters.")
                continue
            break 
        
        data = self.input_handler.takeInputData()   
        date, amount = data 
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
            
            if not self.validator.categoryValidation(category):
                print(Fore.RED + "Category must be at least 2 characters long and contain only letters.")
                continue
            break
        
        data = self.input_handler.takeInputData()
        date, amount = data 
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
                selected_entry = next((entry for entry in results if entry["id"] == id), None)
                if not selected_entry:
                    print(Fore.RED + "Transaction ID not found in the search results.")
                    continue
                break
            except ValueError:
                print(Fore.RED + "Invalid ID format. Please enter a number.")
        
        while True:
            try:
                amount_input = input(f"New Amount (Current: {selected_entry['amount']}, press enter to keep current): ").strip()
                if not amount_input:
                    amount = selected_entry['amount']
                else:
                    try:
                        amount = float(amount_input)
                        if not self.validator.amountValidation(amount):
                            print(Fore.RED + "Amount cannot be zero or negative!")
                            continue
                    except ValueError:
                        print(Fore.RED + "Invalid amount format.")
                        continue
                    
                category_input = input(f"New Category (Current: {selected_entry['category']}, press enter to keep current): ").strip()
                if not category_input:
                    category = selected_entry['category']
                else:
                    if not self.validator.categoryValidation(category_input):
                        print(Fore.RED + "Category must be at least 3 characters long and contain only letters.")
                        continue
                    category = category_input
                                
                date_input = input(f"New Date (DD-MM-YYYY, Current: {selected_entry['date']}, press enter to keep current): ").strip()
                if not date_input:
                    date = selected_entry['date']
                else:
                    if not self.validator.dateValidation(date_input):
                        print(Fore.RED + "Invalid date format. Please use DD-MM-YYYY.")
                        continue
                    date = date_input

                if self.manager.update_transaction(id, amount, category, date):
                    print(Fore.GREEN + f"Transaction {id} updated successfully!\n")
                    break 
                else:
                    print(Fore.RED + "Failed to update transaction.")
            except ValueError:
                print(Fore.RED + "Invalid Transaction ID format.")
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
        
         
            