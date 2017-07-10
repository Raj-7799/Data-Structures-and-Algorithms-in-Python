from Bfs import Vertex
from Bfs import BreadthFirstSearch


def dfs(node):
    node.visited = True
    print("%s ->" % node.data);
    for i in node.neighbours:
        if i.visited:
            pass
        else:
            dfs(i)


if __name__ == '__main__':
    vertex1 = Vertex("A")
    vertex2 = Vertex("B")
    vertex3 = Vertex("C")
    vertex4 = Vertex("D")
    vertex5 = Vertex("E")
    vertex6 = Vertex("F")
    vertex7 = Vertex("G")
    vertex8 = Vertex("H")
    vertex9 = Vertex("I")
    vertex10 = Vertex("J")
    vertex11 = Vertex("K")
    vertex1.addneighbour(vertex2)
    vertex1.addneighbour(vertex3)
    vertex2.addneighbour(vertex4)
    vertex2.addneighbour(vertex5)
    vertex3.addneighbour(vertex9)
    vertex3.addneighbour(vertex10)
    vertex4.addneighbour(vertex6)
    vertex4.addneighbour(vertex7)
    vertex9.addneighbour(vertex11)
    vertex6.addneighbour(vertex8)
    b = BreadthFirstSearch()
    dfs(vertex1)
