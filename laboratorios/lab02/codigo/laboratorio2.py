#punto 1.1
def es_valido(tablero):
	for i in range(len(tablero)-1):
		for k in range(i+1,len(tablero)):
			if abs(int(tablero[i])-int(tablero[k]))==k-i or tablero[i]==tablero[k]:
				return False
	return True

def queens_aux(pre, pos, resultado):
	if len(pos)==0:
		resultado.append(pre)
	for i in range(len(pos)):
		queens_aux(pre+pos[i],pos[:i]+pos[i+1:],resultado)
	return resultado

def queens(n):
	pos=[str(i) for i in range(n)]
	permutaciones=queens_aux("",pos,[])
	contador=0
	for i in range(len(permutaciones)):
		opcion=list(permutaciones[i])
		if es_valido(opcion):
			contador+=1
	return contador
