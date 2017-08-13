import DigraphAM
import DigraphAL
"""
    @archivo GraphAlgorithms
    Descripcion: implementacion algoritmos para probar en grafos.
    @author Mateo Ramirez H. / Juan Camilo Echeverri S.
    @version 1
"""

#Generamos un grafo de matriz y lo llenamos
gmatriz = DigraphAM.digraphAM(11)
gmatriz.add_arc(5,11)
gmatriz.add_arc(11,2)
gmatriz.add_arc(11,9)
gmatriz.add_arc(11,10)
gmatriz.add_arc(7,11)
gmatriz.add_arc(7,8)
gmatriz.add_arc(8,9)
gmatriz.add_arc(3,8)
gmatriz.add_arc(3,10)

#Generamos un grafo de lista y lo llenamos
glista = DigraphAL.digraphAL(11)
glista.add_arc(5,11)
glista.add_arc(11,2)
glista.add_arc(11,9)
glista.add_arc(11,10)
glista.add_arc(7,11)
glista.add_arc(7,8)
glista.add_arc(8,9)
glista.add_arc(3,8)
glista.add_arc(3,10)


def punto1_2(grafo):
	#Recorro el total de vertices de el grafo
	for i in range(grafo.size):
		#Comparo cual vertice tiene mayor longitud en sus lsitas y lo declaro como maximo
		if len(grafo.get_successors(i)) < len(grafo.get_successors(i+1)):
			maximo=i+1
		else:
			maximo=1
	#retorno el maximo
	return maximo
