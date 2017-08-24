#Implementacion de grafo en matriz

import numpy

class digraphAM:

    def __init__(self,size):
        self.size = size
        self.matriz = numpy.zeros(shape=(size+1,size+1))

    def add_arc(self,source,destination,weight=1):
        self.matriz[source,destination]=weight

    def get_successors(self,vertex):
        successors=[]
        for i in range(self.size):
            if self.matriz[vertex,i] != 0:
                successors.append (i)
        return successors

    def get_weight(self,source,destination):
        return self.matriz[source][destination]

