# Author: Émile
# Date: 2025-12-11
# But: Sauvegarder le calcul imc et le nom de la personnne dans un fichier
#      Lire le fichier et afficher son contenue
import datetime
import os

#variable globale temporaire pour tester la fonction
IMC = 21.37
NOM = "John Bloodborne"

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
    with open(f"{path}/historique-{nom.lower().title().strip()}.txt", "a") as f:
        #le open cherche a append un fichier avec le nom/path fournit, si il n'existe pas il le cree
        f.write(f"{date.strftime("%x")};{nom.replace(" ", "-").lower()};{imc}") #f.write append au fichier la ligne qui contient les donnnees a sauvegarder.


def afficher_historiquqe():
    #Lit le fichier
    pass

def main():
    sauvegarder_calcul(NOM, IMC)

if __name__ == "__main__":
    main()
