class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def helper(sum, i, arr):
            if(sum == target):
                if arr not in result:
                    result.append(arr[:])
                    return True
            if(sum > target or len(candidates) == i):
                return False
            
            for j in range(i, len(candidates)):
                arr.append(candidates[j])
                helper(sum+candidates[j], j, arr)
                arr.pop() # undo the work / backtrack

        helper(0, 0, [])
        return result