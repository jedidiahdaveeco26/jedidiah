class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Adds money to the balance."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deducts money if the balance is sufficient."""
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def display_balance(self):
        """Displays the account balance."""
        print(f"Account balance: {self.balance}")


# Creating a bank account
account1 = BankAccount("124231100", "Jedidiah Dave", 5000)
    
# Performing transactions
account1.deposit(1000)      # Depositing money
account1.withdraw(2500)     # Withdrawing money
account1.withdraw(1100)    # Trying to withdraw more than balance

# Displaying the balance
account1.display_balance()