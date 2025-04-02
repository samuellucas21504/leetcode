class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = {}
        m_len = 0

        for r in range(len(s)):
            if s[r] not in seen:
                seen[s[r]] = 1
            else:
                seen[s[r]] += 1
                while s[r] in seen and seen[s[r]] > 1 and l < r:
                    seen[s[l]] -= 1
                    if seen[s[l]] == 0:
                        del seen[s[l]]
                    l += 1

            if m_len < len(s[l:r + 1]):
                m_len = len(s[l:r + 1])

        return m_len