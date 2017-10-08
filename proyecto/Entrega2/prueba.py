import prototypeAlgo
import entrega2_crearGrafo
import entrega2_diccionarios
import math

#hypot(x,y)
#sqrt(x*x + y*y)

grafo=entrega2_crearGrafo.entrega2_crearGrafo()
grafo.crear_grafo()

diccionarios=entrega2_diccionarios.entrega2_diccionarios()
diccionarios.crear_dic_coor()

algoritmo=prototypeAlgo.Graph()

def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        #AQUI
        destinations = list(graph.grafo[current_node].keys())
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            #AQUI
            weight = graph.grafo[current_node][next_node] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path

coordenadas=[(5.1421214,2.143334395),(0.1421215,2.145434395)]
inicial=(2.1421213,0.143434395)

def calcular_minimo(inicial,coordenadas):
    #a=[p for i in range(num)]
    minimo = math.hypot(coordenadas[0][0] - inicial[0], coordenadas[0][1] - inicial[1])
    mini=coordenadas[0]
    for i in coordenadas:
    	temp = math.hypot(i[0] - inicial[0], i[1] - inicial[1])
    	if min(minimo, temp) == temp:
    		minimo = temp
    		mini = i
    return mini

def prueba(inicial,coordenadas):
	inicial_id=diccionarios.diccionario_coor[str(inicial[0]),str(inicial[1])]
	proximo=calcular_minimo(inicial,coordenadas)
	proximo_id=diccionarios.diccionario_coor[str(proximo[0]),str(proximo[1])]
	print (dijsktra(grafo,inicial_id,proximo_id))

  

