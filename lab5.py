l1 = ['abcd', 786, 2.23, 'ion', 70.2]

#slice - nimic dupa, ultima valoare - [interval) ca la matematica
print(l1[2:])

print(l1[-5])

print(l1[2:0])

#duplicarea elementelor
print(l1+l1)

l2 = [123, 14]
l3 = l1+l2
print(l3)

l1[1] = 'mod'
print(l1)

l4 = l2
print(l4)

print(l4==l2) # verificam daca au acelasi continut

print(l4 is l2) #verifica daca coincide regiunea de memorie utilizata

print(hex(id(l2)))

#liste cu aceleasi elemente
#for i in len(l2):
#   l4[i] = l2[i]

print(l4)

#se poat efolosi si metoda copy()

l5 = [1, 2.0, 'trei', 1+4j]
print(l5[0:2])

l5.insert(1,[7,7,7,7,7,7,7])
print(l5)

l5.insert(0, l5)
print(l5)

#stergerea elementelor
#l5 = []
l5.clear()
print(l5)

l6 = l1, l2, l5
print(l6)

l1 = 'ceva'
print(l1)
print(l6)
#lista este mutabila
#tuplul si constantele sunt imutabile

""" SORTAREA"""

l1 = [1, '2', '3']
#print(sorted(l1))
print(range(len(l1)))

for i in range(len(l1)):
    print(l1[i],end=" ")

print(enumerate(l1))

print(list(enumerate(l1))) # face un tuplu cu elementele lui l1 si indexul lor

for idx,val in enumerate(l1):
    print(val, end=" ")

l2 = [val*2 for val in[1,2,3]]

print(list(zip(l1,l2))) # tuplu de forma(l1[i],l2[i])

#tuplu
t1 = ('abcd', 786, 2.23, 'ion', 70.2)
print(len(t1))

t2 = tuple(l2)
print(t2)

#tuplurile pot fi sortate in anumite conditii

print(list(reversed(t2)))

print(tuple(reversed(l2)))

""" DICTIONARE"""
#o cheie poate fi si um tuplu

d_ro_en ={}
d_ro_en['carte'] = 'book'
print(d_ro_en)
d_ro_en = {'carte':'book', 'mar':'apple', 'masa':'table'}
print(d_ro_en.values())
print(list(d_ro_en.keys()))

print(dir(d_ro_en))

a = 5
while a<=47:
    if a % 2 != 0:
        print(a)
    a+=1
else:
    print("doar daca nu mai e indeplinita conditia din while")

"""FUNCTII"""
def even(a,b):
    while a<=b:
        if a % 2 != 0:
            print(a)
    a+=1

#functie cu input variabil
def suma(*vartuple):
    suma = 0
    for elem in vartuple:
        suma+=elem
    return suma
print(suma(1,1,2,5))


"""CITIREA DE DATE"""
var1 = input("Introduceti stringul: ")
print(var1)

var1,var2,var3 = input("Introduceti cuvintele: ").split()
print(var1,var2,var3)

