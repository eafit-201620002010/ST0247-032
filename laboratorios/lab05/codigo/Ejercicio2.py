"""
    @clase Ejercicio 2
    Descripcion: Ejercicio2 lab 5
    @author Mateo Ramirez H. / Juan Camilo Echeverri S.
    @version 1
"""
from DigraphAM 
from lab05    import held_karp

def input(line):
    for i in range(len(line)):
        line[i] = int(line[i])

def coords(line):
    for i in range(len(line)):
        line[i] = int(line[i]) - 1

def crear_mundo(width, height, coords):
    world = DigraphAM.digraphAM(len(coords))
    for i in range(len(coords)):
        coords_i = coords[i]
        for j in range(len(coords)):
            coords_j = coords[j]
            cost = get_cost(coords_i[0], coords_i[1], coords_j[0], coords_j[1])
            world.addArc(i, j, cost)
    return world

def get_cost(x_s, y_s, x_e, y_e):
    cost_x = abs(x_s - x_e)
    cost_y = abs(y_s - y_e)
    return cost_x + cost_y
    
def solve(graph):
    return held_karp(graph)


n_worlds = int(input())
    
for i in range(n_worlds):
    w_size = input().split(' ')
    convert_input(w_size)
    if w_size[0] > 20 or w_size[1] >20:
        exit()
                
    start = input().split(' ')
    convert_coords(start)

    n_rad  = int(input())

    if n_rad > 10:
        exit()

    coords = [[0,0]]*n_rad
    
    for i in range(n_rad):
        coord = input().split(' ')
        convert_coords(coord)
        if coord[0] > 20 or coord[1] >20:
            exit()
        else:
            coords[i] = [coord[0], coord[1]]
    
    coords = [[start[0],start[1]]] + coords

    world = create_world(w_size[0], w_size[1], coords)
    print(world)
    print('The shortest path has length', solve(world))  