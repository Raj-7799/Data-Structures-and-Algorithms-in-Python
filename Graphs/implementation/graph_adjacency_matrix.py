from pprint import pformat

class Graph:
    """[Generates a un-directed graph which stores the data in the form of Adjacency matrix]
    """
    def __init__(self, nums=0):
        """[Initializes the graph with]

        Args:
            nums (int, optional): [description]. Defaults to 0.
        """
        self.V = nums
        self.graph = [[0 for i in range(nums)] for j in range(nums)]
    
    def add_edge(self, vertex_1, vertex_2):
        """[It creates a edge between two vertex.]

        Args:
            vertex_1 ([int])
            vertex_2 ([int])
        """
        self.graph[vertex_1][vertex_2] = 1
        self.graph[vertex_2][vertex_1] = 1
    
    def __str__(self):
        return pformat(self.graph)

# driver
if __name__ == "__main__":
    g = Graph(5)

    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(3, 4)
    
    print(g)
