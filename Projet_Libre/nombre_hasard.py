# nombre_hasard.py (Nadjib)
"""
Génération du nombre secret pour le jeu
nombre compris entre 1 et 100 inclus

"""
import random

def generer_nombre_secret(minimum: int = 1, maximum: int = 100) -> int :

    if minimum >= maximum :
        raise ValueError("Le minimum doit être inferieur au maximum")

    return random.randint(minimum,maximum)
