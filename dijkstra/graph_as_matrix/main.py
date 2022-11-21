import math


# get the shortest path from specific vertices in the graph
def getShortestDistancesFromVertex(graph, vertex):
    n = len(graph)
    not_visited = {i:True for i in range(n)}
    distances = [math.inf] * n

    distances[vertex] = 0
    while len(not_visited) > 0:
        shortest_distance = math.inf
        shortest_distance_index = -1
        for i in range(len(graph)):
            if i in not_visited and distances[i] < shortest_distance:
                shortest_distance = distances[i]
                shortest_distance_index = i
        if shortest_distance_index == -1:
            # disconnected graph
            break
        not_visited.pop(shortest_distance_index)
        # go through all neighbours
        for neighbour, cost in enumerate(graph[shortest_distance_index]):
            if cost != 0:
                distances[neighbour] = min(distances[neighbour], distances[shortest_distance_index] + cost)

    return distances
