class Solution:
    @staticmethod
    def hammingWeight(self, n):
        q = 0
        while n > 0:
            if n & 1:
                q += 1
            n >>= 1

        return q