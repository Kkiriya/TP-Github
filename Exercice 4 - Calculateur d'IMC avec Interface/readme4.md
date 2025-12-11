## Exercice 4 : Calculateur d'IMC avec Interface

### Scénario 4

Créer un calculateur d'IMC avec différentes fonctionnalités

### Modules à Développer

**Membre 1 :** `calculs.py`
**-->** Nadjib

```python
def calculer_imc(poids, taille):
    # IMC = poids / taille²

def interpreter_imc(imc):
    # Retourne la catégorie
```

**Membre 2 :** `interface.py`
**-->** Neil

```python
def demander_infos():
    # Demande poids et taille

def afficher_resultat(imc, categorie):
    # Affiche joliment
```

**Membre 3 :** `historique.py`
**-->** Émile

```python
def sauvegarder_calcul(nom, imc):
    # Sauvegarde dans un fichier

def afficher_historique():
    # Lit le fichier
```

**Membre 4 :** `main.py` et tests
**-->** Bruno

```python
# Orchestre tout + tests unitaires
```

### Défis Avancés

1. Gérer les merge conflicts sur `main.py`
2. Utiliser Git Flow (branches feature/develop/main)
3. Faire des rebases pour garder l'historique propre

---
