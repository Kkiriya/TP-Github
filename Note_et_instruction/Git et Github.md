### Commandes de base: 
**Demarer:**<br>
`git init` --> Initialiser un nouveau repo <br>
`git status` --> voir l'etat actuel du repo<br>
`git add fichier.py` --> ajouter un fichier au repo<br>
`git add .` --> ajouter tous les fichiers au repo<br>

**Sauvegarder:**<br>
`git commit -am "message"` --> creer un commit<br>
`git log` --> voir lhistorique de commit<br>
`git log --oneline` --> historique condenser<br>
`git diff` --> voir les modif apporter<br>

### Manipuler les branches:
**Creer et Naviguer:**<br>
`git branch` --> listes les branches<br>
`git banch nom-branche` --> creer une branche<br>
`git checkout nom-branche` --> basculer sur la branche<br>
`git checkout -b nom-branche` --> creer et bascule la branche<br>

**Fusionner et Supprimer:**<br>
`git checkout main` --> retourner sur main<br>
`git merge nom-branche` -->  fusionne dans main<br>
`git branch -d nom-branche` --> supprime la branche si fusionner<br>
`git branch -D nom-branche` --> force la suppression de la branche<br>

### Strategies de branches:<br>

| Git flow                             | Github flow                   |
| ------------------------------------ | ----------------------------- |
| `main`: Code en production           | `main`: Toujours deployable   |
| `develop`: Integration des features  | Creer une branche par feature |
| `feature`: Nouvelles fonctionnalités | Commits regulier + push       |
| `release`: Preparation des versions  | Ouvrir une pull request       |
| `hotfix`: corrections urgentes       | review + discussion           |
|                                      | merge dans main               |

### Github et Collab

**Configuer un remote:**<br>
`git remote add origin [URL]` --> ajoute un remore nommer *origin*<br>
`git remote -v` --> voir les remotes configurer<br>
`git remote remove origin` --> supprime un remote<br>

**Clone un Repo (pour collaboration ou simplement avoir les fichier)**<br>
`git clone [URL]` --> clone le repo et tous ses fichier<br>
`git clone [URL] .` --> clone le repo dans le repertoire courant sans creer un nouveau repertoire<br>

**Synchroniser:**<br>
`git push -u origin main` --> envoyer + definir upstream (-u)<br>
`git pull origin main` --> recuper + fusionner<br>
`git fetch origin` --> recuperer sans fusionner<br>
