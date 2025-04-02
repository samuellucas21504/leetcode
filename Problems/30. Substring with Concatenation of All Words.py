class Solution:
    @staticmethod
    def findSubstring(s, words):
        word_length = len(words[0])
        total_length = len(words) * word_length
        if len(s) < total_length:
            return []

        need = {}

        for word in words:
            if word in need:
                need[word] += 1
            else:
                need[word] = 1
        res = []

        for i in range(word_length):
            l, r = i, i
            have = {}
            count = 0

            while r <= len(s):
                word = s[r:r+word_length]
                r += word_length

                if word in need:
                    if word in have:
                        have[word] += 1
                    else:
                        have[word] = 1

                    if have[word] == need[word]:
                        count += 1

                if r - l == total_length:
                    if count == len(need):
                        res.append(l)

                    lword = s[l:l+word_length]
                    l += word_length

                    if lword in need:
                        if have[lword] == need[lword]:
                            count -= 1

                        have[lword] -= 1

        return res


print(Solution.findSubstring('a', ['a', 'b']))
print(Solution.findSubstring('barfoothefoobarman', ["foo","bar"]))
print(Solution.findSubstring('wordgoodgoodgoodbestword', ["word","good","best","word"]))
