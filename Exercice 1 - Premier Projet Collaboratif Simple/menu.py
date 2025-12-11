# Date: 2025-12-08
# Auteur: Émile, Nadjib, Neil, Bruno
# But: Créer ensemble un "menu du restaurant" en Python

def afficher_entrees(): # Nadjib
    # Affiche la liste des entrées disponible dans le menu.
    print("\n--- Entrées ---")

    entrees = [
        "Salade niçoise",
        "Soupe de tomate",
        "Tomate mozzarella"
        ]

    for plat in entrees:
        print(plat)

def afficher_plats_principaux(): # Neil
    print("\n--- Plats Principaux ---")

    plats = [
        "Steak frites",
        "Pâtes carbonara",
        "Poulet grillé"
        ]

    for plat in plats:
        print(plat)

# updated desserts, food
def afficher_desserts(): # Bruno
    print("\n---Desserts---")

    desserts = [
        "gateau fraise",
        "gateau chocolat",
        "gateau vanille"
        ]

    for d in desserts:
        print(d)

# Chef de projet / Git Master: Émile
def main():
    print("=== MENU DU RESTAURANT ===")
    # Les autres ajouteront leur code ici
    afficher_entrees()
    afficher_plats_principaux()
    afficher_desserts()

if __name__ == "__main__":
    main()
