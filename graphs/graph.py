from queue import Queue
#a simple weighted, directed graph implementation with support for common graph algorithms
#implemented: bfs, dfs, kahn's topological ordering, unweighted shortest paths, dijkstra's, bellman-ford
#pending: dfs topological ordering, prim's, kruskal's 
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
    def getDistance(self, x, y):
        return self.adjMatrix[x][y]
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
    
    #dijkstra's algorithm
    def dijkstra(self, startId):
        verticeSet = set([vertex.id for vertex in self.getVertices()])
        distanceDict = {} 
        predDict = {}
        predDict[startId] = None
        for i in range(len(self.vertices)):
            distanceDict[i]=-1
        distanceDict[startId]=0
        current = startId
        while(verticeSet):
            verticeSet.remove(current)
            for vertex in self.getVertex(current).getNeighbors():
                if vertex in verticeSet:
                    if distanceDict[vertex]==-1 or self.getDistance(current, vertex)<distanceDict[vertex]:
                        distanceDict[vertex]=self.getDistance(current, vertex)
                        predDict[vertex] = current
            minDistance=-1
            #this could be avoided if using priority queue
            for vertex, distance in distanceDict.items():
                if vertex in verticeSet and (minDistance==-1 or distance<minDistance):
                    minDistance=distance
                    current=vertex
        print("Shortest path distances:")
        print(distanceDict)   
        print("Predecessors")
        print(predDict)
    
    #bellman-ford algorithm
    def bellmanford(self, startID):
        dists = {}
        pred = {}
        pred[startID] = None
        for vertex in self.getVertices():
            dists[vertex.id]=None
        dists[startID]=0
        isChange=1
        while(isChange):
            isChange=0
            for vertex in self.getVertices():
                if dists[vertex.id]!=None:
                    for neighbor in vertex.getNeighbors():
                        if dists[neighbor] == None or dists[neighbor]>dists[vertex.id]+self.adjMatrix[vertex.id][neighbor]:
                            dists[neighbor] = dists[vertex.id]+self.adjMatrix[vertex.id][neighbor]
                            pred[neighbor] = vertex.id
                            isChange=1
        print("Shortest path distances:")
        print(dists)   
        print("Predecessors")
        print(pred)

    #prim's algorithm (minimum spanning tree)


if __name__=='__main__':
    G = Graph(3)
    #G.printAdjMatrix()
    G.addEdge(0,1,1)
    G.addEdge(0,2,5)
    G.addEdge(1,2,2)
    print('adjacency matrix')
    G.printAdjMatrix()
    #print('dfs')
    #G.dfs(1)
    #print('bfs')
    #G.bfs(1)
    #G.kahn()
    #G.unwtSP(1)
    #G.dijkstra(0)
    G.bellmanford(0)
    