from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _dict = defaultdict(list)
        result = []
        for i in strs:
            i_sorted = tuple(sorted(i))
            _dict[i_sorted].append(i)
            result = _dict.values()
        return result
