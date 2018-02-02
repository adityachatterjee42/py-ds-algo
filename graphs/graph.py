from queue import Queue
#a simple weighted, directed graph implementation with support for common graph algorithms
#implemented: bfs, dfs, kahn's topological ordering, unweighted shortest path
#pending: topo sort, dijkstra's, bellman-ford's, prim's, kruskal's 
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
    def getVertices(self):
        return self.vertices
    def getVertex(self, id):
        return(self.vertices[id])
    #depth-first search
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
    #breadth-first search
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
    #kahn's topological ordering algorithm
    def kahn(self):
        #setup phase
        inEdges = {}
        for i in range(self.totNodes):
            inEdges[i]=0
        for i in range(self.totNodes):
            for j in range(self.totNodes):
                if self.adjMatrix[i][j]!=-1:
                    inEdges[j]=inEdges[j]+1
        #setup complete (wouldn't need this step if using adjacency list)
        '''dict printer
        for i in range(self.totNodes):
            if i in inEdges:
                print('{0}:{1}'.format(i,inEdges[i]))

        '''
        while(inEdges):
            for i in range(self.totNodes):
                if i in inEdges and inEdges[i]==0:
                    print('at node {0}'.format(i))
                    inEdges.pop(i)
                    for j in range(self.totNodes):
                        if self.adjMatrix[i][j]!=-1:
                            self.adjMatrix[i][j]=-1
                            inEdges[j]=inEdges[j]-1
    #unweighted shortest paths
    def unwtSP(self, startId):
        q = Queue()
        distanceDict={}
        predecessorDict={}
        visitedSet=set()
        for vertex in self.getVertices():
            distanceDict[vertex.id]=-1
            predecessorDict[vertex.id]=None
        distanceDict[startId]=0
        q.put(startId)
        while(q.qsize()>0):
            curVertex=q.get()
            for neighbor in self.getVertex(curVertex).getNeighbors():
                if neighbor not in visitedSet:
                    visitedSet.add(neighbor)
                    distanceDict[neighbor]=distanceDict[curVertex]+1
                    predecessorDict[neighbor]=curVertex
                    q.put(neighbor)
        for x,y in distanceDict.items():
            print("Vertex:{0} Distance{1}".format(x,y))


    


    

if __name__=='__main__':
    G = Graph(5)
    #G.printAdjMatrix()
    G.addEdge(1,0,0)
    G.addEdge(1,2,0)
    G.addEdge(0,3,0)
    G.addEdge(2,4,0)
    G.addEdge(0,2,0)
    G.addEdge(3,2,0)
    #G.addEdge(1,4,0)
    print('adjacency matrix')
    G.printAdjMatrix()
    #print('dfs')
    #G.dfs(1)
    #print('bfs')
    #G.bfs(1)
    #G.kahn()
    G.unwtSP(1)
    