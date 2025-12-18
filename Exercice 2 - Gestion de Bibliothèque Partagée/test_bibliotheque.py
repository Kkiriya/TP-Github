import livres

def test_ajouter_livre(): 
    livres.ajouter_livre("1984", "George Orwell")

    assert "1984" in livres.livres
    assert livres.livres["1984"] == "George Orwell"

def test_afficher_livres():
    livres.ajouter_livre("La Bibliothèque de Minuit", "Matt Haig")
    assert livres.afficher_livres() == "La Bibliothèque de Minuit, Matt Haig"

def test_rechercher_livre():
    livres.ajouter_livre("Harry Potter", "J.K. Rowling")

    assert livres.rechercher_livre("Harry") == "Harry Potter, J.K. Rowling"
    assert livres.rechercher_livre("Inconnu") == "Livre introuvable"

