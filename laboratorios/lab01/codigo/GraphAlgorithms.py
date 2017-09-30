import DigraphAM
import DigraphAL
from collections import defaultdict
"""
    @archivo GraphAlgorithms
    Descripcion: implementacion algoritmos para probar en grafos.
    @author Mateo Ramirez H. / Juan Camilo Echeverri S.
    @version 1
"""

#Generamos un grafo de matriz y lo llenamos
gmatriz = DigraphAM.digraphAM(11)
gmatriz.add_arc(5,11)
gmatriz.add_arc(11,2)
gmatriz.add_arc(11,9)
gmatriz.add_arc(11,10)
gmatriz.add_arc(7,11)
gmatriz.add_arc(7,8)
gmatriz.add_arc(8,9)
gmatriz.add_arc(3,8)
gmatriz.add_arc(3,10)

#Generamos un grafo de lista y lo llenamos
glista = DigraphAL.digraphAL(11)
glista.add_arc(5,11)
glista.add_arc(11,2)
glista.add_arc(11,9)
glista.add_arc(11,10)
glista.add_arc(7,11)
glista.add_arc(7,8)
glista.add_arc(8,9)
glista.add_arc(3,8)
glista.add_arc(3,10)


def punto1_2(grafo):
    #Recorro el total de vertices de el grafo
    for i in range(grafo.size):
        #Comparo cual vertice tiene mayor longitud en sus lsitas y lo declaro como maximo
        if len(grafo.get_successors(i)) < len(grafo.get_successors(i+1)):
            maximo=i+1
        else:
            maximo=1
    #retorno el maximo
    return maximo


def dijsktra(graph, initial):
  visited = {initial: 0}
  path = {}
  nodes = set()
  edges=defaultdict(list)

#Metodo implementado para obtener todos los vertices y agregarlos a un set
#Y obtener todas las aristas y agregarlas una estructura desconocida para mi
  for i in range(graph.size+1):
    nodes.add(i)
    successors = graph.get_successors(i)
    for k in range(len(successors)):
        edges[i].append(successors[k])

  while nodes: 
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]


    for edge in edges[min_node]:
      weight = current_weight + graph.get_weight(min_node, edge)
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return visited, path


#Adaptado de: http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
#Metodos implementados se refieren a los metodos echos por mi
def dfs(graph, start):
    visited, stack = set(), [start]
    grafo={}
    #Metodo implementado para pasar el grafo a diccionario de sets
    for i in range(graph.size+1):
        grafo[str(i)]=set()
        successors = graph.get_successors(i)
        for k in range(len(successors)):
            grafo[str(i)].add(str(successors[k]))
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(grafo[vertex] - visited)
    return visited

#Adaptado de: http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
#Metodos implementados se refieren a los metodos echos por mi
def bfs(graph, start):
    visited, queue = set(), [start]
    grafo={}
    #Metodo implementado para pasar el grafo a diccionario de sets
    for i in range(graph.size+1):
        grafo[str(i)]=set()
        successors = graph.get_successors(i)
        for k in range(len(successors)):
            grafo[str(i)].add(str(successors[k]))
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(grafo[vertex] - visited)
    return visited
