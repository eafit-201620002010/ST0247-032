import grafo

#punto 1
def puedo_poner_reina(r,tablero):
	for i in range(r):
		if abs(tablero[i]-tablero[r])==r-i or tablero[i]==tablero[r]:
			return False
	return True


def n_reinas(n):
	tablero = [None]*n
	return len(n_reinas_aux([],0,tablero)) 



def n_reinas_aux(r,n,tablero):
	if n>=len(tablero):
		r.append(tablero)
	else:
		for i in range(len(tablero)):
			tablero[n]=i
			if puedo_poner_reina(n,tablero):
				n_reinas_aux(r,n+1,tablero)
	return r

#punto 2

grafo = grafo.digraphAL(11)
grafo.add_arc(5,11)
grafo.add_arc(11,2)
grafo.add_arc(11,9)
grafo.add_arc(11,10)
grafo.add_arc(7,11)
grafo.add_arc(7,8)
grafo.add_arc(8,9)
grafo.add_arc(3,8)
grafo.add_arc(3,10)


def camino(grafo,inicio,fin):
	visitados=[False]*len(grafo.lista)
	return dfs(grafo,inicio,fin,visitados)


def dfs(grafo,nodo,objetivo,visitados):
	visitados[nodo]=True
	if nodo==objetivo:
		return True
	else:
		sucesores=grafo.get_successors(nodo)
		for i in sucesores:
			if not visitados[i]:
				if dfs(grafo,i,objetivo,visitados):
					return True
	return False
