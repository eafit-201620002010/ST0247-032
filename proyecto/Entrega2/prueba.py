import entrega2_crearGrafo
import entrega2_diccionarios
import math


grafo=entrega2_crearGrafo.entrega2_crearGrafo()
grafo.crear_grafo()

diccionarios=entrega2_diccionarios.entrega2_diccionarios()
diccionarios.crear_dic_coor()


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
            return "Route Not Possible"
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    path = path[::-1]
    return path

#Metodos implementados bajo el principio de 'Collins' y esperan modificaciones mas optimas.

#Metodo para calcular el nodo mas cercano por medio de las coordenadas.
def calcular_minimo(inicial,coordenadas):
    #hypot(x,y)
    #sqrt(x*x + y*y)
    minimo = math.hypot(coordenadas[0][0] - inicial[0], coordenadas[0][1] - inicial[1])
    mini=coordenadas[0]
    for i in range(len(coordenadas)):
    	temp = math.hypot(coordenadas[i][0] - inicial[0], coordenadas[i][1] - inicial[1])
    	if min(minimo, temp) == temp:
    		minimo = temp
    		mini = i
    return mini

#Metodo para ejecutar dijsktra y calcular_minimo en todo mi grafo y encontrar toda la ruta
def recorrido(inicial,coordenadas):
	temp=diccionarios.diccionario_coor[str(inicial[0]),str(inicial[1])]
	recorrido=[]
    #Ciclo para viajar a todos los nodos
	while coordenadas:
        #Busco en mi diccionario el id de dichas coordenadas.
		inicial_id=diccionarios.diccionario_coor[str(inicial[0]),str(inicial[1])]
        #Calculo el nodo mas cercano a mi nodo principal para saber a cual viajar primero
		proximo=coordenadas.pop(calcular_minimo(inicial,coordenadas))
		proximo_id=diccionarios.diccionario_coor[str(proximo[0]),str(proximo[1])]
		diji=dijsktra(grafo,inicial_id,proximo_id)
		recorrido+=diji[:len(diji)-1]
		inicial=proximo
    #Al acabar el ciclo vuelvo al primer nodo
	inicial_id=diccionarios.diccionario_coor[str(inicial[0]),str(inicial[1])]
	diji=dijsktra(grafo,inicial_id,temp)
	recorrido+=diji
	return recorrido

#Metodo para calcular la distancia total recorrida ya que el dijsktra se me bugeo
#Implementacion magistral de 'Collins
#Nota: 'Collins' es una marca de machetes muy buena
def distancia(recorrido):
	distancia=0
	for i in range(len(recorrido)-1):
		distancia+=grafo.grafo[recorrido[i]][recorrido[i+1]]
	return distancia


coordenadas=[(5.1421214,2.143334395),(0.1421215,2.145434395)]
inicial=(2.1421213,0.143434395)
test=recorrido(inicial,coordenadas)
print("Recorrido ",test," Distancia ",distancia(test))

