# Author: Émile
# Date: 2025-12-21
# But: faire fonctionner le programme

import logique_jeu
import nombre_hasard

NBR_ESSAI_TOTAL = 3 # le nombre d'essai pour trouver le nbr secret
NBR_SECRET = nombre_hasard.generer_nombre_secret(1, 100)
nbr_essai_restant = 0

while True:
    if logique_jeu.jouer(NBR_SECRET, NBR_ESSAI_TOTAL, True): break
