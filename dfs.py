import sys

if len(sys.argv) != 2:
    print("Usage:-\npython dfs.py <OUT-FILE>\n")
    sys.exit(1)

INP_FILE = "graph.dat"
OUT_FILE = sys.argv[1]

class Vertex:
    count = 0

    def __init__(self):
        self.name = chr(ord('A') + Vertex.count)
        Vertex.count += 1
        self.adjVertices = []

    def __del__(self):
        Vertex.count -= 1


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
                weight = int(line[j*2 + 1])
                self.vertices[i].adjVertices.append(neighbour)
                self.edges[(self.vertices[i], neighbour)] = weight

    def display(self):
        print("The graph is:-\n")

        for i in range(self.vertexCount):
            print("Vertex " + self.vertices[i].name, " --> ", end="")
            adjVerticesCount = len(self.vertices[i].adjVertices)

            for j in range(adjVerticesCount):
                neighbour = self.vertices[i].adjVertices[j]
                weight = self.edges[(self.vertices[i], neighbour)]
                print(neighbour.name + "(" + str(weight) + "), ", end="")
            print("\n")


g = Graph(7)
g.display()
