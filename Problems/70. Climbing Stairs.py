class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [0] * n
        for i in range(0, n):
            if i - 1 > 0 and i - 2 > 0:
                steps[i] = steps[i - 1] + steps[i - 2]
            else:
                steps[i] = i + 1

        return steps[-1]
