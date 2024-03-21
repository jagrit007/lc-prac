class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        result = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] += 1

            if (r - l + 1) - max(count.values()) > k:
                # move window
                count[s[l]] -= 1 #firstly remove leftmost while moving window
                l+=1 # finally move the window
            result = max(result, r-l+1)
        return result
            