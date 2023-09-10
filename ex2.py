#Exercitiu din curs
#Cel cu dictionarea

d_ro_en = {'carte':'book','mar':'apple','masa':'table'}

#Cerinta 1 - printarea lui
print(d_ro_en)

#Printarea cheilor
print(dir(d_ro_en)) # pentru a vedea ce metode putem folosi
print(d_ro_en.keys())

print(list(d_ro_en.keys()))

#Valorile din dictionar
print(d_ro_en.values())
print(list(d_ro_en.values()))

for i in list(d_ro_en.values()):
    print(i)


#primul cubant - cautarea se face pe baza de cheie
print()
print(d_ro_en['carte'])

print(d_ro_en.get('doi'))

#Crearea unui nou dictionar
d_md_en = d_ro_en

#Verificare logica
print(d_md_en is d_ro_en)

print(hex(id(d_ro_en)))
print(hex(id(d_md_en)))

d_md_en = d_ro_en.copy()


print(d_md_en.pop('carte'))
print(d_md_en)

del d_md_en

#Dictionary comprehension
#Asa am adaugat doi si two in dictionar
d_md_en={key:d_ro_en[key] for key in list (d_ro_en.keys())}
print(d_md_en)

d_md_en={key:d_ro_en.get(key) for key in ['mar', 'masa', 'doi']}
print(d_md_en)
d_md_en['doi'] = 'two'
print(d_md_en)




