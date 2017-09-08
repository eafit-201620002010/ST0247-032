size=input("tamaño: ")
tablero=[]
for i in range(int(size)):
	print ("fila: ",i)
	tablero.append(input())
print (tablero)

restriccion=[1459]*int(size)
for i in range(len(tablero)):
	for n in range(len(tablero[i])):
		if tablero[i][n]=="*":
			restriccion[i]=n
print (restriccion)