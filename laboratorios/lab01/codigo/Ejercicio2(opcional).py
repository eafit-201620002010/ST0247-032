import DigraphAL


grafo = DigraphAL.digraphAL(4)
grafo.add_arc(2,3)
grafo.add_arc(3,2)
grafo.add_arc(1,3)
grafo.add_arc(3,1)
grafo.add_arc(1,4)
grafo.add_arc(4,1)


def FunnyGame(grafo):
	visitados=[False]*grafo.size
	vuelo=-1
	for i in range(grafo.size):
		if FunnyGame_aux(grafo,i+1,visitados)==True:
			vuelo=i+1
			break
	if vuelo>-1:
		print("First player wins flying to airport ",vuelo)
	else:
		print("First player loses")


def FunnyGame_aux(grafo,nodo,visitados):
	if all(visitados[:nodo-1]+visitados[nodo:]):
		visitados[nodo-1]=True
	vuelos=grafo.get_successors(nodo)
	for i in vuelos:
		if visitados[i-1]==False:
			visitados[nodo-1]=True
			if FunnyGame_aux(grafo,i,visitados)==False:
				visitados[nodo-1]=False
	return all(visitados)
