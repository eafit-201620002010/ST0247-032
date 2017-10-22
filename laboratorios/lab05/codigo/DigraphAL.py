
"""
    @clase digraphAl
    Descripcion: implementacion de grafo con listas.
    @author Mateo Ramirez H. / Juan Camilo Echeverri S.
    @version 1.2
"""


class digraphAL:

    def __init__(self, size):
        self.size=size
        #Creo una lista
        self.lista=[]
        #Recorro desde la posicion 0 hasta el size asignado creando listas en cada posicion
        for i in range(size+1): self.lista.append([])

    def add_arc(self,source,destination,weight=1):
        #Añadimos una tupla en el vertice asignado que contiene el vertice adyacente con el peso de la arista que por defecto es 1
        self.lista[source].append((destination,weight))

 
    def get_successors(self,vertex):
        #Creo una lista
        successors=[]
        #Recorro la lista de mi vertice especificado
        for i in range(len(self.lista[vertex])):
            #Añado a mi lista creada todos los vertices adyacientes a mi vertice especificado
            successors.append(self.lista[vertex][i][0])
        #Retorno mi lista creada
        return successors


    def get_weight(self,source,destination):
        #Recorro la lista de mi vertice especificado
        for i in range(len(self.lista[source])):
            #Si en la lista del vertice especificado se encuentra el vertice de destino retorno el peso de el arco de los dos
            if self.lista[source][i][0]==destination:
                return self.lista[source][i][1]
        #Retorno cero por defecto
        return 0

