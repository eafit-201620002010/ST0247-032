

class prueba:

    def __init__(self):
        #Creo un diccionario
        self.grafo={}


    def crear_grafo(self):

         with open("sal.txt") as f:
            #Leo linea por linea
            for line in f:
                #Creo un arreglo que almacene cada string separado por un espacio en la linea
                a=line.split(" ")
                #Añado en el vertice asignado una tupla que contiene el vertice adyacente y peso del arco
                self.grafo[a[0]].append((a[1],a[2]))