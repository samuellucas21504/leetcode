class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        i32 = abs(-2 ** 31)
        m = 1 if x > 0 else -1
        x = abs(x)

        if x > i32:
            return 0

        rn = 0
        while x > 0:
            d = x % 10
            rn = rn * 10 + d
            if rn > i32:
                return 0
            x = x // 10

        return rn * m