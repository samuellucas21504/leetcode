class Solution(object):
    def reverseWords(self, s):
        ns = ""
        l, r = 0, 0
        while r < len(s):
            if s[r] != " ":
                r += 1
            else:
                ns += s[l:r+1][::-1]
                r += 1
                l = r

        ns += ' '
        ns += s[l:r + 1][::-1]
        return ns[1::]