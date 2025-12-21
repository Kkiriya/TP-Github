def comparer(nombre_secret: int, proposition: int) -> str:
    """
    Compare la proposition au nombre secret.
    Retourne: "Trop petit", "Trop grand" ou "Gagné"
    """
    if proposition < nombre_secret:
        print("Trop petit")
        return "Trop petit"
    elif proposition > nombre_secret:
        print("Trop grand")
        return "Trop grand"
    else:
        print("Gagné")
        return "Gagné"
