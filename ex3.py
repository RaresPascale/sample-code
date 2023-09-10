import cmath

unu = 3
doi = 3.2
trei = 1 + 1j
patru = 'George'
cinci = "5"

""" 3.1 TIPURI DE DATE """
print(type(unu))
print(type(doi))
print(type(trei))
print(type(patru))

""" 3.2 """
print()
print(unu + doi)
print(patru + cinci) # concatenarea celor doua stringuri

""" 3.3 """
print()
print(unu*3)
print(unu**unu) #unu ridicat la puterea unu
print(patru*3) #string-ul scris de 3 ori

""" 3.4 """
print()
print(patru + str(doi))


""" 3.5 """
print()
help(patru)
#help(str)

""" 3.6 """
print()
print(type(int(cinci)))
print(type(complex(cinci)))
print(type(float(cinci)))