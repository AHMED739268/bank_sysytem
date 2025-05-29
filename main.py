

import sys
from bank_system import BankSystem


def main():
    """Main function to run the bank management system"""
    try:
        # Create and run the bank system
        bank_system = BankSystem()
        bank_system.run()

    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()