class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # with hashmap
        _map = {} # val: index
        for i, n in enumerate(nums):
            if target - n in _map:
                return [i, _map[target-n]]
            else:
                _map[n] = i
        # without hashmap
        # for i in range(0, len(nums)):
        #     ind1=i
        #     for j in range(i+1, len(nums)):
        #         if nums[ind1]+ nums[j] == target:
        #             print([ind1, j])
        #             return [ind1,j]