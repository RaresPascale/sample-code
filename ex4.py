#Exercitiu cu liste

l1 = [1,2, '3', '4']
l2 = l1

print(l1 ==l2)
print(l1 is l2)

#Nu se mai afla in aceeasi regiune de memorie
l2 = l1.copy()
print(l2 is l1)

#
l2 = [n*2 for n in [1,2,3]]
print(l2)

#Exemplu pt while loop in python

a = 5 - 1
while a < 7 - 1:
    a +=1
    if a == 6:
        pass
        #break #break termina bucla si ne duce dupa bucla
        #continue
    print(a)
else:
    print("Bucla completa")
print("while s-a terminat")

# parcurgerea unei liste
l1 = [ 1, 2, 3]
for i in l1:
    print(i)

print()
l1 = [0,3,5]
for i in l1:
    print(i)

#Parcurgem cu indecsii
print()
for i in range(len(l1)):
    print(i,l1[i])

#Parcurgere dn 2 in 2
print()
for i in range(0,len(l1),2):
    print(i,l1[i])

# Enumerare
print()
for idx,val in enumerate(l1):
    print(idx)

#Merge intre 2 liste
l1 = [1,2,3]
l2 = [4,5,6]

zip(l1,l2)
for v1,v2 in zip(l1,l2):
    print(v1,v2)


for i in sorted(l1):
    print(i)


l1.append(14)
print(l1)

l1.pop(3)
print(l1)

tpl = ( 'abcd', 786 , 2.23, 'john', 70.2 )
print(tpl)