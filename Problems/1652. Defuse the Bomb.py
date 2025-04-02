class Solution(object):
    @staticmethod
    def decrypt(code, k):
        if k == 0:
            return [0] * len(code)

        r = []
        for i in range(len(code)):
            r.append(0)
            for j in range(0, abs(k)):
                m = int((k / abs(k)) * (j + 1))
                r[i] += code[(i + m) % len(code)]

        return r