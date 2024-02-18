class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        _dict = {}
        _dict[0] = -1
        count = 0
        max_len = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            elif nums[i] == 1:
                count += 1
            
            if count in _dict:
                max_len = max(max_len, i - _dict[count])
            else:
                _dict[count] = i
        return max_len