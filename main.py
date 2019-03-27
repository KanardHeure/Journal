#! /usr/bin/env python3
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

### IMPORT ###
import sys
import create_folder_file as cff
import List_of_question as Loq
##############

cff.create_directory()
message, reponse = Loq.question()
cff.create_journal_file(message, reponse)
sys.exit(0)
