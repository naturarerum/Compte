from Account import Account
from Operation import *

def main():
    cpte = Account("BNC", 500)
    print("Compte :", cpte.name)

    ope  = Operation("DEP","EPICERIE",25)


if __name__ == "__main__":
    main()
