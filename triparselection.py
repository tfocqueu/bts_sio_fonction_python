# Créé par thomas, le 03/05/2016 en Python 3.2
from lycee import*

def triselection(tb,n):
    nbmax=tb[0]
    indicemax = 0
    for ind in range (len(tb)):
        if nbmax < tb[ind]:
            nbmax = tb[ind]
            indicemax = ind

    tb[indicemax],tb[n-1] = tb[n-1],nbmax

#6,3,5,2,3,7

    nbmax = tb[0]
    indicemax = 0
    for ind in range (len(tb)-1):
        if nbmax < tb[ind]:
            nbmax = tb[ind]
            indicemax = ind
    tb[indicemax],tb[n-2] = tb[n-2],nbmax

#3,3,5,2,6,7
    nbmax = tb[0]
    indicemax = 0
    for ind in range (len(tb)-2):
        if nbmax < tb[ind]:
            nbmax = tb[ind]
            indicemax = ind
    tb[indicemax],tb[n-3] = tb[n-3],nbmax
#3,3,2,5,6,7
    nbmax = tb[0]
    indicemax = 0
    for ind in range (len(tb)-3):
        if nbmax < tb[ind]:
            nbmax = tb[ind]
            indicemax = ind
    tb[indicemax],tb[n-4] = tb[n-4],nbmax
#2,3,3,5,6,7
    nbmax = tb[0]
    indicemax = 0
    for ind in range (len(tb)-4):
        if nbmax < tb[ind]:
            nbmax = tb[ind]
            indicemax = ind
    tb[indicemax],tb[n-5] = tb[n-5],nbmax
#2,3,3,5,6,7

    return tb
print(triselection([6,3,7,2,3,5],6))