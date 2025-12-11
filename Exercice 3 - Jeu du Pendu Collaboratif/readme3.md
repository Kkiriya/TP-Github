## Exercice 3 : Jeu du Pendu Collaboratif

### Scénario 3

Développer un jeu du pendu en équipe

### Architecture du Projet

```txt
pendu/
├── mots.py          (Membre 1 : liste de mots)
├── affichage.py     (Membre 2 : affichage ASCII)
├── jeu.py           (Membre 3 : logique du jeu)
└── main.py          (Membre 4 : point d'entrée)
```

### Tâches Détail

**Membre 1 - `mots.py` :**
**-->** Neil

```python
def choisir_mot():
    mots = ["python", "programmation", "github", "collaboration"]
    # Retourner un mot aléatoire
```

**Membre 2 - `affichage.py` :**
**-->** Bruno

```python
def afficher_pendu(erreurs):
    # Dessins ASCII selon le nombre d'erreurs
```

**Membre 3 - `jeu.py` :**
**-->** Émile

```python
def jouer_tour(mot_secret, lettres_trouvees, lettre):
    # Logique du jeu
```

**Membre 4 - `main.py` :**
**-->** Nadjib

```python
# Importe tous les modules et orchestre le jeu
```

### Workflow Git

1. Chaque membre crée sa branche : `feature-mots`, `feature-affichage`, etc.
2. Chacun développe indépendamment
3. Merge progressif dans `develop`
4. Résolution des dépendances entre modules

---
