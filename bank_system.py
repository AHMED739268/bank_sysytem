"""
Bank Management System - Core business logic
"""

import hashlib
from sqlalchemy.exc import SQLAlchemyError
from models import User, get_session


class BankSystem:
    """Main bank management system class"""

    def __init__(self):
        self.session = get_session()
        self.current_user = None

    def hash_password(self, password):
        """Hash password for security"""
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self):
        """Register a new user"""
        print("\n=== User Registration ===")
        try:
            name = input("Enter your name (max 20 characters): ").strip()[:20]
            if not name:
                print("Name cannot be empty!")
                return

            email = input("Enter your email (max 50 characters): ").strip()[:50]
            if not email:
                print("Email cannot be empty!")
                return

            # Check if email already exists
            existing_user = self.session.query(User).filter(User.email == email).first()
            if existing_user:
                print("Email already registered! Please use a different email.")
                return

            password = input("Enter your password: ").strip()
            if not password:
                print("Password cannot be empty!")
                return

            # Create new user with hashed password
            hashed_password = self.hash_password(password)
            new_user = User(
                name=name,
                email=email,
                password=hashed_password,
                balance=0.0
            )

            self.session.add(new_user)
            self.session.commit()
            print("Registration successful! You can now login.")

        except SQLAlchemyError as e:
            print(f"Database error occurred: {e}")
            self.session.rollback()
        except Exception as e:
            print(f"An error occurred: {e}")

    def login_user(self):
        """Login existing user"""
        print("\n=== User Login ===")
        try:
            email = input("Enter your email: ").strip()
            password = input("Enter your password: ").strip()

            if not email or not password:
                print("Email and password cannot be empty!")
                return False

            # Hash the entered password for comparison
            hashed_password = self.hash_password(password)

            # Find user in database
            user = self.session.query(User).filter(
                User.email == email,
                User.password == hashed_password
            ).first()

            if user:
                self.current_user = user
                print(f"Login successful! Welcome, {user.name}!")
                return True
            else:
                print("Invalid email or password!")
                return False

        except SQLAlchemyError as e:
            print(f"Database error occurred: {e}")
            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def show_profile(self):
        """Display user profile information"""
        if not self.current_user:
            print("No user logged in!")
            return

        print("\n=== User Profile ===")
        print(f"ID: {self.current_user.id}")
        print(f"Name: {self.current_user.name}")
        print(f"Email: {self.current_user.email}")
        print(f"Age: Not specified")  # Placeholder as mentioned in requirements
        print(f"Password: {self.current_user.password}")  # For demonstration purposes only
        print(f"Account Balance: ${self.current_user.balance:.2f}")

    def show_balance(self):
        """Display current account balance"""
        if not self.current_user:
            print("No user logged in!")
            return

        # Refresh user data from database to get latest balance
        self.session.refresh(self.current_user)
        print(f"\n=== Account Balance ===")
        print(f"Current Balance: ${self.current_user.balance:.2f}")

    def process_loan(self):
        """Process loan request and add to balance"""
        if not self.current_user:
            print("No user logged in!")
            return

        print("\n=== Loan Request ===")
        try:
            loan_amount = float(input("Enter the loan amount: $"))

            if loan_amount <= 0:
                print("Loan amount must be positive!")
                return

            # Add loan amount to current balance
            self.current_user.balance += loan_amount

            # Save updated balance to database
            self.session.commit()

            print(f"Loan of ${loan_amount:.2f} approved and added to your account!")
            print(f"New balance: ${self.current_user.balance:.2f}")

        except ValueError:
            print("Please enter a valid numeric amount!")
        except SQLAlchemyError as e:
            print(f"Database error occurred: {e}")
            self.session.rollback()
        except Exception as e:
            print(f"An error occurred: {e}")

    def post_login_menu(self):
        """Display and handle post-login menu options"""
        while True:
            print("\n=== Bank Menu ===")
            print("1) Profile")
            print("2) Balance")
            print("3) Loans")
            print("4) Logout")

            choice = input("Select an option (1-4): ").strip()

            if choice == "1":
                self.show_profile()
            elif choice == "2":
                self.show_balance()
            elif choice == "3":
                self.process_loan()
            elif choice == "4":
                print("Logging out...")
                self.current_user = None
                break
            else:
                print("Invalid option! Please select 1, 2, 3, or 4.")

    def main_menu(self):
        """Display and handle main menu options"""
        while True:
            print("\n=== Bank Management System ===")
            print("1) Login")
            print("2) Register")
            print("3) Exit")

            choice = input("Select an option (1-3): ").strip()

            if choice == "1":
                if self.login_user():
                    self.post_login_menu()
            elif choice == "2":
                self.register_user()
            elif choice == "3":
                print("Thank you for using Bank Management System. Goodbye!")
                self.cleanup()
                return False
            else:
                print("Invalid option! Please select 1, 2, or 3.")

    def cleanup(self):
        """Clean up database session"""
        if self.session:
            self.session.close()

    def run(self):
        """Start the bank management system"""
        try:
            print("Welcome to the Bank Management System!")
            self.main_menu()
        except KeyboardInterrupt:
            print("\n\nApplication interrupted by user.")
            self.cleanup()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            self.cleanup()