class Solution:
    def missingNumber(self, nums) -> int:
        x = 0

        for num in nums:
            x ^= num

        for i in range(len(nums) + 1):
            x ^= i

        return x