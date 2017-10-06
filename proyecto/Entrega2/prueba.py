from collections import defaultdict
  

class Prueba():
    def __init__(self):
        self.grafo=defaultdict(dict)
        self.diccionario_coor={}
        self.diccionario_name={}
        self.diccionario_rh={}
        self.recorrido=[]
    
    def crear(self):
        with open("arcos2.txt") as f:
            for line in f:
                a=line.split(" ")
                #opcion: int(round(float(a[2])))
                self.grafo[a[0]][a[1]] = float(a[2])

    def crear_dic_coor(self):
         with open("vertices2.txt") as f:
            for line in f:
                a=line.split(" ")
                self.diccionario_coor[(a[1],a[2])]=a[0]


    def crear_dic_name(self):
         with open("vertices2.txt") as f:
            for line in f:
                a=line.split(" ")
                self.diccionario_name[a[3][:-1]]=a[0]

    def crear_dic_rh(self):
         with open("vertices2.txt") as f:
            for line in f:
                a=line.split(" ")
                self.diccionario_rh[a[0]]=[(a[1],a[2])]



graph = Prueba()
graph.crear()
graph.crear_dic_rh()



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

#print(dijsktra(graph, 'X', 'Y'))
