"""
    @clase laboratorio4
    Descripcion: Puntos del laboratorio 4
    @author Mateo Ramirez H. / Juan Camilo Echeverri S.
    @version 1
"""
import math



"""
Title:  ED2-respuestas-Taller6-Greedy.doc
Author: Mauricio
Date: 
Code Version: 
Avaibility: http://interactiva.eafit.edu.co/ei/contenido
"""
def punto1(grafo,inicial):
    visitados = [False]*(grafo.size+1)
    respuesta = [0]*(grafo.size+2)
    indice = 0
    actual = inicial
    cercano = -1
    cercano_peso = math.inf
    visitados[actual] = True
    successors=grafo.get_successors(actual)

    for i in successors:
        if grafo.get_weight(actual,i) < cercano_peso and i != actual and not visitados[i]:
            cercano = i
            cercano_peso = grafo.get_weight(actual,i)
    indice += 1
    actual = cercano
    respuesta[indice] = actual

    while indice < grafo.size:
        cercano = -1
        cercano_peso = math.inf
        visitados[actual] = True

        successors = grafo.get_successors(actual)

        for i in successors:
            if grafo.get_weight(actual,i) < cercano_peso and i != actual and not visitados[i]:
                cercano = i
                cercano_peso = grafo.get_weight(actual, i)
        indice += 1
        actual = cercano
        respuesta [indice] = actual

    respuesta[indice] = inicial
    return respuesta
