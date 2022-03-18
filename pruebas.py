from vertice import Vertice
from arista import Arista
from grafica import Grafica
import algoritmos

def main():
    # vértices
    v1 = Vertice("v1")
    v2 = Vertice("v2")
    v3 = Vertice("v3")
    v4 = Vertice("v4")

    # aristas
    a1 = Arista(v1, v2)
    a2 = Arista(v2, v3)
    a3 = Arista(v3, v4)
    a4 = Arista(v4, v1)

    # conjuntos de vértices
    vertices = [v1, v2, v3, v4]

    # conjunto de aristas
    aristas = [a1, a2, a3, a4]

    # Gráfica
    g = Grafica(vertices, aristas)

    assert g.vertices == vertices
    assert g.aristas == aristas

    g.adel(a1)
    aristas.remove(a1)

    assert g.vertices == vertices
    assert g.aristas == aristas

    g.vdel(v3)
    vertices.remove(v3)
    aristas.remove(a2)
    aristas.remove(a3)

    assert g.vertices == vertices
    assert g.aristas == aristas

    # graficables
    sg1 = [3, 3, 3, 3]
    sg2 = [0, 0, 0, 0, 0, 0, 0]
    sg3 = [3, 3, 2, 2]

    # no graficables
    sn1 = [5, 4, 3, 3, 2]
    sn2 = [7, 4, 4, 6, 5]
    sn3 = [3, 2, 4, 5, 6]

    assert algoritmos.havel_hakimi(sg1)
    assert algoritmos.havel_hakimi(sg2)
    assert algoritmos.havel_hakimi(sg3)

    assert not algoritmos.havel_hakimi(sn1)
    assert not algoritmos.havel_hakimi(sn2)
    assert not algoritmos.havel_hakimi(sn3)

if __name__ == '__main__':
    main()
