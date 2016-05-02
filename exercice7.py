# Créé par Fenrir, le 02/05/2016 en Python 3.2
def inverse(ch):
    #Assignation de la longueur
    longueur = len(ch)
    #Assignation de i = longueur - 1 & chi = string vide
    i, chi = longueur-1, ""
    #Tant que i >= 0 retourner la derniere lettre
    while i >= 0:
        chi = chi + ch[i]
        i = i -1
    return chi

print(inverse('Sebastien'))