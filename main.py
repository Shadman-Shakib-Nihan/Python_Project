from CLI_UI import CashFlow

def main():
    
    """Main entry point of the application."""
    display = CashFlow()
    
    try:
        display.display_features()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user. Stay safe!")
        
if __name__ == "__main__":
    main()