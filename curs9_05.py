import os
import test1
# pwd in Linux - getcwd() din modulul os
print(os.getcwd())

print(os.listdir())


""" 
Terminologie POO

Metoda - functie definita in interiorul clasei
Variabile de instanta - atribute specifice unui obiect
obiectul este instanta unei clase

Mostenire - se mostenesc de la clasa parinte: metode si atribute
supraincarcarea functiilor - nu se poate face in python
supraincarcarea operatorilor - 
pass - o instructiune speciala(practic nu reprezinta nimic 
self - referinta catre sine <=> this in java

getattr()
hasattr() - verifica daca obj are atributul name
setattr() - se poat creea un atribut pentru un anumit obiect
delattr() - se sterge atributul

__dict__ - dictionar cu namespace-ul clasei
__doc__ - documentatia clasei

Garbage Collector - python curata memoria, cand referinta unui obiect este zero sau la 
                    apelarea functiei del
                    
__del()__ - destructor

Mostenirea

class SubClassName(ParentClass1):

o clasa copil poate sa suprascrie metodele si atributele clasei parinte

constructorul din clasa parinte trebuie apelat explicit
super().__init__(parent__attr)
ParentClass1.__init__(self,parent_attr) - cand sunt mai multe clase mostenite

!!!se pot suprascrie metodele clasi parinte, functionalitati built-in, operatori

in python toate metodele sunt publice

Protejarea variabilelor
sunt bdf publice

conventie de nume
un _attr la inceput - variabila protejata - se poate accesa din clasa si subclasele ei
doua __attr la inceput - variabila - accesabila doar in interiorul clasei
                        - se poate accesa din exteriorul clasei folosint obj.ClassName_attr

Fiecare variabila este obiect instanta a unei clase


"""

obj1 = test1.Test1("O1")
print(obj1)