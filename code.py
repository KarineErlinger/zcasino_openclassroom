# -*-coding:Latin-1 -*
import os
from random import randrange
from math import ceil

mise_total = 1000
partie = True

print("Votre argent:", mise_total, "$")

while partie:
    nbr_mise = -1
    while nbr_mise < 0 or nbr_mise > 49:
        nbr_mise = input("Choissez votre numéro: ")
        try:
            nbr_mise = int(nbr_mise)
        except ValueError:
            print("Vous n'avez pas saisi de nombre")
            nbr_mise = -1
            continue
        if nbr_mise < 0:
            print("Ce nombre est négatif")
        if nbr_mise > 49:
            print("Ce nombre est supérieur à 49")
            
    mise = 0            
    while mise <= 0 or mise > mise_total:
        mise = input("Tapez le montant de votre mise : ")
        try:
            mise = int(mise)
        except ValueError:
            print("Vous n'avez pas saisi de nombre")
            mise = -1
            continue
        if mise <= 0:
            print("La mise saisie est négative ou nulle.")
        if mise > mise_total:
            print("Vous ne pouvez miser autant, vous n'avez que", mise_total, "$")
    

    tirage = randrange(50)
    print("Le tirage est:", tirage)



    if tirage == nbr_mise:
        print("Jackpot!", mise * 3, "$")
        mise_total += mise * 3
    elif tirage %2 == nbr_mise %2:
        mise = ceil(mise * 0.5)
        print("Bravo, vous gagnez:", mise, "$")
        mise_total += mise
    else:
        print("Perdu!")
        mise_total -= mise
    

 # On interrompt la partie si le joueur est ruiné
    if mise_total <= 0:
        print("Vous êtes ruiné ! C'est la fin de la partie.")
        partie = False
    else:
        # On affiche l'argent du joueur
        print("Vous avez à présent", mise_total, "$")
        quitter = input("Souhaitez-vous quitter le casino (o/n) ? ")
        if quitter == "o" or quitter == "O":
            print("Vous quittez le casino avec vos gains.")
            partie = False

os.system("pause")
