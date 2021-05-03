from Graphs.implementation.graph_adjacency_list import Graph

def dfs(graph: Graph, nums: int, starting_node: int):
    """[Runs depth first search on connected component of the starting_node]

    Args:
        graph ([Graph]): [graph implementation using adjacency list]
        nums ([int]): [number of vetexes in the graph]
        starting_node ([int]): [starting vertex for the graph]
    """
    visited = [False for i in range(nums)]
    stack = []

    visited[starting_node] = True
    stack.append(starting_node)

    while stack:
        node = stack.pop(-1)

        for neighbour in graph.get_neighbours(node):
            if not visited[neighbour]:
                visited[neighbour] = True
                stack.append(neighbour)
                print("Traversed from Node {} to Node {}".format(node, neighbour))


# driver
if __name__ == '__main__':
    g = Graph(5); # Total 5 vertices in graph
    g.add_edge(1, 0);
    g.add_edge(0, 2);
    g.add_edge(2, 1);
    g.add_edge(0, 3);
    g.add_edge(1, 4);
    dfs(g, 5, 0)