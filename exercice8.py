# Créé par thomas, le 02/05/2016 en Python 3.2
from lycee import*


def compteMots(ph):
    compteur = 0
    for ind in range (len(ph)):
        if (ph[ind] == " ") :
            compteur= compteur + 1
    compteur = compteur +1
    return compteur

print(compteMots("je suis une phrase"))

