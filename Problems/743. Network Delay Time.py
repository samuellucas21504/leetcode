import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}

        for node in times:
            if node[0] not in graph:
                graph[node[0]] = {node[1]: node[2]}
            else:
                graph[node[0]][node[1]] = node[2]

        dist = {k: 0}
        pq = [(0, k)]
        while pq:
            current_distance, current_node = heapq.heappop(pq)

            node = graph.get(current_node)
            if node:
                for neighbor, weight in node.items():
                    distance = dist.get(neighbor, float('inf'))

                    if current_distance + weight < distance:
                        dist[neighbor] = current_distance + weight
                        heapq.heappush(pq, (current_distance + weight, neighbor))

        _max = -1
        if n > len(dist):
            return _max

        for key, v in dist.items():
            _max = max(_max, v)

        if _max == 0:
            return -1

        return _max