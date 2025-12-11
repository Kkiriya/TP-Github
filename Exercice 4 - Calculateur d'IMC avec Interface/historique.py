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
    # mkdir lance une erreur si le fichier existe deja le try permet d'a la fois verifier si le fichier existe deja et de le creer si il nexiste pas
    try:
        path = f"./.txt/{nom.strip().replace(" ", '-')}"
        print(path)
        os.makedirs(path)
    except:
        print("leak?")

    # date = datetime.datetime.now()
    # #Sauvegarde dans un fichier
    # with open(f"./txt/{nom.strip()}/historique-{nom.lower().title().strip()}.txt", "a") as f:
    #     f.write(f"{date.strftime("%x")}-{nom.replace(" ", "-").lower()}-{imc}")


def afficher_historiquqe():
    #Lit le fichier
    pass

def main():
    sauvegarder_calcul(NOM, IMC)

if __name__ == "__main__":
    main()
