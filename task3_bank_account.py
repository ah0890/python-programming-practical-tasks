# Task 3: Bank Account System using Object-Oriented Programming
# This program uses two classes:
#   - Customer : stores the customer's details
#   - Account  : stores the account details and handles transactions
# Each Account object contains a Customer object.


class Customer:
    """Represents a bank customer."""

    def __init__(self, name, customer_id):
        # Constructor: runs automatically when a Customer object is created
        self.name = name
        self.customer_id = customer_id

    def display_customer_info(self):
        print(f"Customer Name  : {self.name}")
        print(f"Customer ID    : {self.customer_id}")


class Account:
    """Represents a bank account that belongs to a customer."""

    def __init__(self, account_number, customer, balance=0):
        # Constructor: runs automatically when an Account object is created
        self.account_number = account_number
        self.customer = customer  # A Customer object stored inside the Account
        self.balance = balance

    def deposit(self, amount):
        # The deposit amount must be greater than zero
        if amount <= 0:
            print("Error: Deposit amount must be greater than zero.")
            return

        self.balance = self.balance + amount
        print(f"Success: Rs. {amount:,.2f} deposited.")

    def withdraw(self, amount):
        # The withdrawal amount must be greater than zero
        if amount <= 0:
            print("Error: Withdrawal amount must be greater than zero.")
            return

        # Cannot withdraw more money than the account has
        if amount > self.balance:
            print(f"Error: Insufficient balance. "
                  f"Available balance is Rs. {self.balance:,.2f}.")
            return

        self.balance = self.balance - amount
        print(f"Success: Rs. {amount:,.2f} withdrawn.")

    def display_balance(self):
        print(f"Current Balance: Rs. {self.balance:,.2f}")

    def display_account_info(self):
        # Uses the Customer object's method to show customer details
        self.customer.display_customer_info()
        print(f"Account Number : {self.account_number}")
        self.display_balance()


# ---------------------------------------------------------------
# Demonstration: creating objects and calling their methods
# ---------------------------------------------------------------

print("=" * 45)
print("          BANK ACCOUNT SYSTEM")
print("=" * 45)

# 1. Create a customer and an account for that customer
customer1 = Customer("Ali Khan", "C001")
account1 = Account("ACC-1001", customer1, 5000)

print("\n--- Account Created ---")
account1.display_account_info()

# 2. Deposit money
print("\n--- Deposit Rs. 2,500 ---")
account1.deposit(2500)
account1.display_balance()

# 3. Withdraw money
print("\n--- Withdraw Rs. 3,000 ---")
account1.withdraw(3000)
account1.display_balance()

# 4. Try to withdraw more than the available balance
print("\n--- Withdraw Rs. 10,000 (more than balance) ---")
account1.withdraw(10000)
account1.display_balance()

# 5. Try invalid (zero and negative) amounts
print("\n--- Deposit Rs. 0 (invalid amount) ---")
account1.deposit(0)

print("\n--- Withdraw Rs. -500 (invalid amount) ---")
account1.withdraw(-500)

# 6. Show the final account details
print("\n--- Final Account Details ---")
account1.display_account_info()
print("=" * 45)
