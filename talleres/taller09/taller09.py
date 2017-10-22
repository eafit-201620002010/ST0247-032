import numpy

def levenshtein(a,b):
	aa = a.lower()
	bb = b.lower()

	if len(aa)==0:
		return bb
	elif len(bb)==0:
		return aa

	matriz = numpy.zeros((len(aa)+1,len(bb)+1),dtype=numpy.int)

	for i in range(len(aa)):
		matriz[i][0] = i
	for i in range(len(bb)):
		matriz[0][i] = i

	for i in range(1,len(aa)+1):
		aaa=aa[i-1]
		for k in range(1,len(bb)+1):
			bbb=bb[k-1]
			if aaa==bbb:
				costo=0
			else:
				costo=1
			print(matriz)
			matriz[i][k] = min(matriz[i-1][k]+1,
							   matriz[i][k-1]+1,
							   matriz[i-1][k-1]+costo)

	return matriz[len(aa)][len(bb)]

