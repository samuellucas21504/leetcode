class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[b].append(a)

        state = [0] * numCourses

        def has_cycle(v):
            if state[v] == 1:
                return True
            if state[v] == 2:
                return False

            state[v] = 1
            for n in graph[v]:
                if has_cycle(n):
                    return True

            state[v] = 2
            return False

        for i in range(numCourses):
            if has_cycle(i):
                return False

        return True