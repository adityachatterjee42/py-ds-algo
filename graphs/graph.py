class Vertex:
    def __init__(self, node):
        self.id = node
        self.visited = False
    def addNeighbor(self, neighbor, G):
        G.addEdge(self.id, neighbor)
    def getConnections(self, G):
        return G.adjMatrix[self.id]
    def getVertexID(self):
        return self.id
    def setVertexID(self, id):
        self.id = id
    def setVisited(self):
        self.visited = True
    def __str__(self):
        return str(self.id)

class Graph:
    def __init__(self, numVertices, cost=0):
        self.adjMatrix = [[-1]*numVertices for i in range(numVertices)]
        self.numVertices = numVertices
        self.vertices = []
        for i in range(0, numVertices):
            newVertex = Vertex(i)
            self.vertices.append(newVertex)
    def setVertex(self, vtx, id):
        if 0<=vtx<self.numVertices:
                self.vertices[vtx].setVertexID(id)
    def getVertex(self, n):
        for vertxin in range(self.numVertices):
            if n == self.vertices[vertxin].getVertexID():
                return vertxin
            else:
                return -1
    def addEdge(self, frm, to, cost=0):
        if self.getVertex(frm)!=-1 and self.getVertex(to)!=-1:
            self.adjMatrix[self.getVertex(frm)][self.getVertex(to)] = cost
            self.adjMatrix[self.getVertex(to)][self.getVertex(frm)] = cost
    def getVertices(self):
        vertices=[]
        for vertexin in range(0,self.numVertices):
            vertices.append(self.vertices[vertxin].getVertexID())
        return vertices
    def printMatrix(self):
        for u in range(0,self.numVertices):
            row=[]
            for v in range(0,self.numVertices):
                row.append(self.adjMatrix[u][v])
            print(row)
    def getEdges(self):
        edges=[]
        for v in range(0,self.numVertices):
            for u in range(0,self.numVertices):
                if self.adjMatrix[u][v]!=-1:
                    vid=self.vertices[v].getVertexID()
                    uid=self.vertices[u].getVertexID()
                    edges.append((vid, uid, self.adjMatrix[u][v]))
        return edges







