import random

liste_mots = [
    "python",
    "ordinateur",
    "clavier",
    "souris",
    "programmation",
    "github",
    "variable",
    "collaboration"
]
def choisir_mot():
    """Retourne un mot aléatoire depuis la liste."""
    return random.choice(liste_mots)