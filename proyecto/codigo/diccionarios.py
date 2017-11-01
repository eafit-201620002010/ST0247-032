"""
@clase diccionarios
Descripcion: Construccion diccionarios del grafo
@author Mateo Ramirez H. / Juan Camilo Echeverri S.
@version 1
"""
class diccionarios:

    def __init__(self):

        #Creo dos diccionarios.
        self.diccionario_coor={}
        self.diccionario_name={}
        self.diccionario_id={}


    def crear_dic_coor(self):
        #"with" abre el archivo y lo cierra al acabar.
         with open("vertices.txt", encoding="utf8") as f:

            #Leo linea por linea
            for line in f:

                #Creo una lista que almacena cada elemento de la linea separado por espacios.
                #Nota: la posicion '0' de la lista almacena el id del vertice, la posicion '1' y '2' las coordenadas,
                #y la posicion '3' el nombre del vertice.
                a=line.split(" ")

                #Cada llave de mi diccionario es una tupla con las cordenadas del vertice y almacena el id del vertice
                self.diccionario_coor[(a[1],a[2])]=a[0]


    def crear_dic_name(self):
         with open("vertices2.txt", encoding="utf8") as f:
            for line in f:
                a=line.split(" ")

                #Cada llave de mi diccionario es el nombre del vertice y almacena el id del vertice
                self.diccionario_name[a[3][:-1]]=a[0]


    def crear_dic_id(self):
         with open("vertices.txt", encoding="utf8") as f:
            for line in f:
                a=line.split(" ")

                #Cada llave de mi diccionario es el nombre del vertice y almacena el id del vertice
                self.diccionario_id[a[0]]=(a[1],a[2])