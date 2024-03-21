"""
TP sur les POO

Étudiant: Amine Hanafi

Exercie: Gestion d'une liste de personne
"""

class ListePersonnes:
    # Module d'initialisation
    def __init__(self): 
        self.personnes = []

    # Module pour ajouter une personne
    def ajouter_personne(self, nom, age): 
        nouvelle_personne = {"nom": nom, "age": age}
        self.personnes.append(nouvelle_personne)

    # Module pour chercher une personne, l'operation va chercher  si la personne existe et affiche son age si il existe dans la liste 
    # sinon, un message va avertir l'utilisateur que la personne n'existe pas.
    def afficher_personnes(self, nom_recherche):
        personne_trouvee = None
        for personne in self.personnes:
            if personne["nom"] == nom_recherche:
                personne_trouvee = personne
                print(f"La personne {personne_trouvee['nom']} est dans la liste. Son age est {personne_trouvee['age']}.")
        if not personne_trouvee:
            print("Cette personne n'existe pas dans la liste.")

# Programme principal
liste = ListePersonnes()

# Cette boucle sert à afficher au utilisateur les operations possible
while True:
    print("\nTapez 1 pour ajouter une personne à la liste.")
    print("Tapez 2 pour chercher une personne.")
    print("Tapez 'q' pour quitter.")
    option = input("\nEntrez l'option choisie : ")

    if option == "1":
        liste.ajouter_personne(input("\nEntrer le nom de la personne : "), int(input("Entrer son age : ")))
    elif option == "2":
        nom_recherche = input("\nEntrer le nom de la personne recherchée : ")
        liste.afficher_personnes(nom_recherche)
    elif option == "q":
        break
    # si  l'utilisateur entre autre chose que ce qui est attendu, un message d'erreur d'affiche
    else:
        print("Option invalide.")
