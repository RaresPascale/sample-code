for i in [1,2]:
    print("hello world")

# variabile in python
# Trenuie sa inceapa cu o litera sau _

var1 = 5
print()
print(hex(id(var1)))

var2 = var1 #o schimbare in var1 afecteaza si pe var2
print(hex(id(var2)))

#Tipul lui var1
print(type(var1))

# Metode valabile pt var1
print(dir(var1))

#protected un _
#private __ 2 underscore-uri

#Variante de printare
print(var1)

#Afiseaza concatenat
print("Text1",end=''); print("Text2")

print("Text1", "Text2", "Text3")

print("Text1", "Text2", "Text3",sep=";")

print("Variable is: ", var1)

print("Variable is: ", var1,sep='')

#F string
print(f"Variable is : {var1}")

print("Variable is: "+str(var1))

print("Variable is {},{}".format(var1,var1))

"""
Comentariu pe mai multe linii
fsdfsdfsd
fsdfsdfsd
sdfsfsd
"""







