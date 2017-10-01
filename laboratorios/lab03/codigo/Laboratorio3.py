"""
    @clase laboratorio3
    Descripcion: Punto 2 del laboratorio 2
    @author Mateo Ramirez H. / Juan Camilo Echeverri S.
    @version 1
"""


def n_reinas(n):
	tablero = [None]*n
	return len(n_reinas_aux([],0,tablero)) 



def n_reinas_aux(r,n,tablero):
	if n>=len(tablero):
		r.append(tablero)
		return r
	else:
		for i in range(len(tablero)):
			tablero[n]=i
			if puedo_poner_reina(n,tablero):
				n_reinas_aux(r,n+1,tablero)
	return r

def puedo_poner_reina(r,tablero):
	for i in range(r):
		if abs(tablero[i]-tablero[r])==r-i or tablero[i]==tablero[r]:
			return False
	return True