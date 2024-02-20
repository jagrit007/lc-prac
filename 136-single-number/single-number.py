class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bitwise_num = 0
        for i in nums:
            bitwise_num = bitwise_num ^ i
        return bitwise_num