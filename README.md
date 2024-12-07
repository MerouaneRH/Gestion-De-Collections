# Noms et Prénoms avec adresses mails des membres du groupe:
- TOUBAL Rabah : rabah.toubal@etu.univ-orleans.fr
- GUILLARD Joan: joan.guillard@etu.univ-orleans.fr
- HAMZE Muhamad: muhamad.hamze@etu.univ-orleans.fr
- RAHMOUN Merouane: merouane.rahmoun@etu.univ-orleans.fr

## Commandes Question 01:

1. `USERNAME=$(basename $(id -un) @campus.univ-orleans.fr) USERID=$(id -u) docker-compose up -d`

2. `docker exec -ti fw1-cc-votre_nom_utilisateur whoami`

3. `django-admin startproject cc`

4. `python manage.py startapp collec_management`

5. `python manage.py runserver 0.0.0.0:8000 &`

## Commandes Question 02:

1. `python manage.py runserver 0.0.0.0:8000 &`

## Commandes Question 03:

1. `python manage.py makemigrations`

2. `python manage.py sqlmigrate collec_management 0001`

3.  `python manage.py migrate`

4. `python manage.py shell`

5. `from collec_management.models import Collec`

6. `from django.utils import timezone`

7. `c = Collec(title="test", description="Ceci est un test",date=timezone.now())`

8. `c.save()`

## Commandes Question 04:

1. `python manage.py makemigrations`

2. `python manage.py migrate`

3. `python manage.py loaddata collec_management/fixtures/examples.json`

4. `python manage.py shell`

5. `from collec_management.models import Collec`

6. `Collec.objects.all()`

## Commandes Question 05:

1. `python manage.py makemigrations`

2. `python manage.py migrate`

3. `python manage.py loaddata collec_management/fixtures/examples.json`

4. `python manage.py runserver 0.0.0.0:8000 &`

## Commandes Question 06:

1. `python manage.py makemigrations`

2. `python manage.py migrate`

3. `python manage.py loaddata collec_management/fixtures/examples.json`

4. `python manage.py runserver 0.0.0.0:8000 &`

## Commandes Question 07:

1. `python manage.py makemigrations`

2. `python manage.py migrate`

3. `python manage.py loaddata collec_management/fixtures/examples.json`

4. `python manage.py runserver 0.0.0.0:8000 &`

## Commandes Question 08:

1. `python manage.py makemigrations`

2. `python manage.py migrate`

3. `python manage.py loaddata collec_management/fixtures/examples.json`

4. `python manage.py runserver 0.0.0.0:8000 &`

## Commandes Question 09:

1. `python manage.py makemigrations`

2. `python manage.py migrate`

3. `python manage.py loaddata collec_management/fixtures/examples.json`

4. `python manage.py runserver 0.0.0.0:8000 &`

## Commandes Question 10:

1. `python manage.py makemigrations`

2. `python manage.py migrate`

3. `python manage.py loaddata collec_management/fixtures/examples.json`

4. `python manage.py runserver 0.0.0.0:8000 &`

##  Note: l'ajout de la date est automatique même si les données sont ajoutées dans le shell .

## Commandes question 11:

1.  `python manage.py createsuperuser`

2. `python manage.py runserver 0.0.0.0:8000 &`

3. `python manage.py makemigrations`

4. `python manage.py migrate`

## Commandes question 12:

1.  `python manage.py createsuperuser`

2. `python manage.py runserver 0.0.0.0:8000 &`

3. `python manage.py makemigrations`

4. `python manage.py migrate`


## Commandes question 13:
1.  `python manage.py loaddata collec_management/fixtures/examples.json`

2. `python manage.py makemigrations`

3. `python manage.py migrate`


## Commandes question 14:

1. `python manage.py runserver 0.0.0.0:8000 &`

## Commandes question 15:

1. `python manage.py makemigrations`

2. `python manage.py migrate`

3. `python manage.py loaddata collec_management/fixtures/examples.json`

4. `python manage.py runserver 0.0.0.0:8000 &`

## Commandes question 16:

1. `python manage.py makemigrations`

2. `python manage.py migrate`

3. `python manage.py loaddata collec_management/fixtures/examples.json`

4. `python manage.py runserver 0.0.0.0:8000 &`

## Commandes question 17:

1. `python manage.py makemigrations`

2. `python manage.py migrate`

3. `python manage.py loaddata collec_management/fixtures/examples.json`

4. `python manage.py runserver 0.0.0.0:8000`

