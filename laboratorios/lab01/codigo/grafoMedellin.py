"""
    @clase grafoMedellin
    Descripcion: Implementacion de grafo utilizando diccionario de lista de pares
    @author Mateo Ramirez H. / Juan Camilo Echeverri S.
    @version 1
"""

class grafoMedellin:

    def __init__(self):
        #Creo un diccionario
        self.grafo={}


    def crear_grafo(self):

    	#CREAMOS LOS VERTICES

        #Utilizo with para abrir el archivo y cerrarlo automaticamente al acabar
         with open("vertices.txt") as f:
            #Leo linea por linea
            for line in f:
                #Creo un arreglo que almacene cada string separado por un espacio en la linea
                a=line.split(" ")
                #Creo una lista dentro de la llave de mi diccionario que es la posicion cero del arreglo
                self.grafo[a[0]]=[]

        #CREAMOS LOS ARCOS
        
        #Utilizo with para abrir el archivo y cerrarlo automaticamente al acabar
         with open("arcos.txt") as f:
            #Leo linea por linea
            for line in f:
                #Creo un arreglo que almacene cada string separado por un espacio en la linea
                a=line.split(" ")
                #Añado en el vertice asignado una tupla que contiene el vertice adyacente y peso del arco
                self.grafo[a[0]].append((a[1],a[2]))