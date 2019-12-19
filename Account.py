class Account:
    """ Class representing a bank account"""

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def display_balance(self):
        print(self.balance)

    def set_balance(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance
    
    def add_operation(self,Operation):
        self.balance  = self.balance + Operation.amount
        #print(self.balance)
