import comparaison_nbr
import user_input

def jouer(NBR_SECRET: int, NBR_ESSAI_TOTAl: int, DEBUG_MODE: bool):
    if DEBUG_MODE: print(f"Deviner le nombre secret ({NBR_SECRET}): ")
    else: print(f"Deviner le nombre secret: ")

    input = user_input.get_secret_number()

    resultat = comparaison_nbr.comparer(NBR_SECRET, input)

    match resultat:
        case "Trop petit":
            return False
        case "Trop grand":
            return False
        case "Gagné":
            return True
