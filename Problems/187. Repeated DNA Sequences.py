class Solution:
    @staticmethod
    def findRepeatedDnaSequences(s):
        if len(s) < 10:
            return []

        d = {}
        seen = []

        for i in range(0, len(s)-9):
            ss = s[i:i+10]
            if ss in d:
                d[ss] += 1
            else:
                d[ss] = 1

        for key in d:
            if d[key] > 1:
                seen.append(key)

        return seen

print(Solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(Solution.findRepeatedDnaSequences("AAAAAAAAAAA"))
print(Solution.findRepeatedDnaSequences("AAAAAAAAAAAAA"))
