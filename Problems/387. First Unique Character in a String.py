class Solution(object):
    @staticmethod
    def firstUniqChar(s):
        """
        :type s: str
        :rtype: int
        """
        ar = [0] * len(s)
        for i, c in enumerate(s):
            if ar[ord(c) % len(s)] != 0:
                print(c)
                ar.insert(ord(c) % len(s), i)
            else:
                print(c, 'eta')
                ar[ord(c) % len(s)] = -1

        print(ar)
        for i, v in enumerate(ar):
            if v == 1:
                return i

        return -1
