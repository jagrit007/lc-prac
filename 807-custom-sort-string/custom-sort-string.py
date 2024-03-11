class Solution:
    def customSortString(self, order: str, s: str) -> str:
        start = ""
        end = ""
        hmap = defaultdict(int)
        
        for i in s:
            if i not in order:
                end+= i
            else:
                hmap[i] += 1
        
        for char in order:
            start += hmap[char] * char

        return start + end