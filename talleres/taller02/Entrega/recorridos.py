import DigraphAL


grafo_lista = DigraphAL.digraphAL(11)
grafo_lista.add_arc(5,11)
grafo_lista.add_arc(11,2)
grafo_lista.add_arc(11,9)
grafo_lista.add_arc(11,10)
grafo_lista.add_arc(7,11)
grafo_lista.add_arc(7,8)
grafo_lista.add_arc(8,9)
grafo_lista.add_arc(3,8)
grafo_lista.add_arc(3,10)



def dfs_aux(grafo, vertice, final, recorrido, resultado):
    recorrido+=[vertice]
    if vertice == final:
        resultado.append(recorrido)
    else:
        for i in grafo.get_successors(vertice):
             if i not in recorrido:
                dfs_aux(grafo,i,final,recorrido[:],resultado)




def dfs(grafo, vertice, final):
    resultado = []
    dfs_aux(grafo,vertice,final,[],resultado)
    return resultado
