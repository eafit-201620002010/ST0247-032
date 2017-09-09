import grafo

grafo = grafo.digraphAL(3)
grafo.add_arc(0,2,15)
grafo.add_arc(0,1,7)
grafo.add_arc(0,3,6)
grafo.add_arc(2,0,9)
grafo.add_arc(2,1,6)
grafo.add_arc(2,3,12)
grafo.add_arc(3,2,8)
grafo.add_arc(3,0,10)
grafo.add_arc(3,1,4)
grafo.add_arc(1,3,3)
grafo.add_arc(1,2,7)
grafo.add_arc(1,0,2)





def permutaciones(pre, pos, resultado):
	if len(pos)==0:
		resultado.append(pre)
	for i in range(len(pos)):
		permutaciones(pre+pos[i],pos[:i]+pos[i+1:],resultado)
	return resultado

def FunnyGame_aux(grafo,nodo,visitados,suma,minimo):
	print ("Estoy en: ",nodo," y sumo ",suma)
	if suma>minimo:
		print("la cague: ",nodo)
		return -1
	vuelos=grafo.get_successors(nodo)
	for i in vuelos:
		if visitados[i]==False:
			print("sucesores: ",vuelos)
			print("quiero ir a :",i,visitados[i])
			visitados[i]=True
			suma+=grafo.get_weight(nodo,i)
			if FunnyGame_aux(grafo,i,visitados,suma,minimo)==-1:
				visitados[i]=False
				suma-=grafo.get_weight(nodo,i)

	return suma


#def remove_at(grafo,permutaciones):
		
