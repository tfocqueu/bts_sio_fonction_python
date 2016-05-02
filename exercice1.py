# Créé par thomas, le 26/04/2016 en Python 3.2
from lycee import *

def maximum(n1,n2,n3):
    if (n1>= n2 and n1>=n3):
        return (n1)
    if (n2>= n1 and n2>=n3):
        return (n2)
    if (n3>= n2 and n3>=n1):
        return (n3)

print (maximum(5,4,10))