class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def helper(intermediate, left, right):
            if len(intermediate) == n * 2:
                result.append(intermediate)
                return
            if left < n:
                helper(intermediate + "(", left+1, right)
            if right < left:
                helper(intermediate + ")", left, right+1)
        
        helper('', 0, 0)
        return result