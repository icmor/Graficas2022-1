#Clase que modela una grafica
class grafica:

    #Metodo constructor de la clase
    def __init__(self, vertices, aristas):
        self.vertices = vertices
        self.aristas = aristas
        for v in self.vertices:
            for a in self.aristas:
                if(a.get_ex1().__eq__(v)):
                    v.vecinos.append(a.get_ex2())
                elif(a.get_ex2().__eq__(v)):
                    v.vecinos.append(a.get_ex1())

    #Metodo que nos devuelve una representacion en cadena de una grafica
    def __str__(self):
        #representar en cadena el conjunto de vertices      
        vert = "{"
        for v in self.vertices:
            vert = vert + ", " + v.__str__()
        vert = vert + "}"   
        
        #representar en cadena el conjunto de vertices
        arist = "{"
        for a in self.aristas:
            arist = arist + ", " + a.__str__()
        arist = arist + "}"
        
        return "El conjunto de vertices es: " + vert + "\n" + "El conjunto de aristas es: " + arist
    
    #Metodo que elimina un vertice de la grafica
    def elimina_v(self, v):
        self.vertices.remove(v)
        for aux in self.vetices:
            if (v in aux.vecinos):
                aux.vecinos.remove(v)
        eliminadas = []
        for a in self.aristas:
            if(a.get_ex1().__eq__(v) or a.get_ex2().__eq__(v)):
                eliminidas.append(a)
        for a2 in eliminadas:
            self.aristas.remove(a2)

    #Metodo que elimina una arista
    def elimina_a(self, a):
        self.aristas.remove(a)
        for v in self.vertices:
            if(v__eq__(a.get_ex1())):
                v.vecinos.remove(a.get_ex2())
            elif(v__eq__(a.get_ex2())):
                v.vecinos.remove(a.get_ex1())




