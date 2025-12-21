# Author: Émile
# Date: 2025-12-17
# But: Sauvegarder le calcul imc et le nom de la personnne dans un fichier
#      Lire le fichier et afficher son contenue
import datetime
import os

class Historique():
    #path vers le dir contenant, les dossier de chaque user
    DIRPATH = "../.txt/"

    # makedirs lance une erreur si le fichier existe deja le try permet d'a la fois verifier si le fichier existe et de le creer sinon
    try:
        os.makedirs(DIRPATH)
    except:
        pass

    def __init__(self, name: str, imc: float) -> None:
        self.nom = name
        self.imc = imc
        self.DATE = datetime.datetime.now()

        #Make the folder where user data is saved
        self.FOLDERPATH = f"{self.DIRPATH}{self.nom.strip().replace(" ", '-')}/"

        try:
            os.makedirs(self.FOLDERPATH)
        except:
            pass

        #Path ou l'on se trouve les fichiers sauvegarder
        self.FILEPATH = f"{self.FOLDERPATH}historique-{self.nom.lower().title().strip().replace(" ", '')}.txt" #full path → ex: ./.txt/John-Bloodborne/historique-JohnBloodborne.txt

    def sauvegarder_calcul(self) -> str:
        """
        ### Docstring for sauvegarder_calcul\n
        **Sauvegarde le fichier:** *historique-PrenomNom.txt*\n
        **dans le path:** *./.txt/Nom/*\n
        **Sous le format suivant:** *Date: mois/jour/annee;	Nom: Prenom Nom;	IMC: 00.00*\n

        :param nom: String qui contient le nom complet du user
        :type nom: "str"
        :param imc: Float qui contient le resultat du calcul IMC
        :type imc: "float"
        :return: Message annoncant le success de la sauvegarde
        :rtype: str
        """
        #sauvegarde dans le fichier
        with open(self.FILEPATH, "a") as f:
            #le open cherche a append un fichier avec le nom/path fournit, si il n'existe pas il le cree
            historique = f"Date: {self.DATE.strftime("%x")};\tNom: {self.nom.strip().lower().title()};\tIMC: {self.imc}\n"

            f.write(historique) #f.write append au fichier la ligne qui contient les donnnees a sauvegarder.
        return "Sauvegarder avec success!"

    def afficher_historique(self, doPrint: "bool" = False) -> str:
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
        with open(self.FILEPATH) as f:
            for lines in f:
                if doPrint: print(lines)
                historique += (lines + "\n")
            return historique

    def get_nom(self) -> str:
        return self.nom

    def get_imc(self) -> float:
        return self.imc

    def set_imc(self, imc: float) -> None:
        self.imc = imc

    def __str__(self):
        return f"Path: {self.FILEPATH} \nName: {self.nom} \nIMC: {self.imc}"

def main():
    # variable temporaire pour tester la fonction
    IMC = 21.37
    NOM = "John Bloodborne"
    IMC2 = 25.23
    NOM2 = "Bob Darksouls"

    # test de la classe et de ses methode
    historique_John = Historique(NOM, IMC)
    historique_Bob = Historique(NOM2, IMC2)
    # print(historique_John)
    # print(historique_Bob)

    historique_John.sauvegarder_calcul()
    historique_Bob.sauvegarder_calcul()

    historique_John.afficher_historique(True)
    print("*"*40)
    historique_Bob.afficher_historique(True)

if __name__ == "__main__":
    main()
