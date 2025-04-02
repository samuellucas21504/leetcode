class Solution:
    def myAtoi(self, s: str) -> int:
        i32 = (2) ** 31

        started = False
        value = 0
        pointer = 0
        sign = 1

        while pointer < len(s):
            char = s[pointer]
            if char == ' ' and not started:
                pointer += 1
                continue
            elif char == '+' and not started:
                sign = 1
                started = True
                pointer += 1
                continue
            elif char == '-' and not started:
                sign = -1
                started = True
                pointer += 1
                continue

            if not char.isdigit() and not started:
                return 0

            if char.isdigit():
                started = True
                value *= 10
                value += int(char)

                if value >= i32:
                    if sign > 0:
                        return i32 - 1

                    return -i32
            elif not char.isdigit() and started:
                return sign * value

            pointer += 1

        return sign * value