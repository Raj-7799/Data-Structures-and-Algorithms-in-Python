from pprint import pformat

class Graph:
    """[Generates a un-directed graph which stores the data in the form of Adjacency matrix]
    """
    def __init__(self, nums=0):
        """[Initializes the graph with]

        Args:
            nums (int, optional): Defaults to 0.
        """
        self.V = nums
        self.graph = [[] for j in range(nums)]
    
    def add_edge(self, vertex_1, vertex_2):
        """[It creates a edge between two vertex.]

        Args:
            vertex_1 ([int])
            vertex_2 ([int])
        """
        self.graph[vertex_1].append(vertex_2)
        self.graph[vertex_2].append(vertex_1)
    
    def get_neighbours(self, vertex):
        """

        Args:
            vertex ([int]): []

        Returns:
            [list]: [all neighbours of the given vertex]
        """
        return self.graph[vertex]

    def __str__(self):
        return pformat(self.graph)

# driver
if __name__ == "__main__":
    g = Graph(5)

    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(3, 4)
    
    print(g)
