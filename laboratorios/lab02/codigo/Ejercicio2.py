def puedo_poner_reina(r,tablero):
	for i in range(r):
		if abs(tablero[i]-tablero[r])==r-i or tablero[i]==tablero[r]:
			return False
	return True


def n_reinas():
	size=input("tamaño: ")
	tablero=[]
	for i in range(int(size)):
		print ("fila: ",i)
		tablero.append(input())
	restriccion=[1459]*int(size)
	for i in range(len(tablero)):
		for n in range(len(tablero[i])):
			if tablero[i][n]=="*":
				restriccion[i]=n
	tablero = [None]*int(size)
	return len(n_reinas_aux([],0,tablero,restriccion)) 



def n_reinas_aux(r,n,tablero,restriccion):
	if n>=len(tablero):
		r.append(tablero)
	else:
		for i in range(len(tablero)):
			if n<(len(restriccion)):
				if i==restriccion[n]:
					continue
			tablero[n]=i
			if puedo_poner_reina(n,tablero):
				n_reinas_aux(r,n+1,tablero,restriccion)
	return r