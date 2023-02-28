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


# read graph from file
filename = "Graph_Dijk2_1.txt"
with open(filename) as f:
    lines = f.readlines()

graph = [[] for _ in range(10)]
for line in lines:
    u, v, w = map(int, line.split())
    graph[u].append((v, w))

# run Dijkstra's algorithm
start = 0
dist, prev = dijkstra(start, graph)

# print shortest paths
for i in range(len(graph)):
    if dist[i] == float('inf'):
        print(f"Node {i}: unreachable")
    else:
        path = [i]
        u = i
        while prev[u] is not None:
            path.append(prev[u])
            u = prev[u]
        path.reverse()
        print(f"Node {i}: distance={dist[i]}, path={path}")
