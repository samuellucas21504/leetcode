class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cl_m = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in cl_m:
                if stack and stack[-1] == cl_m[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not len(stack)