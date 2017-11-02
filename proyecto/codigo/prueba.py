import grafo
import diccionarios
import math
from time import time
import os
import psutil

grafo=grafo.grafo()
grafo.crear_grafo()

diccionarios=diccionarios.diccionarios()
diccionarios.crear_dic_coor()
diccionarios.crear_dic_id()

coordenadas=[(6.228493,-75.570888),(6.235463,-75.575514),(6.237513,-75.570420),(6.246328,-75.575205),(6.260740,-75.591001),(6.256578,-75.615109),
(6.205157,-75.555572),(6.209039,-75.558876)]
inicial=(6.237513,-75.570420)



"""
    Dado un vertice inicial, un vertice objetivo y un grafo, retorna
    el camino mas corto entre ambos vertices .

    *Parametro graph: Grafo a utilizar.
    *Parametro initial: Vertice de inicio.
    *Parametro end: Vertice objetivo.
    *Return: retorna una lista de vertices visitados para llegar al vertice objetivo desde el inicial.
"""
def dijsktra(graph, initial, end):
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = list(graph.grafo[current_node].keys())
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.grafo[current_node][next_node] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return [math.inf]
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    path = path[::-1]
    return path



"""
    Dado unas coordenada inicial y una lista de coordenas, retorna
    la coordenada mas cercana.

    *Parametro inicial: Coordenada inicial.
    *Parametro coordenadas: Lista de coordenadas.
    *Return: retorna un la coordenada mas cercana o mas similar a la coordenada inicial.
"""
def calcular_cercano(inicial,coordenadas):
    minimo = math.inf
    resultado=None

    for i in coordenadas:
        temp = math.hypot(float(i[0]) - inicial[0], float(i[1]) - inicial[1])

        minimo = min(minimo,temp)
        if minimo == temp:
            resultado = i

    return resultado



"""
    Dado una lista de vertices, retorna la distancia de recorrer cada vertice de la lista.

    *Parametro recorrido: Lista de vertices.
    *Return: retorna un float que es la distancia total de recorrer todos los vertices de la lista.
"""
def distancia(recorrido):
    distancia=0

    for i in range(len(recorrido)-1):
        distancia+=grafo.grafo[recorrido[i]][recorrido[i+1]]

    return distancia



"""
    Dado unas coordenadas iniciales y una lista de coordenas, retorna
    una lista de id's de vertices visitados para recorrer todas las coordenadas.

    *Parametro inicial: Coordenada inicial.
    *Parametro coordenadas: Lista de coordenadas a visitar.
    *Return: retorna una lista con el id de cada vertice visitado para poder recorrer el total de elementos
     de la lista coordenadas y volver a la coordenada inicial.
"""
def recorrido2(inicial,coordenadas):
    diccionario=diccionarios.diccionario_coor
    temp=diccionario[inicial[0],inicial[1]]
    recorrido=[]

    while coordenadas:

        inicial_id=diccionario[inicial[0],inicial[1]]
        proximo=coordenadas.pop()
        proximo_id=diccionario[proximo[0],proximo[1]]

        diji=dijsktra(grafo,inicial_id,proximo_id)
        if math.inf in diji:
            return "Ruta imposible"

        recorrido+=diji[:len(diji)-1]
        inicial=proximo

    inicial_id=diccionario[inicial[0],inicial[1]]
    diji=dijsktra(grafo,inicial_id,temp)
    recorrido+=diji


    return recorrido



"""
    Dado unas coordenadas iniciales y una lista de coordenas, verifica
    si existen en el grafo para poder remplazarlas con las coordenadas mas
    cercanas en caso de no existir.

    *Parametro inicial: Coordenada inicial.
    *Parametro coordenadas: Lista de coordenadas a visitar.
    *Return: retorna una lista con el id de cada vertice visitado para poder recorrer el total de elementos
     de la lista coordenadas y volver a la coordenada inicial.
"""


 
 


def prueba(inicial, coordenadas):
    tiempo_inicial = time() 
 
    llaves=diccionarios.diccionario_coor.keys()
    inicialStr=str(inicial[0]),str(inicial[1])
    coordenadasStr=[(str(i[0]),str(i[1])) for i in coordenadas]

    if inicialStr not in llaves:
        inicialStr=calcular_cercano(inicial,llaves)

    for i in range(len(coordenadasStr)):
        if coordenadasStr[i] not in llaves:
            coordenadasStr[i]=calcular_cercano(coordenadas[i],llaves)

    test=recorrido2(inicialStr,coordenadasStr)
    if test == "Ruta imposible":
        print("Recorrido2: ",test)
    else:
        print("Recorrido2 ",test," Distancia ",distancia(test))
    tiempo_final = time()
    tiempo_ejecucion = tiempo_final - tiempo_inicial
    print ('El tiempo de ejecucion fue:',tiempo_ejecucion, "seg")
    process = psutil.Process(os.getpid())
    print(process.memory_info().rss, "bytes")

"""
coordenadas=[]
for i in test:
        coordenadas.append(diccionarios.diccionario_id[str(i)])
print("Recorrido2 ",coordenadas)
a=diccionarios.diccionario_coor.keys()
print("PRUEBA",calcular_cercano((5.0,2.0),a))
"""
