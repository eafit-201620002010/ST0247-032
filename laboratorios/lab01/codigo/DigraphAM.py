import numpy
"""
    @clase digraphAl
    Descripcion: implementacion de grafo con matrices.
    @author Mateo Ramirez H. / Juan Camilo Echeverri S.
    @version 1.2
"""

class digraphAM:

    def __init__(self,size):
        self.size = size
        #Creo una matriz con el numero de columnas y filas igual a la cantidad de vertices y la lleno de ceros
        self.matriz = numpy.zeros(shape=(size+1,size+1))


    def add_arc(self,source,destination,weight=1):
    	#Agrego un peso entre en el vertice de origen(columna cero) y el vertice destino(fila cero)
        self.matriz[source,destination]=weight


    def get_successors(self,vertex):
    	#Creo una lista
        successors=[]
        #Recoro todos los vertices de la fila cero
        for i in range(self.size):
        	#Si el vertice especificado tiene un peso diferente de 0 con el vertice de la fila significa que hay un arco entre dichos
            if self.matriz[vertex,i] != 0:
            	#Agrego el vertice con el que se encontro el arco a la lista
                successors.append (i)
        #retorno la lista
        return successors


    def get_weight(self,source,destination):
    	#Retorno el peso que se encuentra en la posicion de la matriz dada por ambos vertices
        return self.matriz[source][destination]

