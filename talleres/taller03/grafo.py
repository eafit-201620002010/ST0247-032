#Implementacion de grafo en lista


class digraphAL:

    def __init__(self, size):
        self.size=size
        self.lista=[]
        for i in range(size+1): self.lista.append([])

    def add_arc(self,source,destination,weight=1):
        self.lista[source].append((destination,weight))

    def get_successors(self,vertex):
        successors=[]
        for i in range(len(self.lista[vertex])):
            successors.append(self.lista[vertex][i][0])
        return successors

    def get_weight(self,source,destination):
        for i in range(len(self.lista[source])):
            if self.lista[source][i][0]==destination:
                return self.lista[source][i][1]
        return 0

