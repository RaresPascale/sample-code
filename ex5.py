var = 5

if type(var) is int and var >=5:
    print("Numar mai mare sau egal decat 5")
elif type(var) is str:
    print("String")
elif type(var) is int and var<5:
    print("Mai mic decat 5")
else:
    print("Altceva")


a = 5
b = True
c = 'None'
d = None

print(a and b)
print(a and c)
e = 0
f = ""
print(bool(f))

print(a or b)


string = "hello world"
print(string.capitalize())

l_fructe = ['mere', 'pere', 'nuci' ]
l_pret = [10,14,15]

print()
for fruct, pret in zip(l_fructe,l_pret):
    print(fruct.capitalize(), ":", pret, "lei/kg", sep="")