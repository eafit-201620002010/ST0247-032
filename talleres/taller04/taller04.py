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

def remove_at(grafo,permutaciones):
		
