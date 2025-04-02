class Solution(object):
    def maximumLengthSubstring(self, s):
        oc = {}
        l, r, max = 0, 0, 0

        while r < len(s):
            if s[r] in oc:
                oc[s[r]] += 1

                if oc[s[r]] > 2:
                    while l < r and oc[s[r]] > 2:
                        oc[s[l]] -= 1
                        l += 1
            else:
                oc[s[r]] = 1

            if (r - l) > max:
                max = r - l

            r += 1

        return max + 1