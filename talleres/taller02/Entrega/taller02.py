#Fuerza Bruta

# 1
def punto1(start, nums, target):
    if start==len(nums):
        return target==0
    return punto1(start+1,nums,target-nums[start]) or punto1(start+1,nums,target)


# 2
def punto2(pre, pos, resultado):
	resultado.add(pre)
	if len(pos)==0 :
		return resultado
	return punto2(pre+pos[:1],pos[1:],resultado) and punto2(pre,pos[1:],resultado)

# 3
def punto3(pre, pos, resultado):
	if len(pos)==0:
		resultado.add(pre)
	for i in range(len(pos)):
		punto3(pre+pos[i],pos[:i]+pos[i+1:],resultado)
	return resultado

# 4

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
	pos=""
	#pos=[format(i) for i in range(n)]
	for i in range(n):
		pos=pos+str(i)
	permutaciones=queens_aux("",pos,[])
	
	contador=0
	for i in range(len(permutaciones)):
		opcion=list(permutaciones[i])
		if es_valido(opcion):
			contador=contador+1
	return contador


