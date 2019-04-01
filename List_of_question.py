#! /usr/bin/env python3
# -*- coding: Utf-8 -*-

### IMPORT ###
from os import system
##############

### FUNCTION ###
def question(mode):
    if mode == True:
        question = ["Bonjour, qu'as-tu fait aujourd'hui?", "Et comment c'est passé ta journée ?", "Sur une échelle de 1 à 10, à quel point tu t'es senti dépressif", "As-tu pleurer aujourd'hui ?"]
    else:
        question = ["Raconte moi ta journée !"]
    reponse = []

    for item in question:
        system("cls")
        system("clear")
        print(item)
        reponse.append(input("\n"))
    return(question, reponse)

def select_Mode():
    print("Souhaites tu répondre à des question ou être en mode autonome ?")
    print("1 - Question")
    print("2 - Mode autonome")
    answer = input("Votre choix ? ")
    if answer == '1':
        mode = True
    else:
        mode = False
    return(mode)

################