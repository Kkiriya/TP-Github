# Author: Émile
# Date: 2025-12-20
# But: affichage pour le jeu du pendu

#f"{''.join(mot)} | vie: {nbr_vie}/{VIE} | (a-z): {essai}"

def affichage(mot: str, vie_restante: int, vie_totale: int, lettre_entrer: str):
    """
    Docstring for affichage

    :param mot: String contenant toutes les lettre trouver
    :type mot: str
    :param vie_restante: Int representant le nbr de vie restante
    :type vie_restante: int
    :param vie_totale: Int representant le nbr de vie Totale
    :type vie_totale: int
    :param lettre_entrer: String contenant la lettre deviner par le joueur
    :type lettre_entrer: str
    """
    print(f"{mot} | vie: {vie_restante}/{vie_totale} | (a-z): {lettre_entrer}")

def main():
    mot = "__tt_t_"
    vie_restante = 2
    vie_totale = 5
    lettre_entrer = 'a'
    affichage(mot, vie_restante, vie_totale, lettre_entrer)

if __name__ == "__main__":
    main()
