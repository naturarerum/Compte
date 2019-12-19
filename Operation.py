class Operation:
    """represents an operation on an account"""

    def __init__(self,date_ope,optype,category,amount):
        self.optype = optype
        self.category=category
        self.amount=amount
        self.date_ope = date_ope
    
    """ def print_operation(self):
        print(self.date_ope,self.optype,self.category,self.amount) """
