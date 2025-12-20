def comparer(nombre_secret: int, proposition: int) -> str:
    """
    Compare la proposition au nombre secret.
    Retourne: "Trop petit", "Trop grand" ou "Gagné"
    """
    if proposition < nombre_secret:
        return "Trop petit"
    elif proposition > nombre_secret:
        return "Trop grand"
    else:
        return "Gagné"
