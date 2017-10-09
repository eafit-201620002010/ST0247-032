"""
@clase entrega2_crearGrafo
Descripcion: Construccion del grafo
@author Mateo Ramirez H. / Juan Camilo Echeverri S.
@version 3
"""
from collections import defaultdict

class entrega2_crearGrafo:

    def __init__(self):

    	#Creo un diccionario.
    	self.grafo=defaultdict(dict)

    #Creo el grafo con el diccionario
    def crear_grafo(self):

    	#"with" abre el archivo y lo cierra al acabar.
         with open("arcos.txt") as f:

         	#Leo linea por linea
            for line in f:

            	#Creo una lista que almacena cada elemento de la linea separado por espacios.
            	#Nota: la posicion '0' de la lista almacena el vertice inicial, la posicion '1' el vertice adyacente,
            	#la posicion '2' el peso del arco y la posicion '3' el nombre del arco.
                a=line.split(" ")

                #Cada llave de mi diccionario representa un vertice y contienen otro diccionario.
                #Las llaves de estos segundos diccionarios son los vertices adyacentes y contienen el peso del arco.
                #Ejemplo: grafo = {'v1': {'v2': 10, 'v3': 23}}.
                self.grafo[a[0]][a[1]] = float(a[2])


