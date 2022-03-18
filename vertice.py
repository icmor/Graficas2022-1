class Vertice:

    # Método constructor
    def __init__(self, identificador, vecinos = None):
        self.identificador = identificador
        if not vecinos:
            self.vecinos = []
        else:
            self.vecinos = vecinos

    # Devuelve el grado de un vértice y se obtiene como cualquier otro atributo
    @property
    def grado(self):
        return len(self.vecinos)

    # Método que nos dice si dos vértices son iguales
    def __eq__(self, other):
       return self.identificador == other.identificador

    # Método que nos devuelve una representacion en cadena de un vértice al evaluar
    def __repr__(self):
        return f"Vertice('{self.identificador}')"

    # Método que nos devuelve una representacion en cadena de un vértice al imprimir
    def __str__(self):
        return self.identificador
