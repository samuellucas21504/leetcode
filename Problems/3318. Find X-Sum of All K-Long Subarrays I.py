class Solution(object):
    @staticmethod
    def findXSum(nums, k, x):
        l = 0
        tot = []
        oc = {}

        for r in range(len(nums)):
            if nums[r] in oc:
                oc[nums[r]] += 1
            else:
                oc[nums[r]] = 1

            while r - l + 1 > k:
                oc[nums[l]] -= 1
                if oc[nums[l]] == 0:
                    del oc[nums[l]]

                l += 1

            if r - l + 1 == k:
                top_x = []
                for key, freq in oc.items():
                    inserted = False
                    for i in range(len(top_x)):
                        if freq > top_x[i][1] or (freq == top_x[i][1] and key > top_x[i][0]):
                            top_x.insert(i, (key, freq))
                            inserted = True
                            break
                    if not inserted:
                        top_x.append((key, freq))

                    if len(top_x) > x:
                        top_x.pop()

                tot.append(0)
                for key, freq in top_x:
                    tot[-1] += key * freq

        return tot



s = Solution
print(s.findXSum([1,1,2,2,3,4,2,3], 6, 2))