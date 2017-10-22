import numpy,DigraphAL,itertools
"""
    @clase lab05
    Descripcion: Ejercicios del lab 5
    @author Mateo Ramirez H. / Juan Camilo Echeverri S.
    @version 1
"""

#Distancia levenshtein
#'a' cadena inicial, 'b' cadena objetivo
def punto1_1(a,b):
    aa = a.lower()
    bb = b.lower()

    if len(aa)==0:
        return bb
    elif len(bb)==0:
        return aa

    matriz = numpy.zeros((len(aa)+1,len(bb)+1),dtype=int)

    for i in range(len(aa)+1):
        matriz[i][0] = i
    for i in range(len(bb)+1):
        matriz[0][i] = i

    for i in range(1,len(aa)+1):
        aaa=aa[i-1]
        for k in range(1,len(bb)+1):
            bbb=bb[k-1]
            if aaa==bbb:
                costo=0
            else:
                costo=1
            matriz[i][k] = min(matriz[i-1][k]+1,
                               matriz[i][k-1]+1,
                               matriz[i-1][k-1]+costo)
    print (matriz)
    return matriz[len(aa)][len(bb)]


#Subsequencia
#'x'cadena a buscar subsequencia en cadena 'y'
def punto1_3(x,y):
    lenx=len(x)
    leny=len(y)
    table = numpy.zeros((lenx+1,leny+1),dtype=int)
    
    for i in range(1,lenx+1):
        for j in range(1,leny+1):
            if x[i-1] == y[j-1]:
                table[i][j] = table[i-1][j-1]+1
            else:
                table[i][j] = max(table[i][j-1],
                                  table[i-1][j])
    return table,table[lenx][leny]

#Metodo auxiliar para obtener la cadena de subsequencia
def punto1_4(x,y):
    indice = 0
    s=""
    matriz=punto1_3(x,y)[0]
    for i in range(len(matriz[0])):
        for j in range(len(matriz)):
            if matriz[j][i]>indice:
                s+=x[j-1]
                indice+=1
    return s
        

"""
Title: held_karp
Author: CarlEkerot
Date: 18 Feb 2016
Code Version: 
Avaibility: https://github.com/CarlEkerot/held-karp/blob/master/held-karp.py
"""

def held_karp(graph):

    dists = gen_dist(graph)
    n     = len(dists)

    # Maps each subset of the nodes to the cost to reach that subset, as well
    # as what node it passed before reaching this subset.
    # Node subsets are represented as set bits.
    C = {}

    # Set transition cost from initial state
    for k in range(1, n):
        C[(1 << k, k)] = (dists[0][k], 0)

    # Iterate subsets of increasing length and store intermediate results
    # in classic dynamic programming manner
    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            # Set bits for all nodes in this subset
            bits = 0
            for bit in subset:
                bits |= 1 << bit

            # Find the lowest cost to get to this subset
            for k in subset:
                prev = bits & ~(1 << k)

                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + dists[m][k], m))
                C[(bits, k)] = min(res)

    # We're interested in all bits but the least significant (the start state)
    bits = (2**n - 1) - 1

    # Calculate optimal cost
    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + dists[k][0], k))
    opt, parent = min(res)

    #path
    path = []
    for i in range(n - 1):
        path.append(parent)
        new_bits= bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = new_bits
    path.append(0)
    return opt, list(reversed(path))



#Metodo implementado para generar la matriz de distancias de un grafo
def gen_dist(graph):
    size = graph.size
    matriz = [[0]*size for i in range(size)]
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i][j] = graph.get_weight(i, j)
    return matriz
 

graph2 = DigraphAL.digraphAL(4)
graph2.add_arc(0, 1, 7)
graph2.add_arc(0, 2, 15)
graph2.add_arc(0, 3, 6)
graph2.add_arc(1, 0, 2)
graph2.add_arc(1, 2, 7)
graph2.add_arc(1, 3, 3)
graph2.add_arc(2, 0, 9)
graph2.add_arc(2, 1, 6)
graph2.add_arc(2, 3, 12)
graph2.add_arc(3, 0, 10)
graph2.add_arc(3, 1, 4)
graph2.add_arc(3, 2, 8)