# Author: Émile
# Date: 2025-12-11
# But: Sauvegarder le calcul imc et le nom de la personnne dans un fichier
#      Lire le fichier et afficher son contenue
import datetime
import os

#variable globale temporaire pour tester la fonction
IMC = 21.37
NOM = "John Bloodborne"
IMC2 = 25.23
NOM2 = "Bob Darksouls"


def sauvegarder_calcul(nom, imc):
    # path qui contien le fichier de sauvegarde pour chaque users
    path = f"./.txt/{nom.strip().replace(" ", '-')}" # → ex: .txt/John-Bloodborne

    # makedirs lance une erreur si le fichier existe deja le try permet d'a la fois verifier si le fichier existe deja et de le creer si il nexiste pas
    try:
        os.makedirs(path)
    except:
        pass

    date = datetime.datetime.now()
    #Sauvegarde dans un fichier
    with open(f"{path}/historique-{nom.lower().title().strip().replace(" ", '')}.txt", "a") as f:
        #le open cherche a append un fichier avec le nom/path fournit, si il n'existe pas il le cree
        historique = f"Date: {date.strftime("%x")};\tNom: {nom.strip().lower().title()};\tIMC: {imc}\n"

        f.write(historique) #f.write append au fichier la ligne qui contient les donnnees a sauvegarder.


def afficher_historiquqe():
    #Lit le fichier
    pass

def main():
    #test de la fonction
    sauvegarder_calcul(NOM, IMC)
    sauvegarder_calcul(NOM2, IMC2)

if __name__ == "__main__":
    main()
