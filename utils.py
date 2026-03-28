from tabulate import tabulate
from colorama import Fore, Style, init
from datetime import datetime

# initial colorama
init(autoreset=True)

class ValidationError:
    """Custom exception for validation errors."""
    def amountValidation(self, amount):
        if amount is not None and amount <= 0:
            return False
        return True
        
    def dateValidation(self, date):
        if date is not None:
            try:
                datetime.strptime(date, "%d-%m-%Y")
            except ValueError:
                return False
        return True
            
    def categoryValidation(self, category):
        if len(category) <= 2 or not category.replace(" ", "").isalpha():
            return False
        return True


class InputData:
    def __init__(self):
        """Class to handle user input and validation."""
        self.validator = ValidationError()
        
    def takeInputData(self):
        print(Fore.CYAN + "Press Enter to use today's date, or enter a date (DD-MM-YYYY).")
        while True:
            date = input("Date (DD-MM-YYYY): ").strip()
            if not date:
                date = datetime.now().strftime("%d-%m-%Y")
                print("Date: " + Fore.GREEN + date)
                break
            elif not self.validator.dateValidation(date):
                print(Fore.RED + "Invalid date format. Please use DD-MM-YYYY.")
                continue
            break
        while True:
            try:
                amount_input = input("Amount: ").strip()
                amount = float(amount_input)
                if not self.validator.amountValidation(amount):
                    print(Fore.RED + "Amount cannot be zero or negative!")
                    continue
                break
            
            except ValueError:
                print(Fore.RED + "Invalid amount. Please enter a number.") 
        return date, amount
        
        