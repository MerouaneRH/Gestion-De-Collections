# Gestion de Collections et d'Éléments 🗂️

Ce projet est une application web développée avec **Django** pour la gestion de collections et des éléments qui y sont rattachés. Il permet de consulter, ajouter, modifier et supprimer des collections et des éléments, avec des fonctionnalités d'authentification et de gestion des autorisations.

---

## Fonctionnalités 🚀

- **Gestion des Collections** : Ajout, modification, suppression et consultation des collections.
- **Gestion des Éléments** : Ajout, modification, suppression et consultation des éléments rattachés aux collections.
- **Authentification** : Connexion et déconnexion des utilisateurs.
- **Gestion des Autorisations** :
  - Les utilisateurs ne peuvent accéder qu'aux collections et éléments qu'ils ont créés.
  - Les utilisateurs non authentifiés ne peuvent que consulter la liste des collections.
- **Interface Utilisateur** : Améliorée avec **Bootstrap** pour une meilleure expérience utilisateur.

---

## Structure du Projet 🗂️

- **cc** : Projet Django principal.
- **collec_management** : Application Django pour la gestion des collections et des éléments.
- **README.md** : Fichier contenant les informations sur le projet et les commandes utilisées.
- **cc/**, **collec_management/**, **manage.py** : Structure de base du projet Django.

---

## Installation et Utilisation 🛠️

### Prérequis

- **Python**
- **Django**
- **Docker**

### Commandes Utiles

1. **Lancer le conteneur Docker** :
   ```bash
   USERNAME=$(id -un) USERID=$(id -u) docker-compose up -d
   ```

2. **Vérifier l'utilisateur dans le conteneur** :
   ```bash
   docker exec -ti fw1-cc-votre_nom_utilisateur whoami
   ```

3. **Créer les migrations** :
   ```bash
   python manage.py makemigrations
   ```

4. **Appliquer les migrations** :
   ```bash
   python manage.py migrate
   ```

5. **Charger les données des collections** :
   ```bash
   python manage.py loaddata collec_management/fixtures/examples.json
   ```

6. **Lancer le serveur Django** :
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

---

## Équipe 👥

- **GUILLARD Joan**
- **HAMZE Muhamad**
- **TOUBAL Rabah**
- **RAHMOUN Merouane**


---

Ce projet a été réalisé dans le cadre du cours **Framework Web 1** à l'**Université d'Orléans**.
