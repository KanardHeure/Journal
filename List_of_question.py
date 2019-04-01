#! /usr/bin/env python3
# -*- coding: Utf-8 -*-

### IMPORT ###
from os import system
##############

### FUNCTION ###
def question():
    question = ["Bonjour, qu'as-tu fait aujourd'hui?", "Et comment c'est passé ta journée ?", "Sur une échelle de 1 à 10, à quel point tu t'es senti dépressif", "As-tu pleurer aujourd'hui ?", "Raconte moi ta journée."]
    reponse = []

    for item in question:
        system("cls")
        system("clear")
        print(item)
        reponse.append(input("\n"))
    return(question, reponse)
################