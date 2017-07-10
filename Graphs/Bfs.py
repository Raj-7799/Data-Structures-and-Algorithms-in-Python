class Vertex(object):
    def __init__(self, data):
        self.visited = None
        self.data = data
        self.neighbours = []

    def addneighbour(self, vertex):
        self.neighbours.append(vertex)

    def __str__(self):
        return str(self.data)

    def setvisited(self):
        self.visited = True


class BreadthFirstSearch:
    def __init__(self):
        self.queue = []

    def isempty(self):
        if not self.queue:
            return True
        else:
            return False

    def enqueue(self, vertex):
        self.queue.append(vertex)

    def dequeue(self):
        if self.isempty():
            print("queue is empty")
        else:
            x = self.queue[0]
            self.queue = self.queue[1:]
            return x

    def bfs(self, root):
        root.setvisited()
        self.enqueue(root)
        while not self.isempty():
            root = self.dequeue()
            root.setvisited()
            print(root)
            for i in root.neighbours:
                if not i.visited:
                    i.setvisited()
                    self.enqueue(i)


if __name__ == '__main__':
    vertex1 = Vertex("A")
    vertex2 = Vertex("B")
    vertex3 = Vertex("C")
    vertex4 = Vertex("D")
    vertex1.addneighbour(vertex2)
    vertex2.addneighbour(vertex3)
    vertex3.addneighbour(vertex4)
    vertex4.addneighbour(vertex1)
    b = BreadthFirstSearch()
    b.bfs(vertex1)
    print("Done!")
