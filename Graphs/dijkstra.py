import sys
import heapq


class Vertex:
    def __init__(self, name):
        self.name = name
        self.predecessor = None
        self.visited = None
        self.neighbours = []
        self.mindistance = sys.maxsize

    def __cmp__(self, other):
        return self.cmp(self.mindistance, other.mindistance)

    def __lt__(self, other):
        selfPriority = self.mindistance
        otherPriority = other.mindistance
        return selfPriority < otherPriority

    def addneighbour(self, vertex):
        self.neighbours.append(vertex)


class Edge:
    def __init__(self, weight, origin, target):
        self.origin = origin
        self.target = target
        self.weight = weight


class Djiktra:
    def __init__(self):
        self.q = []

    def shortestpath(self, node):
        node.mindistance = 0
        heapq.heappush(self.q, node)

        while len(self.q) > 0:
            actualvertex = heapq.heappop(self.q)
            actualvertex.visited = True
            for edge in actualvertex.neighbours:
                u = edge.origin
                v = edge.target
                if not v.visited:
                    newdistance = u.mindistance + edge.weight
                    if newdistance < v.mindistance:
                        v.mindistance = newdistance
                        v.predecessor = u
                        heapq.heappush(self.q, v)

    def getshortespath(self, vertex):
        print("The shortest path is ", vertex.mindistance)
        node = vertex
        while node is not None:
            print(node.name)
            node = node.predecessor


if __name__ == '__main__':
    A = Vertex("A")
    B = Vertex("B")
    C = Vertex("C")
    D = Vertex("D")
    e1 = Edge(5, A, B)
    e2 = Edge(3, B, C)
    e3 = Edge(2, D, C)
    e4 = Edge(1, A, D)
    e5 = Edge(2, D , B)
    A.addneighbour(e1)
    A.addneighbour(e4)
    B.addneighbour(e2)
    D.addneighbour(e3)
    D.addneighbour(e5)
    op = Djiktra()
    op.shortestpath(A)
    op.getshortespath(C)
