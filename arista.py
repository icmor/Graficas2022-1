#Clase que modela una arista
class arista:

    #Metodo constructor de la clase arista
    def __init__(self, extremo1, extremo2):
        self.extremo1 = extremo1
        self.extremo2 = extremo2

    #Metodo que devuelve el primer extremo
    def get_ex1(self):
        return self.extremo1

    #Metodo que devuelve el segundo extremo
    def get_ex2(self):
        return self.extremo2

    #Metodo que verifica si dos aristas son iguales
    def __eq__(self, a1):
        if (self.extremo1.__eq__(a1.get_ex1()) and self.extremo2.__eq__(a1.get_ex2())):
            return True
        elif (self.extremo1.__eq__(a1.get_ex2()) and self.extremo2.__eq__(a1.get_ex1())):
            return True
        else:
            return False

    #Metodo que devuelve una representacion en cadena de una arista
    def __str__(self):
        return str(self.extremo1) + str(self.extremo2)











