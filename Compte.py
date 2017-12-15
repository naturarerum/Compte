class Compte:
    """ Classe représentant un compte bancaire"""

    def __init__(self, nom):
        self.nom = nom
        self.solde = 0.0

    def afficher_solde(self):
        print(self.solde)
        return

    def effectuer_retrait(self, montant):
        self.solde -= montant
        return

    def effectuer_depot(self, montant):
        self.solde += montant
        return
