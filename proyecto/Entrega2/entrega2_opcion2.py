import nodo

class entrega2_opcion2:

    """
    Aqui implemente el grafo con:
    un diccionario el cual por cada id de vertice guarda un nodo que contiene coordenadas, nombre y una lista
    dentro de la lista de cada nodo se guarda una tupla con el id del vertice y el peso hacia este
    """

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
                temp=nodo.nodo(a[1],a[2],a[3][:-1])
                #Creo una lista dentro de la llave de mi diccionario que es la posicion cero del arreglo
                self.grafo[a[0]]=temp

        #CREAMOS LOS ARCOS
        
        #Utilizo with para abrir el archivo y cerrarlo automaticamente al acabar
         with open("arcos.txt") as f:
            #Leo linea por linea
            for line in f:
                #Creo un arreglo que almacene cada string separado por un espacio en la linea
                a=line.split(" ")
                #Añado en el vertice asignado una tupla que contiene el vertice adyacente y peso del arco
                self.grafo[a[0]].lista.append((a[1],a[2]))

