from vertice import vertice
from arista import arista
from grafica import grafica

#Main del programa
if __name__ == '__main__':
	
	#vertices
	v1 = vertice("v1")
	v2 = vertice("v2")
	v3 = vertice("v3")
	v4 = vertice("v4")

	#aristas
	a1 = arista(v1, v2)
	a2 = arista(v2, v3)
	a3 = arista(v3, v4)
	a4 = arista(v4, v1)

	#conjuntos de vertices
	vertices = [v1, v2, v3, v4]

	#conjunto de aristas
	aristas = [a1, a2, a3, a4]

	#Grafica
	g = grafica(vertices, aristas)
	
	#imprimimos
	print(str(g))








