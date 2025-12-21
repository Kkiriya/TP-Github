import livres

def test_ajouter_livre():
    print("TEST ajouter_livre")
    livres.ajouter_livre("1984", "George Orwell")
    livres.ajouter_livre("Harry Potter", "J.K. Rowling")


def test_afficher_livres():
    print("\nTEST afficher_livres")
    livres.afficher_livres()


def test_rechercher_livre():
    print("\nTEST rechercher_livre (existant)")
    livres.rechercher_livre("1984")

    print("\nTEST rechercher_livre (inexistant)")
    livres.rechercher_livre("Inconnu")


def main():
    test_ajouter_livre()
    test_afficher_livres()
    test_rechercher_livre()


if __name__ == "__main__":
    main()
