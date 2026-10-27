from account import Account
from transaction import Transaction

class SavingsAccount(Account):
    def __init__(self, account_number, owner_name, balance=0, interest_rate=0.01, min_balance=100):
        # TODO: Call parent constructor with account_number, owner_name, and balance
        super().__init__(account_number, owner_name, balance)
        # TODO: Store interest_rate as self.interest_rate (default 0.01)
        self.interest_rate = interest_rate
        # TODO: Store min_balance as self.min_balance (default 100)
        self.min_balance = min_balance

    def withdraw(self, amount):
        # TODO: Validate that amount is positive (> 0)
        # TODO: If invalid, return (False, "Withdrawal amount must be positive")
        # TODO: Check if withdrawal would go below minimum balance
        # TODO: If below min_balance, return (False, f"Cannot withdraw below minimum balance of ${self.min_balance:.2f}")
        # TODO: Subtract amount from self.balance
        # TODO: Create Transaction object with "withdrawal", amount, and self
        # TODO: Append transaction to self.transaction_history
        # TODO: Return (True, f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        if amount <= 0:
            return (False, "Withdrawal amount must be positive")
        if self.balance - amount < self.min_balance:
            return (False, f"Cannot withdraw below minimum balance of ${self.min_balance:.2f}")
        self.balance -= amount
        transaction = Transaction("withdrawal", amount, self)
        self.transaction_history.append(transaction)
        return (True, f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
    #Message: Transfer failed: Cannot withdraw below minimum balance of $100.00
    
    def apply_interest(self):
        # TODO: Calculate interest as self.balance * self.interest_rate
        # TODO: Add interest to self.balance
        # TODO: Create Transaction object with "interest", interest amount, and self
        # TODO: Append transaction to self.transaction_history
        # TODO: Return (True, f"Applied interest: ${interest:.2f}. New balance: ${self.balance:.2f}")
        interest = self.balance * self.interest_rate
        self.balance += interest
        transaction = Transaction("interest", interest, self)
        self.transaction_history.append(transaction)
        return (True, f"Applied interest: ${interest:.2f}. New balance: ${self.balance:.2f}")