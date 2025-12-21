def jouer(nombre_secret, max_tentatives, demander_nombre, comparer):
    tentatives = 0

    while tentatives < max_tentatives:
        print(f"Tentative {tentatives + 1} / {max_tentatives}")

        nombre_joueur = demander_nombre()
        resultat = comparer(nombre_joueur, nombre_secret)

        if resultat == "gagné":
            print("Gagné !")
            return

        elif resultat == "trop petit":
            print("Trop petit")

        elif resultat == "trop grand":
            print("Trop grand")

        tentatives += 1

    print("Perdu ! Nombre maximum de tentatives atteint.")
    print("Le nombre secret était :", nombre_secret)
