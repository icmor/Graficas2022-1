class Arista:

    # Método constructor de la clase arista
    def __init__(self, ex1, ex2):
        self.ex1 = ex1
        self.ex2 = ex2

    # Método que verifica si dos aristas son iguales (se llama asi: a1 == a2)
    def __eq__(self, other):
        return self.ex1 == other.ex1 and self.ex2 == other.ex2 \
            or self.ex1 == other.ex2 and self.ex2 == other.ex1

    # Método que verifica si v es un extremo de la arista (se llama asi: v in a)
    def __contains__(self, v):
        return v == self.ex1 or v == self.ex2

    #  Método que devuelve una representacion en cadena de arista al evaluar
    def __repr__(self):
        return f"Arista({self.ex1}, {self.ex2})"

    #  Método que devuelve una representacion en cadena de arista al imprimir
    def __str__(self):
        return str(self.ex1) + str(self.ex2)
