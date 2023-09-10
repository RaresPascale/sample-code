"""
FUNCTII IN PYTHON
"""

def add(a,b=4):
    return a+b

print(add(4,5))
print(add(4))

#se creeaza un tuplu


sum3 = 0 # Variabila globala

def add2(*vartuple):
    sum = 0
    print(locals())
    def fct2(a): # se creeaza o functie noua pt a avea o variabila enclosed
        sum2 = 0
        return a
    for i in vartuple:
        sum+=i
    return sum
print(add2(1,2,3,4,5))



#Citirea de la stdin

var1 = input("Introduceti valoarea pt var1: ")
print(var1)
