"""
    @clase laboratorio3
    Descripcion: Puntos del laboratorio 3
    @author Mateo Ramirez H. / Juan Camilo Echeverri S.
    @version 1
"""
import DigraphAL, DigraphAM
import queue, math

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


def n_reinas(n):
    tablero = [None]*n
    return n_reinas_aux([],0,tablero)

def prueba(n):
    tablero = [None]*n
    k=0
    for i in range(n):
        if puedo_poner_reina(i,tablero):
            tablero[k]=i
            k+=1
    return tablero



def n_reinas_aux(r,n,tablero):
    if n>=len(tablero):
        r.append(tablero)
        return r
    else:
        for i in range(len(tablero)):
            tablero[n]=i
            if puedo_poner_reina(n,tablero):
                n_reinas_aux(r,n+1,tablero)
    return r

def puedo_poner_reina(r,tablero):
    for i in range(r):
        if abs(tablero[i]-tablero[r])==r-i or tablero[i]==tablero[r]:
            return False
    return True

def punto1_5(graph):
    grafo=transformar_grafo(graph)
    keys = grafo.keys()
    #recorremos todas las llaves
    for i in keys:
        #recorremos los elementos de la lista de cada llave
        for k in grafo[i]:
            #si la llave es un elemento de el elemento que tiene en su lista
            #o si la llave es un elemento de su propia lista entonces hay ciclo
            if i in grafo[k] or grafo[k]==i:
                return True
    return False

   
#Metodo para transformar un grafo a diccionario de listas
#Cada 'key' es un nodo y cada lista dentro del nodo son los nodos a los que el viaja
def transformar_grafo(graph):
    grafo={}
    for i in range(graph.size+1):
        successors = graph.get_successors(i)
        #recorremos el tamaño del grafo creando llaves con listas en un diccionario
        grafo[i]=[]
        for k in range(len(successors)):
            #por cada llave agregamos una lista de sus sucesores
            grafo[i].append(successors[k])
    return grafo



def punto1_3(grafo, inicial):
  recorrido = []
  q = queue.PriorityQueue()
  q.put(inicial)
  recorrido.append(inicial)
  while not q.empty():
    current = q.get()
    #Mientras la cola no este vacia se revisara cada vertice sucesor del vertice atual
    #si este no se encunetra en el recorrido se agrega
    for i in grafo.get_successors(current):
      if i not in recorrido:
        recorrido.append(i)
        q.put(i)
  return recorrido


def punto1_6(grafo, inicial, final):
  #llenar el arreglo de distancias con infinito
  costo = [math.inf]*(grafo.size+1)
  #marcar la distancia del nodo inicial como 0
  costo[inicial] = 0
  s_pathA(grafo, inicial, costo)
  return costo[final]

def punto1_6aux(grafo, inicial, costo):
  s = grafo.get_successors(inicial)
  if len(s) == 0:
    pass
  else:
    for i in s:
      weight = grafo.get_weight(inicial, i) + costo[inicial]
      #si la distancia se puede mejorar hasta aca 
      #marcamos la nueva distancia
      if costo[i] > weight:
        costo[i] = weight
      punto1_6aux(grafo, i, costo)



def punto2(grafo,nodo):
    costo = [math.inf]*(grafo.size+1)
    recorrido=[]
    costo[1] = 0
    punto2aux(grafo, 1, nodo, costo, recorrido)
    recorrido.append(nodo)
    if costo[n]== math.inf:
        return -1
    else:
        return recorrido



def punto2aux(grafo, k, nodo, costo, recorrido):
  kk = grafo.get_successors(k)
  if len(kk) == 0:
    pass
  else:
    for i in kk:
      weight = grafo.get_weight(k, i) + costo[k]
      if costo[i] > weight:
        if k not in recorrido:
          recorrido.append(k)
        costo[i] = weight
      else:
        if k in recorrido:
          recorrido.remove(k)
      punto2aux(grafo, i, nodo, costo, recorrido)