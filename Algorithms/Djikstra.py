import heapq

def Djikstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    pq = [(start, 0)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > dist[current_node]:
           continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return dist