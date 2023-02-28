import heapq


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


# Laden des Graphen aus einer Textdatei
graph = {}
with open('Graph_Dijk1_1.txt', 'r') as file:
    for line in file:
        node1, node2, weight = line.strip().split()
        if node1 not in graph:
            graph[node1] = {}
        graph[node1][node2] = int(weight)
start = '0'

# Ausführung des Dijkstra-Algorithmus
distances = dijkstra(graph, start)
print(graph,"\n")
for x in distances:
    print(x, distances[x])