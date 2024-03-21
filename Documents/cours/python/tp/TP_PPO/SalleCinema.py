"""
TP sur les POO

Étudiant: Amine Hanafi

Exercie: Gestion d'une salle de cinema
"""

class SalleCinema:
    def __init__(self, capacite, places_speciales):
        self.places_disponibles = capacite
        self.reservations = []
        self.places_speciales = places_speciales

    #afficher le nombre de place disponible
    def nombre_places_disponibles(self):
        return self.places_disponibles

    #Pour  réserver une place, l'operation verfie qu'il reste des place avec une condition avant d'ajouter la nouvelle personne à la liste
    def reserver_place(self, nom, places):
        if places > self.places_disponibles:
            print("pas assez de places disponibles!")
        else:
            self.reservations.append({"nom": nom, "places": places})
            self.places_disponibles -= places
            print(f"Réservation effectuée pour {places} place(s) au nom de {nom}.")

    #à la rechereche d'une reservation, la variable reservations_personne prend une valeur si  on a trouvé une réservation pour cette personne
    # la condition suivant valide si cette variable  est vraie ou fausse pour faire l'affichage qui convient
    def filtrer_reservations_par_personne(self, nom):
        reservations_personne = []
    
        for reservation in self.reservations:
            if reservation["nom"] == nom:
                reservations_personne.append(reservation)
    
        if reservations_personne:
            print(f"Réservations de {nom} : {reservations_personne}")
        else:
            print(f"Aucune réservation trouvée pour {nom}.")

    #à l'annulation, une condition verifie si la reservation existe et incrimente les places si vrai
    #le 2eme teste verifie si annulation_effectuee est vraie ou fausse pour faire l'affichage qui convient
    def annuler_reservation(self, nom):
        annulation_effectuee = False

        for reservation in self.reservations:
            if reservation["nom"] == nom:
                self.places_disponibles += reservation["places"]
                self.reservations.remove(reservation)
                annulation_effectuee = True

        if annulation_effectuee:
            print(f"Réservations de {nom} annulées.")
        else:
            print(f"Aucune réservation trouvée pour {nom}.")

    #la reservation du place specialese 
    def reserver_place_speciale(self, nom):
        if self.places_speciales > 0:
            self.places_speciales -= 1
            self.reservations.append({"nom": nom, "places": 1, "speciale": True})
            print(f"Place spéciale réservée pour {nom}.")
        else:
            print("Désolé, il n'y a plus de places spéciales disponibles.")


salle = SalleCinema(capacite=50, places_speciales=5)

# Cette boucle sert à afficher au utilisateur les operations possible
while True:
    print("\nTapez 1 pour réserver une place normale.")
    print("Tapez 2 pour réserver une place spéciale.")
    print("Tapez 3 pour afficher le nombre de places disponibles.")
    print("Tapez 4 pour filtrer les réservations par personne.")
    print("Tapez 5 pour annuler les réservations d'une personne.")
    print("Tapez 6 pour quitter.")

    option = input("\nEntrez l'option choisie : ")

    if option == "1":
        nom_personne = input("Entrer le nom de la personne : ")
        places_reserver = int(input("Entrer le nombre de places à réserver : "))
        salle.reserver_place(nom_personne, places_reserver)
    elif option == "2":
        nom_personne_speciale = input("Entrer le nom de la personne pour la place spéciale : ")
        salle.reserver_place_speciale(nom_personne_speciale)
    elif option == "3":
        print(f"Nombre de places disponibles : {salle.nombre_places_disponibles()}")
    elif option == "4":
        nom_filtre = input("Entrer le nom de la personne pour filtrer les réservations : ")
        salle.filtrer_reservations_par_personne(nom_filtre)
    elif option == "5":
        nom_annulation = input("Entrer le nom de la personne pour annuler les réservations : ")
        salle.annuler_reservation(nom_annulation)
    elif option == "6":
        break
    else:
        print("Option invalide")
