class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def helper(ind, sum):
            if ind == len(nums):
                return 1 if sum == target else 0
            if (ind, sum) in dp:
                return dp[(ind, sum)]

            dp[(ind, sum)] = (helper(ind+1, sum + nums[ind]) +
                              helper(ind+1, sum - nums[ind]))
            return dp[(ind, sum)]
        return helper(0, 0)
            

            