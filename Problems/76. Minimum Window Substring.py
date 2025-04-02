class Solution:
    @staticmethod
    def minWindow(s, t):
        if len(s) < len(t):
            return ""

        if s == t:
            return s

        need, have = {}, {}

        for c in t:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1

        l = 0
        res = ''
        min_len = float("inf")
        have_count = 0

        for r in range(l, len(s)):
            if s[r] in need:
                if s[r] in have:
                    have[s[r]] += 1
                else:
                    have[s[r]] = 1

                if have[s[r]] == need[s[r]]:
                    have_count += 1

            while have_count == len(need):
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    res = s[l:r+1]

                if s[l] in need:
                    have[s[l]] -= 1

                    if have[s[l]] < need[s[l]]:
                        have_count -= 1

                l += 1

        return res

print(Solution.minWindow('ADOBECODEBANC', 'ABC'))
print(Solution.minWindow('a', 'aa'))
print(Solution.minWindow('a', 'a'))
print(Solution.minWindow('ab', 'a'))
print(Solution.minWindow('abc', 'b'))
print(Solution.minWindow('bbaa', 'aba'))
