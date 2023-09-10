class Test1:
    v_clasa = 0

    def __init__(self, name):
        #Variabila de instanta
        self.age = 0
        self.name = name
        self._v_protected = 0
        self.__v_private = 0

        Test1.v_clasa += 1


obj1 = Test1("O1")
print(f"Am creat {obj1.v_clasa} obiecte")

obj2 = Test1("O2")
print(f"Am creat {obj2.v_clasa} obiecte")

print(obj1.name)
print(obj1._v_protected)
print(obj1.__v_private)
print(obj1.Test1_)
