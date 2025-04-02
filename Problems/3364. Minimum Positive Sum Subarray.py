import sys


class Solution(object):
    @staticmethod
    def minimumSumSubarray(nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        ts = sys.maxsize

        for i in range(l, r + 1):
            s = 0
            for j in range(i):
                s += nums[j]
            if 0 < s < ts:
                ts = s

            fp, lp = 0, i

            while lp < len(nums):
                s -= nums[fp]
                s += nums[lp]

                fp += 1
                lp += 1

                if 0 < s < ts:
                    ts = s

        return ts if ts != sys.maxsize else -1
