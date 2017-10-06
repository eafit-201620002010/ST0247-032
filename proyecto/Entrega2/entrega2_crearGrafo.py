"""
@clase entrega2_crearGrafo
Descripcion: Construccion del grafo
@author Mateo Ramirez H. / Juan Camilo Echeverri S.
@version 2
"""
from collections import defaultdict

class entrega2_crearGrafo:

    def __init__(self):
    	self.grafo=defaultdict(dict)

    def crear_grafo(self):
         with open("arcos.txt") as f:
            for line in f:
                a=line.split(" ")
                #opcion: int(round(float(a[2])))
                self.grafo[a[0]][a[1]] = float(a[2])



grafo=entrega2_crearGrafo()
grafo.crear_grafo()
