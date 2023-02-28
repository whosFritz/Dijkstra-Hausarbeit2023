import heapq

# Laden des Graphen aus einer Textdatei
graph = {}
with open('Graph_Dijk2_1.txt', 'r') as file:
    for line in file:
        node1, node2, weight = line.strip().split()
        if node1 not in graph:
            graph[node1] = {}
        graph[node1][node2] = int(weight)
start = '0'


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        curr_distance, curr_node = heapq.heappop(pq)

        if curr_distance > distances[curr_node]:
            continue

        for neighbor, weight in graph[curr_node].items():
            distance = curr_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


def find_shortest_paths(graph, start):
    """
    Bestimmt die kürzesten Pfade von einem gegebenen Startknoten zu allen anderen Knoten im Graphen.
    """
    # Ausführung des Dijkstra-Algorithmus
    distances = dijkstra(graph, start)
    shortest_paths = {}
    for i in range(len(graph)):
        shortest_path = []
        node = str(i)
        visited = set()
        while node != start:
            shortest_path.insert(0, node)
            for neighbor, weight in graph[node].items():
                if neighbor not in visited and distances[node] == distances[neighbor] + weight:
                    node = neighbor
                    visited.add(node)
                    break
        shortest_path.insert(0, start)
        shortest_paths[str(i)] = shortest_path
    return shortest_paths


shortest_paths = find_shortest_paths(graph, start)


# http://graphonline.ru/en/?graph=EKszLEDFGjKuivSW
for x in shortest_paths:
    print(x, shortest_paths[x])
