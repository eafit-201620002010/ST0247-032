"""
@clase entrega2_crearGrafo
Descripcion: Construccion diccionarios del grafo
@author Mateo Ramirez H. / Juan Camilo Echeverri S.
@version 1
"""
class entrega2_diccionarios:

    def __init__(self):
        #Creo dos diccionario
        self.diccionario_coor={}
        self.diccionario_name={}
        self.diccionario_rh={}



    def crear_dic_coor(self):
         with open("vertices.txt") as f:
            for line in f:
                a=line.split(" ")
                self.diccionario_coor[(a[1],a[2])]=a[0]


    def crear_dic_name(self):
         with open("vertices.txt") as f:
            for line in f:
                a=line.split(" ")
                self.diccionario_name[a[3][:-1]]=a[0]

    def crear_dic_rh(self):
         with open("vertices.txt") as f:
            for line in f:
                a=line.split(" ")
                self.diccionario_rh[a[0]]=[(a[1],a[2])]




di=entrega2_diccionarios()
di.crear_dic_name()
di.crear_dic_coor()
