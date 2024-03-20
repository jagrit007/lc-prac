class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currMax = 0

        for ind, i in enumerate(s):
            hmap = defaultdict(int)
            ptr_2 = ind + 1
            hmap[i] += 1
            count = 1
            while ptr_2 < len(s) and s[ptr_2] not in hmap:
                hmap[s[ptr_2]] += 1
                ptr_2 += 1
                count += 1
            currMax = max(currMax, count)
        return currMax