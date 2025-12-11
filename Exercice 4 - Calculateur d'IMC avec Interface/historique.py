# Author: Émile
# Date: 2025-12-11
# But: Sauvegarder le calcul imc et le nom de la personnne dans un fichier
#      Lire le fichier et afficher son contenue
import datetime
import os

# variable globale temporaire pour tester la fonction
IMC = 21.37
NOM = "John Bloodborne"
IMC2 = 25.23
NOM2 = "Bob Darksouls"


def sauvegarder_calcul(nom: "str", imc: "float") -> "str":
    """
    ### Docstring for sauvegarder_calcul\n
    **Sauvegarde le fichier:** *historique-PrenomNom.txt*\n
    **dans le path:** *./.txt/Nom-Prenom*\n
    **Sous le format suivant:** *Date: mois/jour/annee;	Nom: Prenom Nom;	IMC: 00.00*\n

    :param nom: String qui contient le nom complet du user
    :type nom: "str"
    :param imc: Float qui contient le resultat du calcul IMC
    :type imc: "float"
    :return: Message annoncant le success de la sauvegarde
    :rtype: str
    """
    # path qui contien le fichier de sauvegarde pour chaque users
    dirPath = f"./.txt/{nom.strip().replace(" ", '-')}" # → ex: ./.txt/John-Bloodborne

    # makedirs lance une erreur si le fichier existe deja le try permet d'a la fois verifier si le fichier existe et de le creer sinon
    try:
        os.makedirs(dirPath)
    except:
        pass

    date = datetime.datetime.now()
    path = dirPath + (f"/historique-{nom.lower().title().strip().replace(" ", '')}.txt")
    #full path → ex: ./.txt/John-Bloodborne/historique-JohnBloodborne.txt
    #Sauvegarde dans un fichier
    with open(path, "a") as f:
        #le open cherche a append un fichier avec le nom/path fournit, si il n'existe pas il le cree
        historique = f"Date: {date.strftime("%x")};\tNom: {nom.strip().lower().title()};\tIMC: {imc}\n"

        f.write(historique) #f.write append au fichier la ligne qui contient les donnnees a sauvegarder.
    return "Sauvegarder avec success!"


def afficher_historiquqe(nom: "str", doPrint: "bool" =True) -> "str":
    """
    ### Docstring for afficher_historiquqe
    Permet d'afficher l'historique d'un user spécifique\n
    Permet également de retourner l'historique en String\n
    \n**doPrint** = *True* → On imprimme, pas de retour de String \n
    **doPrint** = *False* → On n'imprime pas, retour de String

    :param nom: String contenant le nom de l'utilisateur rechercher
    :type nom: "str"
    :param doPrint: Bool permetant d'activer/desactiver l'impression et de retourner un String a la place (si l'impression est desactiver)
    :type doPrint: "bool"
    :return: retourne l'historique de l'utilisateur en String
    :rtype: str
    """
    historique = "" #permet de retourner l'historique en plus de l'imprimmer

    #Lit le fichier
    dirPath = f"./.txt/{nom.strip().replace(" ", '-')}" # → ex: ./.txt/John-Bloodborne
    path = dirPath + (f"/historique-{nom.lower().title().strip().replace(" ", '')}.txt")
    #full path → ex: ./.txt/John-Bloodborne/historique-JohnBloodborne.txt

    #ouvre le fichier et le lit ligne par ligne
    with open(path) as f:
        for lines in f:
            if doPrint:
                print(lines)
            historique += (lines + "\n")
    if(not doPrint):
        return historique

def main():
    #test de la fonction
    # sauvegarder_calcul(NOM, IMC)
    # sauvegarder_calcul(NOM2, IMC2)
    afficher_historiquqe(NOM)
    print("-----------------")
    print(afficher_historiquqe(NOM2, False))


if __name__ == "__main__":
    main()
