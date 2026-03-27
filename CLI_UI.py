from Features import CashFlow
from colorama import Fore, Style, init
import sys

# Initialize colorama
init(autoreset=True)    

class UI(CashFlow):
    def display_header(self):
        title = "💸 Cash Flow CLI 💸"
        print(Fore.CYAN + " " + "=" * 50)
        print(Fore.CYAN + "|" + " " * 50 + "|")
        print(f"{Fore.CYAN}|{Style.RESET_ALL} {Fore.YELLOW}{title.center(46)}{Style.RESET_ALL} {Fore.CYAN}|{Style.RESET_ALL}")
        print(Fore.CYAN + "|" + " " * 50 + "|")
        print(Fore.CYAN + " " + "=" * 50)
        print("\n")

    def display_UI(self):
        while True:
            self.display_header()
            print("1. " + Fore.GREEN + "Add a new income" + Style.RESET_ALL)
            print("2. " + Fore.GREEN + "Add a new expense" + Style.RESET_ALL)
            print("3. " + Fore.BLUE + "View all transactions" + Style.RESET_ALL)
            print("4. " + Fore.BLUE + "Search for a transaction" + Style.RESET_ALL)
            print("5. " + Fore.RED + "Delete a transaction" + Style.RESET_ALL)
            print("6. " + Fore.MAGENTA + "Update a transaction" + Style.RESET_ALL)
            print("7. " + Fore.MAGENTA + "View summary report" + Style.RESET_ALL)
            print("0. " + Fore.RED + "Exit" + Style.RESET_ALL)
            
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
                    self.view_summary_report()
                case '0':
                    print(Fore.GREEN + "Thank you for using the Cash Flow CLI!" + Style.RESET_ALL)
                    sys.exit()
                case _:
                    print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)