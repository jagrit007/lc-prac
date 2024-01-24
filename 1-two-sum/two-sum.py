class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            ind1=i
            for j in range(i+1, len(nums)):
                if nums[ind1]+ nums[j] == target:
                    print([ind1, j])
                    return [ind1,j]