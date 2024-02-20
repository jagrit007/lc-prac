class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        _set = set()
        for i, j in enumerate(nums):
            if j in _set:
                _set.remove(j)
            else:
                _set.add(j)
        return _set.pop()
                