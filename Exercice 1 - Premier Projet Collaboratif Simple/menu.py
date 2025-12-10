# Date: 2025-12-08
# Auteur: Émile, Nadjib, Neil, Bruno
# But: Créer ensemble un "menu du restaurant" en Python

#----------------------Affiche les entrees du menu-----------------------------------------#
def afficher_entrees(): # Nadjib
    # Affiche la liste des entrées disponible dans le menu.
    print("Voici la liste des entrées: \n")
    entrees = [
        "1. Salade niçoise",
        "2. Soupe de tomate",
        "3. Tomate mozzarella"
    ]
    for plat in entrees:
        print(plat)

def afficher_plats_principaux(): # Neil
    pass

def afficher_desserts(): # Bruno
    pass

# Chef de projet / Git Master: Émile

def main(): 
    print("=== MENU DU RESTAURANT ===")
    # Les autres ajouteront leur code ici

if __name__ == "__main__":
    main()
