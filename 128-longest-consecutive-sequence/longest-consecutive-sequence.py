class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for i in nums:
            if i-1 not in num_set:
                seq = 0
                while i+seq in num_set:
                    seq += 1
                longest = max(longest, seq)
        return longest