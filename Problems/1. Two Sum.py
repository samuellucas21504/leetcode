from typing import List

class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int):
        s = {}

        for i in range(len(nums)):
            o = target - nums[i]
            if s.get(o) != None and s.get(o) != i:
                return [s[o], i]

            s[nums[i]] = i

print( Solution.twoSum([2,7,11,15], 9) )
