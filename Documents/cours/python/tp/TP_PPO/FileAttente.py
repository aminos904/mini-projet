"""
TP sur les POO

Étudiant: Amine Hanafi

Exercie: Gestion d'une liste d'attente
"""

class FileAttente:
    def __init__(self):
        self.attente_normale = []
        self.attente_prioritaire = []

    def ajouter_personne_en_attente(self, nom):
        self.attente_normale.append(nom)

    def ajouter_personne_prioritaire(self, nom):
        self.attente_prioritaire.append(nom)

    def supprimer_personne_de_attente(self):
        if self.attente_prioritaire:
            personne_supprimee = self.attente_prioritaire.pop(0)
            print(f"La personne prioritaire {personne_supprimee} a été retirée de la file d'attente.")
        elif self.attente_normale:
            personne_supprimee = self.attente_normale.pop(0)
            print(f"La personne {personne_supprimee} a été retirée de la file d'attente.")
        else:
            print("La file d'attente est vide.")
    
    def afficher_file_attente(self):
        print("File d'attente prioritaire :", self.attente_prioritaire)
        print("\nFile d'attente normale :", self.attente_normale)


# Programme principal
file_attente = FileAttente()

while True:
    print("\nTapez 1 pour ajouter une personne normale à la file d'attente.")
    print("Tapez 2 pour ajouter une personne prioritaire à la file d'attente.")
    print("Tapez 3 pour supprimer une personne de la file d'attente.")
    print("Tapez 4 pour afficher la liste d'attente.")
    print("Tapez 'q' pour quitter.")
    
    option = input("Entrez l'option choisie : ")

    if option == "1":
        nom_personne = input("Entrer le nom de la personne normale : ")
        file_attente.ajouter_personne_en_attente(nom_personne)
    elif option == "2":
        nom_personne_prioritaire = input("Entrer le nom de la personne prioritaire : ")
        file_attente.ajouter_personne_prioritaire(nom_personne_prioritaire)
    elif option == "3":
        file_attente.supprimer_personne_de_attente()
    elif option == "4":
        file_attente.afficher_file_attente()

    elif option == "q":
        break
    else:
        print("Option invalide.")
