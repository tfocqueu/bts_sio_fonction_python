# Créé par thomas, le 02/05/2016 en Python 3.2

from lycee import *
def indexmax(liste):
        index=0
        compteur = 0
        maxnb=liste[0]

        for ind in liste:
                if ind>maxnb:
                        maxnb=ind

        while index!=maxnb:
                index=liste[compteur]
                compteur =compteur + 1
        compteur = compteur - 1

        return compteur


liste=[1,5,99,1,22,44,160,12]
print(indexmax(liste))