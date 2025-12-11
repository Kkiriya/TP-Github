# Author: Émile
# Date: 2025-12-11
# But: Contient la logique du jeux pour un tour seulement

#variables globale temporaire pour tester
# mot_secret = "pattate"
# lettres_trouvees = "_" * len(mot_secret)
# lettre = 't'

def jouer_tour(mot_secret: "str", lettres_trouvees: "str", lettre: "str")-> "str":
    """
    Docstring for jouer_tour

    :param mot_secret: String contenant le mot secret que le joueur doit deviner
    :type mot_secret: "str"
    :param lettres_trouvees: String contenant toute les lettre deviner par le jouer
    :type lettres_trouvees: "str"
    :param lettre: String contenant la lettre deviner par le joueur
    :type lettre: "str"
    :return: Version updated de lettres_trouvees, ou un message d'erreur approprier
    :rtype: str
    """
    #strip et lower pour reduire les errerus de frappe
    mot_secret = mot_secret.lower().strip()
    lettre = lettre.lower().strip()
    lettres_trouvees = list(lettres_trouvees) #transforme le string en liste pour pouvoir remplacer les les lettres

    if 'a' <= lettre <= 'z': #verifie si la lettre fait partie de l'alphabet
        if lettre in mot_secret: #verifie si la lettre fait partie du mot_secret
            for idx, l in enumerate(mot_secret): #check chaque lettre qui correspond et remplace le "_" par celle-ci
                if l == lettre:
                    lettres_trouvees[idx] = l
        else:
            return "La Lettre ne fait pas partie du mot"
    else:
        return "ERREUR: LETTRE NON VALIDE"

    return "".join(lettres_trouvees)

def main():

    #test de la fonction
    mot_secret = "pattate"
    #print(jouer_tour(mot_secret,lettres_trouvees, lettre))
    print(jouer_tour(mot_secret, "_______", "t"))
    print(jouer_tour(mot_secret, "__tt_t_", "a"))
    print(jouer_tour(mot_secret, "_attat_", "p"))
    print(jouer_tour(mot_secret, "pattat_", "e"))

if __name__ == "__main__":
    main()
