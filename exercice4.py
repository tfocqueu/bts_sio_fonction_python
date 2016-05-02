# Créé par thomas, le 26/04/2016 en Python 3.2
from lycee import *

def compteCar(ca,ch):
    compteur= 0
    for ind in range (len(ch)):
        if (ca.lower() == ch[ind].lower()):
            compteur=compteur+1
    return compteur

print (compteCar("S","cccCsure"))







