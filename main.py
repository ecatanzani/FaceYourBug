"""Main file"""
import sys
from supervisor import Dian0Supervisor

def main():
    """Main function to show usage example"""
    # Create an instance of the custom exception handler
    custom_excepthook = Dian0Supervisor()
    # Set the custom exception handler as the excepthook
    sys.excepthook = custom_excepthook

    # Usage example
    hfdjshfk # One sample error

if __name__ == '__main__':
    main()
