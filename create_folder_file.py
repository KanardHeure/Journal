#! /usr/bin/env python3
# -*- coding: Utf-8 -*-

### IMPORT ###
from os import path
from os import getcwd
from os import mkdir
from os import chdir
import datetime
##############

### FUNCTION ###
def create_directory():
    curdir = getcwd()
    if not path.exists(path.join(curdir,'Journal de bord')):
        mkdir(path.join(curdir,'Journal de bord'))
    chdir(curdir + "/Journal de bord")

def create_journal_file(question, reponse):
    date = datetime.date.today()
    liste_mois = ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Decembre"]
    nom_mois = liste_mois[date.month - 1]

    journal = open("Journal de " + nom_mois + " " + str(date.year) +".txt", 'a')
    journal.write("Journal du " + str(date.day) + " " + nom_mois + " " + str(date.year) + "\n")
    journal.write("\n")
    i = 0

    for item in question:
        journal.write(item)
        journal.write("\n\t" + reponse[i] + "\n\n")
        i+= 1
    journal.close()
################