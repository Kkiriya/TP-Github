#Main.py (nadjib)

import calculs
import interface
from historique import Historique


def main():
    # 1. Demande des infos utilisateur
    nom, poids, taille = interface.demander_donnees()

    # 2. Calcul IMC
    imc = calculs.calculer_imc(poids, taille)
    categorie = calculs.interpreter_imc(imc)

    # 3. Affichage du résultat
    interface.afficher_resultat(imc, categorie)

    # 4. Sauvegarde dans l'historique
    h = Historique(nom, imc)
    message = h.sauvegarder_calcul()
    print(message)


if __name__ == "__main__":
    main()
