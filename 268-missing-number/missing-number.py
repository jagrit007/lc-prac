class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_num = 0
        for i,j in enumerate(sorted(nums)):
            if missing_num == j:
                missing_num += 1
        return missing_num