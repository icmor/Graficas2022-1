#clase que modela un vertice
class vertice:

    #Metodo constructor de vertices
    def __init__(self, identificador, vecinos =[]):
        self.identificador = identificador
        self.vecinos = vecinos

    #Metodo que nos devuelva el grado de un vertice
    def get_grado(self):
        return len(self.vecinos)

    #Metodo que nos devuelve los vecinos de un vertice
    def get_vecinos(self):
        return self.vecinos

    #Metodo que nos devuelve el identificador de un vertice
    def get_id(self):
        return self.identificador

    #Metodo que nos dice si dos vertices son iguales
    def __eq__(self, v):
        if (self.identificador.__eq__(v.get_id())):
            return True
        else:
            return False

    #Metodo que nos devuelve una representacion en cadena de un vertice
    def __str__(self):
        return self.identificador
