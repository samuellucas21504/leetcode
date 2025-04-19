class Solution:
    @staticmethod
    def numberOfSteps(num):
        s = 0
        while num > 0:
            if num & 1:
                num -= 1
            else:
                num = num >> 1

            s += 1

        return s