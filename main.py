#! /usr/bin/env python
# -*- coding: Utf-8 -*-

# Etape 1 : Création d'un fichier txt portant le nom : journal de bord du mois de xxx année
#____Création d'un dossier Journal de bord et vérification qu'il existe
#____Regarde si il y a des fichier et si parmis les noms il y a celui du mois sinon création
# Etape 2 : Ecriture de la date dans le txt
#____Avec des espaces de façon à ce que ce soit claire
# Etape 3 : Demander à l'utilisateur ce qu'il à fait => Stocké la réponse // Demander son ressentie => stocké la réponse (console ou tkinter)
#____Système de note sur 5 pour chaque (pour voir une progression)
# Etape 4 : Enregistrement et fermeture du fichier
# Etape 5 : Rajouter les réponses au bout des questions si on relance le journal dans la même journée (voir à rajouter l'heure)
# Etape 6 : Réorganisation du code sur plusieurs fichier .py
# Etape 7 : Rajouter des questions et utiliser un peu d'aléatoire (tout en laissant des questions obligatoire)


from os import path
from os import getcwd
from os import mkdir
from os import chdir
from os import system
import sys
import datetime

curdir = path.dirname(__file__)
if len(curdir) == 0: curdir = getcwd()

if not path.exists(path.join(curdir,'Journal de bord')):
    mkdir(path.join(curdir,'Journal de bord'))
chdir(curdir + "/Journal de bord")

message = ["Bonjour, qu'as-tu fait aujourd'hui?", "Et comment c'est passé ta journée ?", "Sur une échelle de 1 à 10, à quel point tu t'es senti dépressif", "As-tu pleurer aujourd'hui ?"]
reponse = []
i = 0
date = datetime.date.today()

for item in message:
    system("cls")
    print(item)
    reponse.append(input("\n"))



liste_mois = ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Decembre"]
liste_mois_chiffre = [1,2,3,4,5,6,7,8,9,10,11,12]



for item in liste_mois_chiffre:
    if item == (date.month):
        nom_mois = liste_mois[(item-1)]

journal = open("Journal de " + nom_mois + " " + str(date.year) +".txt", 'a')
journal.write("Journal du " + str(date.day) + " " + nom_mois + " " + str(date.year) + "\n")
journal.write("\n")


for item in message:
    journal.write(item)
    journal.write("\n\t" + reponse[i] + "\n\n")
    i+= 1
journal.close()
sys.exit(0)
