class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l_prod = 1 # ->
        r_prod = 1 # both are initially 1 because there is no numbers to the left or right of the first number (`edge cases` btw)
        left = [0] * n
        right = [0] * n

        for i in range(n):
            j = -i - 1
            left[i] = l_prod
            right[j] = r_prod
            l_prod *= nums[i]
            r_prod *= nums[j]

        return [x*y for x,y in zip(left, right)]