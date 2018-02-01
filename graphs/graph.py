#a simple directed graph implementation with support for common graph algorithms
class Vertex:
    def __init__(self, i):
        self.id = i
        self.neighbors = []
    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor)
    def getNeighbors(self):
        return self.neighbors

class Graph:
    def __init__(self, totNodes):
        self.vertices = []
        for i in range(totNodes):
            self.vertices.append(Vertex(i))
        self.adjMatrix = [[-1]*totNodes for i in range(totNodes)]
        self.totNodes = totNodes
    def addEdge(self, frm, to, cost):
        if(0<=frm<self.totNodes and 0<=to<self.totNodes):
            self.adjMatrix[frm][to]=cost
            self.vertices[frm].addNeighbor(to)
    def printAdjMatrix(self):
        for i in range(self.totNodes):
            for j in range(self.totNodes):
                print(self.adjMatrix[i][j], end='\t')
            print()
    def getVertex(self, id):
        return(self.vertices[id])
    def dfs(self, id):
        self.dfsRecur(id, set())
    def dfsRecur(self, id, visitedSet):
        if id in visitedSet:
            pass
        else:
            print('at node {0}'.format(id))
            visitedSet.add(id)
            for neighbor in self.vertices[id].getNeighbors():
                visitedSet = self.dfsRecur(neighbor, visitedSet)
        return visitedSet
    def bfs(self, id):
        q = []
        visitedSet = set()
        q.append(self.vertices[id])
        while q:
            curVertex = q.pop(0)
            print('at node {0}'.format(curVertex.id))
            visitedSet.add(curVertex.id)
            for n in curVertex.getNeighbors():
                if n not in visitedSet:
                    neighbor = self.vertices[n]
                    q.append(neighbor)


if __name__=='__main__':
    G = Graph(5)
    #G.printAdjMatrix()
    G.addEdge(1,0,0)
    G.addEdge(1,2,0)
    G.addEdge(0,3,0)
    G.addEdge(2,4,0)
    print('adjacency matrix')
    G.printAdjMatrix()
    print('dfs')
    G.dfs(1)
    print('bfs')
    G.bfs(1)
    