from Account import Account
from Operation import *

def main():
    cpte = Account("BNC", 500)
    print("Compte :", cpte.name)

    ope  = Operation("DEP","EPICERIE",25)
    ope.print_operation()
    cpte.add_operation(ope)
    bal = cpte.get_balance()
    print(bal)


if __name__ == "__main__":
    main()
