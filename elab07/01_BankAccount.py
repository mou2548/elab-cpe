class BankAccount():
    def __init__(self, accountID="0000", balance=0):
        self.accountID = accountID
        self.balance = balance

    def set_account_ID(self, newID):
        self.accountID = newID

    def set_balance(self, new_balance):
        self.balance = new_balance
    
    def get_account_ID(self):
        return self.accountID
    
    def get_balance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdrawal(self, amount):
        self.balance -= amount
    
    def __str__(self):
        accountID = self.get_account_ID()
        balance = self.get_balance()
        output_format = f"ID: {accountID}, Balance: {balance:.2f}"
        return output_format