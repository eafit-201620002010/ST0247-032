import DigraphAM

"""
    @clase Ejercicio2
    Descripcion: implementacion de metodo para colorear grafo.
    @author Mateo Ramirez H. / Juan Camilo Echeverri S.
    @version 1
"""


#Algoritmo compartido por el profesor
def bipartito(grafo, vertice):
	color=[-1]*len(grafo)
	color[vertice]=1

	vertices=[]
	vertices.append(vertice)

	while vertices:
		u=vertices.pop()
		if grafo[u][u]==1:
			return False

		for v in range(len(grafo)):
			if grafo[u][v] == 1 and color[v] == -1:
				color[v]=1-color[u]
				vertices.append(v)
			elif grafo[u][v] == 1 and color[v] == color[u]:
				return False
	return True

c="y"
#Creacion del grafo utilizando implementacion con matrices
while c=="y" or c=="Y":
	vertices=input("vertices: ")
	arcos=input("arcos: ")
	grafo2 = DigraphAM.digraphAM(int(vertices)-1)
	for i in range (int(arcos)):
		arco=input("arco: ")
		grafo2.add_arc(int(arco[0]),int(arco[1]))
		grafo2.add_arc(int(arco[1]),int(arco[0]))

	if bipartito(grafo2.matriz,0):
		print ("BICOLORABLE")
	else:
		print ("NOT BICOLORABLE")
	c=input("continue? ")