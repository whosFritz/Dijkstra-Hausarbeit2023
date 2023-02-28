import heapq
from typing import List, Tuple


def dijkstra(start: int, graph: List[List[Tuple[int, int]]]) -> Tuple[List[int], List[int]]:
    """
    Calculates the shortest path from a given start node to all other nodes in a graph using Dijkstra's algorithm.

    Args:
        start (int): The start node.
        graph (List[List[Tuple[int,int]]]): The graph represented as an adjacency list.

    Returns:
        Tuple[List[int], List[int]]: A tuple containing two lists:
            - The first list contains the shortest distances from the start node to all other nodes.
            - The second list contains the previous node in the path from the start node to all other nodes.
              If a node is unreachable, its previous node is set to None.
    """

    n = len(graph)
    dist = [float('inf')] * n
    prev = [None] * n
    dist[start] = 0

    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            alt = dist[u] + w
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(pq, (alt, v))

    return dist, prev


def all_shortest_paths(start: int, graph: List[List[Tuple[int, int]]]) -> List[List[Tuple[int, List[int]]]]:
    """
    Calculates the shortest paths from a given start node to all other nodes in a graph.

    Args:
        start (int): The start node.
        graph (List[List[Tuple[int,int]]]): The graph represented as an adjacency list.

    Returns:
        List[List[Tuple[int,List[int]]]]: A list containing one list for each node in the graph.
            Each inner list contains a tuple for each reachable node, where the first element is the distance
            from the start node to that node, and the second element is the list of nodes representing the shortest
            path from the start node to that node.
            If a node is unreachable, it is not included in the inner list.
    """

    n = len(graph)
    all_paths = []
    for i in range(n):
        if i == start:
            all_paths.append([(0, [start])])
            continue
        dist, prev = dijkstra(i, graph)
        paths = []
        for j in range(n):
            if dist[j] != float('inf'):
                path = [j]
                u = j
                while prev[u] is not None:
                    path.append(prev[u])
                    u = prev[u]
                path.reverse()
                paths.append((dist[j], path))
        all_paths.append(paths)

    return all_paths


# read the graph from the file
with open('Graph_Dijk2_1.txt', 'r') as f:
    lines = f.readlines()
    graph = [[] for _ in range(len(lines))]
    for line in lines:
        u, v, w = map(int, line.strip().split())
        graph[u].append((v, w))

# calculate the shortest paths from the start node 0 to all other nodes
all_paths = all_shortest_paths(0, graph)

# print the result
for i, paths in enumerate(all_paths):
    print(f'Shortest paths from node 0 to node {i}:')
    for dist, path in paths:
        print(f'distance: {dist}, path: {path}')
