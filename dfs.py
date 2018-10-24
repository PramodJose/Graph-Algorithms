import collections
import heapq
'''import sys

if len(sys.argv) != 2:
    print("Usage:-\npython dfs.py <OUT-FILE>\n")
    sys.exit(1)

OUT_FILE = sys.argv[1]'''
INP_FILE = "graph.dat"


class Vertex:
    count = 0

    def __init__(self):
        self.name = chr(ord('A') + Vertex.count)
        Vertex.count += 1
        self.adjVertices = []
        self.status = None
        self.indegree = 0

    def __del__(self):
        Vertex.count -= 1


    def __lt__(self, other):
        return self.indegree < other.indegree


    def __cmp__(self, other):
        return self.indegree < other.indegree


class Edge:
    count = 1

    def __init__(self):
        self.label = Edge.count
        Edge.count += 1
        self.weight = 0
        self.src = None
        self.dest = None
        self.type = None

    def __del__(self):
        Edge.count -= 1


class Graph:

    def __init__(self, vertexCount):
        self.vertexCount = vertexCount
        self.vertices = []
        self.edges = {}
        fin = open(INP_FILE, "r")

        for i in range(vertexCount):
            self.vertices.append(Vertex())

        for i in range(vertexCount):
            line = fin.readline().split()
            adjVerticesCount = int(line[0])
            line = line[1:]

            for j in range(adjVerticesCount):
                neighbour = self.vertices[int(line[j*2]) - 1]
                neighbour.indegree += 1
                weight = int(line[j*2 + 1])
                self.vertices[i].adjVertices.append(neighbour)
                self.edges[(self.vertices[i], neighbour)] = weight

    def display(self):
        print("The graph is:-")

        for i in range(self.vertexCount):
            print("Vertex " + self.vertices[i].name, " -->  ", end="")
            adjVerticesCount = len(self.vertices[i].adjVertices)

            for j in range(adjVerticesCount):
                neighbour = self.vertices[i].adjVertices[j]
                weight = self.edges[(self.vertices[i], neighbour)]
                print(neighbour.name + "(" + str(weight) + ")", end="")
                if j != adjVerticesCount -1:
                    print(", ", end="")
            print()



    def displayStatus(self):
        print("The status of the vertices are:-")

        for i in range(self.vertexCount):
            print(self.vertices[i].name, " : ", self.vertices[i].status)


    def reset(self):
        for i in range(self.vertexCount):
            self.vertices[i].status = None


def DFS(graph, source, id=0, dfsTreeNum=1):       # id is used to identify the source/parent node from where DFS started
    if id == 0 and dfsTreeNum == 1:
        graph.reset()
        print()
    if id == 0:
        print("DFS Tree number", dfsTreeNum)

    source.status = "Visited"
    print(source.name, "  ", end="")
    for neighbour in source.adjVertices:
        if neighbour.status != "Visited":
            DFS(graph, neighbour, 1, dfsTreeNum)

    if id == 0:
        for vertex in graph.vertices:
            if vertex.status != "Visited":
                print()         # adding a newline for a better looking output
                DFS(graph, vertex, dfsTreeNum=dfsTreeNum+1)
                break
        if dfsTreeNum == 1:
            print()


def BFS(graph, source, bfsTreeNum=1):
    if bfsTreeNum == 1:
        graph.reset()
        print()

    Q = collections.deque()
    Q.append(source)
    source.status = "Added to Queue"

    print("BFS Tree number", bfsTreeNum)
    while len(Q) > 0:
        vertex = Q.popleft()
        vertex.status = "Visited"
        print(vertex.name, "  ", end="")

        for neighbour in vertex.adjVertices:
            if neighbour.status is None:
                neighbour.status = "Added to Queue"
                Q.append(neighbour)

    for vertex in graph.vertices:
        if vertex.status != "Visited":
            print()
            BFS(graph, vertex, bfsTreeNum + 1)

    if bfsTreeNum == 1:
        print()


def topologicalSort(graph):
    graph.reset()
    topologicalNum = 0

    Q = collections.deque()
    for vertex in graph.vertices:
        if vertex.indegree == 0:
            Q.append(vertex)
            vertex.status = "Added to Queue"

    while len(Q) > 0:
        vertex = Q.popleft()
        topologicalNum += 1
        print(vertex.name)
        vertex.status = "Visited"

        for neighbour in vertex.adjVertices:
            if neighbour.status is None:
                neighbour.indegree -= 1
                if neighbour.indegree == 0:
                    Q.append(neighbour)
                    neighbour.status = "Added to queue"

    if topologicalNum != graph.vertexCount:
        print("There was a cycle!")


g = Graph(7)
g.display()
topologicalSort(g)
