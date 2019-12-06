class Operation:
    """represents an operation on an account"""

    def __init__(self,optype,category,amount):
        self.optype = optype
        self.category=category
        self.amount=amount
    
    def print_operation(self):
        print(self.optype,self.category,self.amount)
