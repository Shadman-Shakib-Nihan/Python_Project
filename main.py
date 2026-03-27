from CLI_UI import UI

def main():
    
    """Main entry point of the application."""
    display = UI()
    
    try:
        display.display_UI()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user. Stay safe!")
        
if __name__ == "__main__":
    main()