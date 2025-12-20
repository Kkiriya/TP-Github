# main.py (nadjib)
# Orchestre les fichiers ; affichage.py , jeu.py , mots.py

from mots import choisir_mot
from jeu import jouer_tour
from affichage import affichage


def main():
    # 1. Initialisation du jeu
    mot_secret = choisir_mot()
    lettres_trouvees = "_" * len(mot_secret)

    VIE_TOTALE = 6
    vie_restante = VIE_TOTALE
    lettre_entrer = ""

    print("=== JEU DU PENDU ===")

    # 2. Boucle principale du jeu
    while vie_restante > 0 and "_" in lettres_trouvees:
        affichage(lettres_trouvees, vie_restante, VIE_TOTALE, lettre_entrer)

        lettre_entrer = input("Entrez une lettre : ").strip().lower()

        resultat = jouer_tour(mot_secret, lettres_trouvees, lettre_entrer)

        # Si jouer_tour retourne un message d'erreur
        if resultat in [
            "La Lettre ne fait pas partie du mot",
            "ERREUR: LETTRE NON VALIDE"
        ]:
            print(resultat)
            vie_restante -= 1
        else:
            lettres_trouvees = resultat

    # 3. Fin du jeu
    if "_" not in lettres_trouvees:
        print(f"\nBravo ! Vous avez gagné ! Le mot était : {mot_secret}")
    else:
        print(f"\nPerdu ! Le mot était : {mot_secret}")


if __name__ == "__main__":
    main()
