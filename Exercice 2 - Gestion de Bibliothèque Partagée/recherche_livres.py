
def afficher_livres(livres):
    recherche_titre = "Harry Potter"
    print(f"\nRecherche par titre (contenant'{recherche_titre}')")
    trouve_titre = False
    for livre in livres:
        if recherche_titre.lower() in livre['titre'].lower():
            print(f"Titre: {livre['titre']}, Auteur: {livre['auteur']}, Année: {livre['annee']}")
            trouve_titre = True
    return trouve_titre