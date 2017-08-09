import DigraphAM
import DigraphAL

#prueba1
#Crea grafo en matriz
grafo_matriz = DigraphAM.digraphAM(11)
grafo_matriz.add_arc(5,11)
grafo_matriz.add_arc(11,2)
grafo_matriz.add_arc(11,9)
grafo_matriz.add_arc(11,10)
grafo_matriz.add_arc(7,11)
grafo_matriz.add_arc(7,8)
grafo_matriz.add_arc(8,9)
grafo_matriz.add_arc(3,8)
grafo_matriz.add_arc(3,10)
#Imprime matriz
print (grafo_matriz.matriz)
#Metodo get_successors
print(grafo_matriz.get_successors(11))
#Metodo get_weight
print(grafo_matriz.get_weight(11,10))
print(grafo_matriz.get_weight(11,1))

#Crea grafo en lista
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
#Imprime lista
print (grafo_lista.lista)
#Metodo get_successors 
print(grafo_lista.get_successors(11))
#Metodo get_weight
print(grafo_lista.get_weight(11,10))
print(grafo_lista.get_weight(11,1))
