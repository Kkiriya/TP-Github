#Calculs.py (nadjib)
"""
calcul de l'indice de masse corporelle (IMC) à partir du poids en kilogramme,et la taille en metre
IMC = poids / (taille²) ==> nombre réel arrondi à 2 decimal
Interprétation des résultat selon les catégorie OMS (adultes)

"""

def calculer_imc(poids: float, taille: float) -> float:
    """

    Calcule l'IMC à partir du poids (kg) et de la taille (m).

    """
    
    if poids <= 0 or taille <= 0 :
        raise ValueError("Le poids et la taille doivent etre positifs")
    
    return round(poids / (taille**2), 2) 


def interpreter_imc(imc: float) -> str:
    
    """
    Retourne la catégorie IMC selon les normes OMS

    """

    if imc <= 0:
        raise ValueError("IMC invalide")
    
    if imc < 18.5:
        return "Maigreur"
    elif imc < 25:
        return "Corpulence normale"
    elif imc < 30:
        return "Surpoids"
    elif imc < 35:
        return "Obésité modérée"
    elif imc < 40:
        return "Obésité sévère"
    else:
        return "Obésité morbide"