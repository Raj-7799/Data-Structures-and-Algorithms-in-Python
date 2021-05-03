from Graphs.implementation.graph_adjacency_list import Graph

def bfs(graph: Graph, nums: int, starting_node: int):
    """[Runs breadth first search on connected component of the starting_node]

    Args:
        graph ([Graph]): [graph implementation using adjacency list]
        nums ([int]): [number of vetexes in the graph]
        starting_node ([int]): [starting vertex for the graph]
    """
    visited = [False for i in range(nums)]
    queue = []

    visited[starting_node] = True
    queue.append(starting_node)

    while queue:
        node = queue.pop(0)

        for neighbour in graph.get_neighbours(node):
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)
                print("Traversed from Node {} to Node {}".format(node, neighbour))


# driver
if __name__ == '__main__':
    g = Graph(5)

    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(3, 4)
    g.add_edge(0, 3)
    g.add_edge(0, 1)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    
    bfs(g, 5, 0)
