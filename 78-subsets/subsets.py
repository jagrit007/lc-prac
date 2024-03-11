class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def helper(arr, i):
            result.append(arr[:])
            for j in range(i, len(nums)):
                helper(arr + [nums[j]], j+1)

        helper([], 0)
        return result