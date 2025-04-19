class Solution:
    def countBits(self, n):
        r = [0] * (n + 1)
        for i in range(1, n + 1):
            r[i] = r[i >> 1] + (i & 1)

        return r