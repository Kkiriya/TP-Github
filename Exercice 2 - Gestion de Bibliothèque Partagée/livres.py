# Date: 2025-12-08
# Auteur: Émile, Nadjib, Neil, Bruno
# But: Créer un système de gestion de livres collaboratif

# Structure initiale
bibliotheque = [
    {"titre": "Harry Potter", "auteur": "JK Rowling"},
    {"titre": "1984", "auteur": "George Orwell"},
    {"titre": "Supermarket", "auteur": "Bobby Hall" },
    {"titre": "Tant que le café est encore chaud", "auteur": "Toshikazu Kawaguchi"},
    {"titre": "La Bibliothèque de Minuit", "auteur": "Matt Haig" },
    {"titre": "Le Passager", "auteur" : "Patrick Senécal"},
    {"titre": "Les Sept Jour du talion","auteur": "Patrick Senécal"}
]

def ajouter_livre(titre, auteur): # Émile
    if (titre.strip() != '') and (auteur.strip()!= ''):
        bibliotheque.append({"titre:": titre, "auteur": auteur})
        print("livre ajouter!")
    else:
        print("Input invalide!")

def afficher_livres():
    print("\n---Liste des livres disponible---\n")
    for i, livre in enumerate(bibliotheque, start=1):
        print(f"{i}. {livre['titre']} ({livre['auteur']})")

def rechercher_livre(titre): # Bruno
    pass

def main():
    #test de la fonction ajouter
    ajouter_livre("Test", "Blank")
    print(bibliotheque)

if __name__ == "__main__":
    main()
