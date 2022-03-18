# Clase que modela una gráfica
class Grafica:

    # Método constructor de la clase
    def __init__(self, vertices, aristas):
        self.vertices = vertices.copy()
        self.aristas = aristas.copy()
        for a in self.aristas:
            a.ex1.vecinos.append(a.ex2)
            a.ex2.vecinos.append(a.ex1)

    # Método que elimina vértices de la gráfica
    def vdel(self, *args):
        for v in args:
            self.vertices.remove(v)
            for aux in self.vertices:
                if v in aux.vecinos:
                    aux.vecinos.remove(v)
            eliminadas = []
            for a in self.aristas:
                if v in a:
                    eliminadas.append(a)
            for a in eliminadas:
                self.aristas.remove(a)

    # Método que elimina una arista
    def adel(self, *args):
        for a in args:
            self.aristas.remove(a)
            for v in self.vertices:
                if v == a.ex1:
                    v.vecinos.remove(a.ex2)
                elif v == a.ex2:
                    v.vecinos.remove(a.ex1)

    # Método que nos devuelve una representación en cadena de gráfica al evaluar
    def __repr__(self):
        v = "[" + ", ".join(str(v) for v in self.vertices) + "]"
        a = "[" + ", ".join(str(a) for a in self.aristas) + "]"
        return f"Grafica({v}, {a})"

    # Método que nos devuelve una representacion en cadena de gráfica al imprimir
    def __str__(self):
        # representar en cadena el conjunto de vértices
        v = "{" + ", ".join(str(v) for v in self.vertices) + "}"

        # representar en cadena el conjunto de aristas
        a = "{" + ", ".join(str(a) for a in self.aristas) + "}"

        return f"El conjunto de vértices es: {v}\nEl conjunto de aristas es: {a}"

