import calculs
import historique

def demander_donnees():
    """Demande le poids et la taille à l'utilisateur."""
    try:
        nom = input("Entrez votre nom : ").strip()
        poids = float(input("Entrez votre poids (kg): "))
        taille = float(input("Entrez votre taille (m): "))
        return  nom, poids, taille
    
    except ValueError:
        print("Erreur : veuillez entrer des nombres valides.")
        return demander_donnees()

def afficher_resultat(imc, categorie):
    """Affiche l'IMC et sa catégorie."""
    print(f"\nVotre IMC est : {imc:.2f}")
    print(f"Catégorie : {categorie}")


def lancer_interface():
    """Gère toute la logique d'interface du calculateur IMC."""
    poids, taille = demander_donnees()
    imc = calculs.calculer_imc(poids, taille)

    afficher_resultat(imc)
    historique.sauvegarder_imc(imc)

    print("\nIMC enregistré dans l'historique.")
