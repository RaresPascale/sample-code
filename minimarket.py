import sys


class Produs:

    def __init__(self,nume,pret):
        self.nume = str(nume)

        if pret <= 0:
            sys.exit("Valoare invalida")

        self.pret = float(pret)



class Punga(Produs):

    def __init__(self, nume, pret, greutate):

        super().__init__(nume, pret)

        if float(greutate) > 0:
            self.greutate = float(greutate)
        else:
            sys.exit("Valoare invalida")



if __name__ == '__main__':

    nume,pret,greutate = input().split()
    pret = float(pret)
    greutate = float(greutate)

    punga1 = Punga(nume,pret,greutate)

    nume,pret,greutate = input().split()
    pret = float(pret)
    greutate1 = float(greutate)

    punga2 = Punga(nume,pret,greutate)

    pret_total = punga1.pret * punga1.greutate + punga2.pret*punga2.greutate
    print ("Pret total la casa: {:.2f}".format(pret_total))
    punga2.pret = 9.99
    punga1.greutate = 1.0
    pret_total = punga1.pret * punga1.greutate + punga2.pret*punga2.greutate
    print ("Pret total la casa: {:.2f}".format(pret_total))
